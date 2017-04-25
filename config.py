# Diff Tool - config.py
# defines the config object
import json

class Config():
	def __init__(self, path):
		# set up config object
		self.name = ''
		self.author = ''
		self.version = ''
		self.theme = ''
		self.themeDirectory = ''
		self.themes = []
		self.directory = ''
		self.scriptDirectory = ''
		self.versionDirectory = ''
		
		# only parameter is the full path of the config.json file
		self.configFile = path
		
	def loadConfig(self):
		config = json.loads(open(self.configFile).read())
		
		self.name = config["name"]
		self.author = config["author"]
		self.version = config["version"]
		self.theme = config["theme"]
		self.themeDirectory = config["themeDirectory"]
		self.directory = config["directory"]
		self.scriptDirectory = config["scriptDirectory"]
		self.versionDirectory = config["versionDirectory"]
