# Diff Tool - project.py
# project management
import globalFunc as glb
import json
import uuid
import os
import zipfile
import re

class Project:
	def __init__(self):
		self.project = {
			'author': '',
			'name': '',
			'description': '',
			'createDate': '',
			'guid': '',
			'latestVersion': 0
		}
	
	def create(self, project, f, globals):
		# create a project
		self.project['name'] = project['name']
		self.project['description'] = project['description']
		self.project['author'] = project['author']
		self.project['createDate'] = glb.getTodaysDateAsString()
		self.project['guid'] = str(uuid.uuid4())
		self.project['latestVersion'] = 1
		
		# create a zip directory and place file in it
		fn = os.path.splitext(os.path.basename(f))[0] + '_ver_1' + os.path.splitext(os.path.basename(f))[1]
		zf = zipfile.ZipFile(glb.versionsDirectory() + self.project['guid'] + '.zip', mode='w')
		try:
			zf.write(f, arcname=fn)
		except zipfile.error:
			print str(zipfile.error)
			pass
		finally:
			print 'Zip file created!'
			zf.close()
			self.save()
			# set current project to newly created project
			globals.currentProject = self.project
	
	def load(self, projectName, globals):
		# load json into string
		jsonString = glb.getJsonString(glb.projectDirectory() + projectName + '.json')
		
		# convert to project object
		self.project['name'] = jsonString['name']
		self.project['author'] = jsonString['author']
		self.project['description'] = jsonString['description']
		self.project['createDate'] = jsonString['createDate']
		self.project['guid'] = jsonString['guid']
		self.project['latestVersion'] = int(jsonString['latestVersion'])
		
		globals.currentProject = self.project
	
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
				files.append(os.path.splitext(f.lower())[0])
				
		if name.lower() in files:
			# the file already exists
			return True
		
		return False
		
	def updateProject(self, newVersion, globals):
		f = open(glb.projectDirectory() + self.project['name'] + '.json', 'r+')
		
		# find key, replace its value
		jsonString = json.loads(f.read())
		tmp = jsonString['latestVersion']
		jsonString['latestVersion'] = newVersion
		
		# find in file contents and replace
		f.seek(0)
		json.dump(jsonString, f)
		
		f.truncate()
		f.close()
		
		self.load(self.project['name'], globals)
	
	def deleteProject(self):
		return True
	
	def getArchiveName(self):
		# get the name of the archive for the project
		return glb.versionsDirectory() + self.project['guid'] + '.zip'
	
	def versionDocument(self, fileName):
		# add a version to the new document
		curText, curVer = self.getLatestVersion()
		newVer = curVer + 1
		
		# update latest version in json schema and save
		self.project['latestVersion'] = newVer
		self.updateProject(newVer)
		
		# split fileName into name and extension
		fn = os.path.splitext(os.path.basename(fileName))[0]
		fext = os.path.splitext(os.path.basename(fileName))[1]
		
		# new version
		newName = '{0}_ver_{1}{2}'.format(fn, str(newVer), fext)
		
		return newName
	
	def getFilesInArchive(self):
		# get list of all files in archive
		fn = self.getArchiveName()
		zf = zipfile.ZipFile(fn, 'r')
		
		return zf.namelist()
	
	def listVersions(self):
		# get a list of all version numbers in the archive
		fn = self.getArchiveName()
		files = self.getFilesInArchive(fn)
		versions = []
		
		for f in files:
			v = re.findall(r'_ver_([0-9]*)', f)
			versions.append(int(v[len(v) - 1]))
		
		return versions
	
	def getLatestVersion(self):
		# regex for finding number after _ver_ in file name
		# r'_ver_([0-9]*)'
		# ex: finds 009 in test_text_ver_009.txt
		# version will be in match.groups[0]
		
		# get zip file name from project object
		fn = self.getArchiveName()
		files = self.getFilesInArchive(fn)
		
		currentVersionS = ''
		currentVersionN = -1
		search = '_ver_'
		
		for f in files:
			x = f.find(search)
			if x > -1:
				# there could be multiple _ver_ instances on the file, take the last
				nums = re.findall(r'_ver_([0-9]*)', f)
				ver = int(nums[len(nums) - 1])
				if ver > currentVersionN:
					currentVersionN = ver
					currentVersionS = f
		
		return currentVersionS, currentVersionN