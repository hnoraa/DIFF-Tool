# Diff Tool - config.py
# defines the config object
import globalFunc as glb
import json


class Config:
	def __init__(self, path=''):
		# only parameter is the full path of the config.json file
		self.configFile = path
		self.jsonString = ''
		
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
			pass
	
	def clearObject(self):
		self.name = ''
		self.author = ''
		self.version = ''
		self.theme = ''
		self.themes = []
		self.themeDirectory = ''
		self.appDirectory = ''
		self.schemaDirectory = ''
		self.versionDirectory = ''
		self.projectDirectory = ''
		self.description = ''
	
	def updateConfig(self, key, value):
		if key == "theme":
			value = ''.join([value, ".json"])
			
		glb.updateJsonConfig(self.configFile, key, value)
	
	def getJsonString(self):
		# returns a json string from self.configFile
		self.jsonString = glb.getJsonString(self.configFile)
	
	def loadConfig(self, firstLoad=False):
		if not firstLoad:
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
		self.schemaDirectory = self.jsonString["schemaDirectory"]
		self.versionDirectory = self.jsonString["versionDirectory"]
		self.projectDirectory = self.jsonString["projectDirectory"]
	
	def loadThemes(self, firstLoad=False):
		if not firstLoad:
			# refresh json string, in case config has changed
			self.getJsonString()
		
		# populate themes
		themes = self.jsonString["themes"]
		for i in themes:
			theme = {"name": i["name"], "file": i["file"]}
			self.themes.append(theme)
	
	def about(self):
		print '=' * 80
		print glb.getTodaysDateAsString()
		print 'About: ' + self.name
		print 'Version: ' + self.version
		print 'Author: ' + self.author
		print self.description
		print '=' * 80
		return ''
	
	def listThemes(self):
		print '=' * 80
		print 'Themes:'
		for i in self.themes:
			if i["name"] in self.theme:
				msg = ' - Current Theme: '
			else:
				msg = ' - '
			print msg + i["name"] + ' [File Name: ' + i["file"] + ']'
		print '=' * 80
		return ''
