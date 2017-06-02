# Diff Tool - global.py
# global, app-wide functionality
import os
import sys
import json
import config
import theme
import datetime
import jsonschema
from jsonschema import validate
import project as p

class Globals:
	def __init__(self):
		# the current project, project is loaded via project object
		self.currentProject = p.Project()

		# global config object
		self.configuration = None

		# global theme
		self.theme = None
		
	def loadConfig(self, fileName):
		self.configuration = loadConfig(fileName)
		
	def loadTheme(self):
		self.theme = theme.Theme(self.configuration)

def getTodaysDateAsString():
	# returns todays date as a string
	return datetime.date.today().strftime("%B %d, %Y")


def loadConfig(fileName):
	# load the config object
	path = homeDirectory() + fileName
	return config.Config(path)


def homeDirectory():
	# returns home directory in OS correct syntax
	path = os.getcwd()
	if "win" in sys.platform:
		path += '\\'
	elif "linux" in sys.platform.lower():
		path += '/'
	return path


def themesDirectory():
	# returns themes directory in OS correct syntax
	path = os.getcwd()
	if "win" in sys.platform:
		path += '\\Themes\\'
	elif "linux" in sys.platform.lower():
		path += '/Themes/'
	return path


def versionsDirectory():
	# returns versions directory in OS correct syntax
	path = os.getcwd()
	if "win" in sys.platform:
		path += '\\Versions\\'
	elif "linux" in sys.platform.lower():
		path += '/Versions/'
	return path


def schemaDirectory():
	# returns schema directory in OS correct syntax
	path = os.getcwd()
	if "win" in sys.platform:
		path += '\\Schema\\'
	elif "linux" in sys.platform.lower():
		path += '/Schema/'
	return path


def projectDirectory():
	# returns schema directory in OS correct syntax
	path = os.getcwd()
	if "win" in sys.platform:
		path += '\\Projects\\'
	elif "linux" in sys.platform.lower():
		path += '/Projects/'
	return path


def getJsonString(fn):
	# returns a json string
	f = open(fn, 'r')
	jsonString = json.loads(f.read())
	f.close()
	return jsonString


def getFileLineList(fn):
	# returns a list of lines in the file
	lines = []
	f = open(fn, 'r')
	for line in f:
		line = line.strip()
		lines.append(line)
	f.close()
	return lines


def validateJson(schema, jsonFile):
	# validate json string against schema
	schemaString = getJsonString(schema)
	jsonString = getJsonString(jsonFile)
	
	try:
		validate(schemaString, jsonString)
		return True
	except jsonschema.exceptions.ValidationError as e:
		return False
