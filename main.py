# Diff Tool - main.py
# Entry point for the Diff Tool
import config, theme
import os
import sys

print "Testing config.py..."
if sys.platform == "Windows":
	path = os.getcwd() + '\\config.local.json'
elif "linux" in sys.platform.lower():
	print 'test'
	path = os.getcwd() + '/config.local.json'
	
conf = config.Config(path)
conf.about()
conf.listThemes()

print "Testing theme.py..."
style = theme.Theme(conf)
style.about()
