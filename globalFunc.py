# Diff Tool - global.py
# global, app-wide functionality
import os
import sys
import json
import config
import datetime
from jsonschema import validate

def getTodaysDateAsString():
	return datetime.date.today().strftime("%B %d, %Y")

def quit():
	sys.exit()

def loadConfig(fileName):
	# load the config object
	path = homeDirectory() + fileName
	conf = config.Config(path)
	return conf

def homeDirectory():
	# returns home directory in OS correct syntax
	path = os.getcwd()
	if ("win") in sys.platform:
		path += '\\'
	elif ("linux") in sys.platform.lower():
		path += '/'
	return path

def themesDirectory():
	# returns themes directory in OS correct syntax
	path = os.getcwd()
	if ("win") in sys.platform:
		path += '\\Themes\\'
	elif ("linux") in sys.platform.lower():
		path += '/Themes/'
	return path
	
def versionsDirectory():
	# returns versions directory in OS correct syntax
	path = os.getcwd()
	if ("win") in sys.platform:
		path += '\\Versions\\'
	elif ("linux") in sys.platform.lower():
		path += '/Versions/'
	return path
	
def schemaDirectory():
	# returns schema directory in OS correct syntax
	path = os.getcwd()
	if ("win") in sys.platform:
		path += '\\Schema\\'
	elif ("linux") in sys.platform.lower():
		path += '/Schema/'
	return path
	
def projectDirectory():
	# returns schema directory in OS correct syntax
	path = os.getcwd()
	if ("win") in sys.platform:
		path += '\\Projects\\'
	elif ("linux") in sys.platform.lower():
		path += '/Projects/'
	return path
	
def getJsonString(fileName):
	# returns a json string
	f = open(fileName, 'r')
	jsonString = json.loads(f.read())
	f.close()
	return jsonString
	
def getFileLineList(fileName):
	# returns a list of lines in the file
	lines = []
	f = open(fileName, 'r')
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
		
# these 2 methods will be rolled into a versioning method
# right now they're kind of placeholders
def listFiles(path):
	# returns a list of files in the specified directory
    return os.listdir(path)

def getFileNameParts(fileName):
	# returns list [0]: file name. [1]: extension
    return os.path.splitext(fileName)