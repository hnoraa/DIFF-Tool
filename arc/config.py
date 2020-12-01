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
		self.theme = ''
		self.themes = []
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
		self.description = self.jsonString["description"]
		self.theme = self.jsonString["theme"]
	
	def loadThemes(self, firstLoad=False):
		if not firstLoad:
			# refresh json string, in case config has changed
			self.getJsonString()
		
		# populate themes
		themes = self.jsonString["themes"]
		for i in themes:
			theme = {"name": i["name"], "file": i["file"]}
			self.themes.append(theme)
	
	def about(self, gui=False):
		text = '=' * 80 + '\n'
		if gui:
			text = ''
		text = ''.join([text, glb.getTodaysDateAsString() + '\n'])
		text = ''.join([text, 'About: ' + self.name + '\n'])
		text = ''.join([text, 'Version: 1.0.0' + '\n'])
		text = ''.join([text, 'Author: ' + self.author + '\n'])
		text = ''.join([text, self.description + '\n'])
		if not gui:
			text = ''.join([text, '=' * 80 + '\n'])
		return text
	
	def listThemes(self, gui=False):
		text = '=' * 80 + '\n'
		if gui:
			text = ''
		text = ''.join([text, 'Themes:\n'])
		for i in self.themes:
			if i["name"] in self.theme:
				msg = ' - Current Theme: '
			else:
				msg = ' - '
			text = ''.join([text, msg + i["name"] + ' [File Name: ' + i["file"] + ']\n'])
			if not gui:
				text = ''.join([text, '=' * 80 + '\n'])
		return text
