# Diff Tool - versionControl.py
# version control for the projects
import globalFunc as glb
import zipfile
import re
import os


class VersionControl:
	def __init__(self, project):
		self.project = project
	
	def getArchiveName(self):
		# get the name of the archive for the project
		return glb.versionsDirectory() + self.project.project['guid'] + '.zip'
	
	def versionDocument(self, fileName):
		# add a version to the new document
		curText, curVer = self.getLatestVersion()
		newVer = curVer + 1
		
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
