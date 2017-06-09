# Diff Tool - main.py
# Entry point for the Diff Tool
import cmdLineUi
import globalFunc as glb
from globalFunc import Globals
import sys

# flags
COMMAND_LINE = True
DEBUG = True

# set global object
glbs = Globals()

# load and validate
# load config
if glb.validateJson(glb.schemaDirectory() + 'configSchema.json', glb.homeDirectory() + 'config.local.json'):
	glbs.loadConfig('config.local.json')
else:
	print "ERROR: Invalid Confguration"
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
	# GUI (possible future implementation)
	pass

sys.exit()
