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
		self.currentDiff = []
	
	def create(self, project, f):
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
		finally:
			print 'Zip file created!'
			zf.close()
			self.save()
	
	def load(self, projectName):
		# check to see if project exists/get project name
		x = self.getProjectName(projectName)
		if(x is None):
			return ''
		
		# load json into string
		jsonString = glb.getJsonString(glb.projectDirectory() + x + '.json')
		
		# convert to project object
		self.project['name'] = jsonString['name']
		self.project['author'] = jsonString['author']
		self.project['description'] = jsonString['description']
		self.project['createDate'] = jsonString['createDate']
		self.project['guid'] = jsonString['guid']
		self.project['latestVersion'] = int(jsonString['latestVersion'])
	
	def save(self):
		try:
			# save project as json file
			obj = json.dumps(self.project)
			f = open(glb.projectDirectory() + self.project['name'] + '.json', 'w')
			f.write(obj)
		except IOError as e:
			print e.message
		finally:
			f.close()
			self.load(self.project['name'])
	
	def listProjects(self):
		# list the projects in the projects directory
		for f in os.listdir(glb.homeDirectory() + "Projects"):
			if f.endswith(".json"):
				print os.path.splitext(f)[0]
		return ''
		
	def searchProjects(self, searchString):
		searches = searchString.lower().split('*')
		
		files = []	
		for f in os.listdir(glb.homeDirectory() + "Projects"):
			if f.endswith(".json"):
				x = os.path.splitext(f.lower())[0]
				if any(s in x for s in searches):
					files.append(x)
		return files
				
	def getProjectName(self, name):
		for f in os.listdir(glb.homeDirectory() + "Projects"):
			if f.endswith(".json"):
				x = os.path.splitext(f)[0]
				if name.lower() in x.lower():
					return x
		return None
		
	def projectExists(self, name):
		files = []
		for f in os.listdir(glb.projectDirectory()):
			if f.endswith(".json"):
				files.append(os.path.splitext(f.lower())[0])
				
		if name.lower() in files:
			# the file already exists
			return True
		
		return False

	def editProject(self, key, value, permission=False):
		# edit the project config
		if (key == 'latestVersion' or key == 'guid' or key == 'createDate')\
				and not permission:
			print 'Parameter restricted'
			return ''
		
		if key == 'name':
			name = self.project['name']
			self.project['name'] = value
			self.save()
			
			# delete old project file
			os.remove(glb.projectDirectory() + name + '.json')

		cf = glb.projectDirectory() + self.project['name'] + '.json'
		glb.updateJsonConfig(cf, key, value)
		
		# reload project
		self.load(self.project['name'])
		
	def deleteProject(self):
		# first delete project version file, then delete project json file
		os.remove(glb.versionsDirectory() + self.project['guid'] + '.zip')
		os.remove(glb.projectDirectory() + self.project['name'] + '.json')
	
	def versionDocument(self, fileName):
		# add a version to the new document
		curVer = self.getLatestVersion()
		newVer = curVer + 1
		
		# update latest version in json schema and save
		self.project['latestVersion'] = newVer
		self.editProject('latestVersion', newVer, permission=True)
		
		# split fileName into name and extension
		fn = os.path.splitext(os.path.basename(fileName))[0]
		fext = os.path.splitext(os.path.basename(fileName))[1]
		
		# new version
		newName = '{0}_ver_{1}{2}'.format(fn, str(newVer), fext)
		
		zf = zipfile.ZipFile(glb.versionsDirectory() + self.project['guid'] + '.zip', mode='a')
		try:
			zf.write(fileName, arcname=newName)
		except zipfile.error:
			print str(zipfile.error)
		finally:
			self.save()
			print 'Appended successfully'
			zf.close()
	
	def getFilesInArchive(self):
		# get list of all files in archive
		fn = glb.versionsDirectory() + self.project['guid'] + '.zip'
		zf = zipfile.ZipFile(fn, 'r')
		nl = zf.namelist()
		zf.close()
		return nl
	
	def listVersions(self):
		# get a list of all version numbers in the archive
		files = self.getFilesInArchive()
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
		files = self.getFilesInArchive()
		
		current = -1
		search = '_ver_'
		
		for f in files:
			x = f.find(search)
			if x > -1:
				# there could be multiple _ver_ instances on the file, take the last
				nums = re.findall(r'_ver_([0-9]*)', f)
				ver = int(nums[len(nums) - 1])
				if ver > current:
					current = ver
		
		return current

	def compareFiles(self, fList):
		self.currentDiff = []
		
		# open files from archive and compare
		arc = zipfile.ZipFile(glb.versionsDirectory() + self.project['guid'] + '.zip', 'r')
		linesF1 = arc.open(fList[0]).readlines()
		linesF1 = [x.strip() for x in linesF1]
		linesF2 = arc.open(fList[1]).readlines()
		linesF2 = [x.strip() for x in linesF2]
		arc.close()
		
		# length to iterate over
		diffLength = len(linesF1) if len(linesF1) > len(linesF2) else len(linesF2)
		
		for f1 in range(len(linesF1)):
			if len(linesF1[f1]) < 1:
				linesF1[f1] = '<br />\n'
				
		for f2 in range(len(linesF2)):
			if len(linesF2[f2]) < 1:
				linesF2[f2] = '<br />\n'
		
		# pad file that has less lines
		if len(linesF1) > len(linesF2):
			add = len(linesF1) - len(linesF2)
			for x in range(0, add):
				linesF2.append('<br />\n')
		
		elif len(linesF1) < len(linesF2):
			add = len(linesF2) - len(linesF1)
			for x in range(0, add):
				linesF1.append('<br />\n')
		
		# compare
		for x in range(0, diffLength):
			difference = False if linesF1[x] == linesF2[x] else True
			diffType = "" if difference is False else ("+" if len(linesF1[x]) < len(linesF2[x]) else "-")
			
			self.currentDiff.append({
				"firstFile": linesF1[x],
				"secondFile": linesF2[x],
				"difference": difference,
				"type": diffType
			})
