# Diff Tool - config.py
# defines the config object
import globalFunc as glb
import json

class Config():
	def __init__(self, path=''):
		# only parameter is the full path of the config.json file
		self.configFile = path
		
		if len(self.configFile) > 0:
			# set up config object
			self.clearObject()
		
			# get json string 
			self.getJsonString()
			
			# load config object
			self.loadConfig(True)
			
			# load themes
			self.loadThemes(True)
		else:
			print 'WARNING: No Configuration file has been loaded. Please load one for configuration to continue.'
			
	def clearObject(self):
		self.name = ''
		self.author = ''
		self.version = ''
		self.theme = ''
		self.themes = []
		self.themeDirectory = ''
		self.appDirectory = ''
		self.versionDirectory = ''
		self.description = ''
		
	def updateConfig(self, key, value):
		f = open(self.configFile, 'r+')
		jsonString = json.loads(f.read())
		tmp = jsonString[key]
		jsonString[key] = value
		f.seek(0)
		json.dump(jsonString, f)
		f.truncate()
		f.close()
	
	def getJsonString(self):
		# returns a json string from self.configFile
		self.jsonString = ''
		self.jsonString = glb.getJsonString(self.configFile)	
		
	
	def loadConfig(self, firstLoad=False):
		if firstLoad == False:
			# refresh json string, in case config has changed
			self.getJsonString()
		
		# populate object
		self.name = self.jsonString["name"]
		self.author = self.jsonString["author"]
		self.version = self.jsonString["version"]
		self.description = self.jsonString["description"]
		self.theme = self.jsonString["theme"]
		self.themeDirectory = self.jsonString["themeDirectory"]
		self.appDirectory = self.jsonString["appDirectory"]
		self.versionDirectory = self.jsonString["versionDirectory"]
		
	def loadThemes(self, firstLoad=False):
		if firstLoad == False:
			# refresh json string, in case config has changed
			self.getJsonString()
		
		# populate themes
		themes = self.jsonString["themes"]
		for i in themes:
			theme = {"name": i["name"], "file": i["file"]}
			self.themes.append(theme)
		
	def about(self):
		print '='*80
		print 'About: ' + self.name
		print 'Version: ' + self.version
		print 'Author: ' + self.author
		print self.description
		print '='*80
		print ''
		
	def listThemes(self):
		print '='*80
		print 'Themes:'
		for i in self.themes:
			print ' - ' + i["name"] + ' [File Name: ' + i["file"] + ']'
		print '='*80
		print ''