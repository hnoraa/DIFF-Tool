# Diff Tool - global.py
# global, app-wide functionality
import os
import sys
import json
import config
from jsonschema import validate

def loadConfig(fileName):
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
	path = os.getcwd()
	if ("win") in sys.platform:
		path += '\\Schema\\'
	elif ("linux") in sys.platform.lower():
		path += '/Schema/'
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
		return 'Valid JSON'
	except jsonschema.exceptions.ValidationError as e:
		return 'Invalid JSON'