# Diff Tool - main.py
# Entry point for the Diff Tool
import config, theme
import os

print "Testing config.py..."
path = os.getcwd() + '\\config.json'
conf = config.Config(path)
conf.about()
conf.listThemes()

print "Testing theme.py..."
style = theme.Theme(conf)
style.about()