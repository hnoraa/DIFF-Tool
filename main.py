# Diff Tool - main.py
# Entry point for the Diff Tool
import cmdLineUi
import gui
import globalFunc as glb
from globalFunc import Globals
from Tkinter import *

# flags
COMMAND_LINE = False
DEBUG = True

# set global object
glbs = Globals()

# load and validate
# load config
if glb.validateJson(glb.schemaDirectory() + 'configSchema.json', glb.homeDirectory() + 'config.local.json'):
	glbs.loadConfig('config.local.json')
else:
	print "ERROR: Invalid Configuration"
	sys.exit()

# load themes
if glb.validateJson(glb.schemaDirectory() + 'themeSchema.json', glb.themesDirectory() + 'defaultTheme.json'):
	glbs.loadTheme()
else:
	print "ERROR: Invalid Theme"
	sys.exit()

# toggle between command line & GUI
if COMMAND_LINE:
	if DEBUG:
		# debugging area for testing new features quickly
		print "Testing Diff Tool..."
		print glbs.configuration.theme
		print glbs.theme.name
		
	cmdLn = cmdLineUi.CmdLineUi(glbs)
	cmdLn.greet()
	cmdLn.mainMenu()
else:
	root = Tk()
	app = gui.DiffToolWindow(root, glbs)
	root.resizable(width=False, height=False)
	root.mainloop()

sys.exit()
