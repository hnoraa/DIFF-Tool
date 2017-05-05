# Diff Tool - project.py
# project management
import globalFunc as glb
import json
import os

class Project():
	def __init__(self):
		self.project = {
			'author': '',
			'name': '',
			'description': '',
			'createDate': ''
		}
		
	def create(self, project):
		# create a project
		self.project['name'] = project['name']
		self.project['description'] = project['description']
		self.project['author'] = project['author']
		self.project['createDate'] = glb.getTodaysDateAsString()
		
	def load(self, projectName):
		# load json into string
		f = open(glb.projectDirectory() + projectName + '.json', 'r')
		jsonString = json.loads(f.read())
		f.close()
		
		# convert to project object
		self.project['name'] = jsonString['name']
		self.project['author'] = jsonString['author']
		self.project['description'] = jsonString['description']
		self.project['createDate'] = jsonString['createDate']
		
	
	def save(self):
		# save project as json file
		obj = json.dumps(self.project)
		f = open(glb.projectDirectory() + self.project['name'] + '.json', 'w')
		f.write(obj)
		f.close()
		
	def listProjects(self):
		# list the projects in the projects directory
		for file in os.listdir(glb.homeDirectory() + "Projects"):
			if file.endswith(".json"):
				print os.path.splitext(file)[0]
		return ''