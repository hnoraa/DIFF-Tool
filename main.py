# Diff Tool - main.py
# Entry point for the Diff Tool
import config
import os

print "Testing config.py..."
path = os.getcwd() + '\\config.json'
conf = config.Config(path)
conf.about()
conf.listThemes()