# Diff Tool - global.py
# global, app-wide functionality
import os
import sys
import json
import config

def loadConfig(fileName):
	path = cwd() + fileName
	conf = config.Config(path)
	return conf

def cwd():
	# returns cwd in OS correct syntax
	path = os.getcwd()
	if ("win") in sys.platform:
		path += '\\'
	elif ("linux") in sys.platform.lower():
		path += '/'
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