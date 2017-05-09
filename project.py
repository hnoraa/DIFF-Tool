# Diff Tool - project.py
# project management
import globalFunc as glb
import json
import uuid
import os
import zipfile

class Project:
	def __init__(self):
		self.project = {
			'author': '',
			'name': '',
			'description': '',
			'createDate': '',
			'guid': ''
		}
	
	def create(self, project, file):
		# create a project
		self.project['name'] = project['name']
		self.project['description'] = project['description']
		self.project['author'] = project['author']
		self.project['createDate'] = glb.getTodaysDateAsString()
		self.project['guid'] = str(uuid.uuid4())
		
		# create a zip directory and place file in it
		fn = os.path.splitext(os.path.basename(file))[0] + '_ver_1' + os.path.splitext(os.path.basename(file))[1]
		zf = zipfile.ZipFile(self.project['guid'] + '.zip', mode='w')
		try:
			zf.write(file, arcname=fn)
		except zipfile.error:
			print str(zipfile.error)
			pass
		finally:
			print 'Zip file created!'
			zf.close()
			self.save()
			# set current project to newly created project
			glb.currentProject = self.project
	
	def load(self, projectName):
		# load json into string
		jsonString = glb.getJsonString(glb.projectDirectory() + projectName + '.json')
		
		# convert to project object
		self.project['name'] = jsonString['name']
		self.project['author'] = jsonString['author']
		self.project['description'] = jsonString['description']
		self.project['createDate'] = jsonString['createDate']
		self.project['guid'] = jsonString['guid']
		
		glb.currentProject = self.project
	
	def save(self):
		# save project as json file
		obj = json.dumps(self.project)
		f = open(glb.projectDirectory() + self.project['name'] + '.json', 'w')
		f.write(obj)
		f.close()
	
	def listProjects(self):
		# list the projects in the projects directory
		for f in os.listdir(glb.homeDirectory() + "Projects"):
			if f.endswith(".json"):
				print os.path.splitext(f)[0]
		return ''

	def projectExists(self, name):
		files = []
		for f in os.listdir(glb.homeDirectory() + "Projects"):
			if f.endswith(".json"):
				files.append(os.path.splitext(f)[0])
				
		if name in files:
			# the file already exists
			return True
		
		return False
	