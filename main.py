# Diff Tool - main.py
# Entry point for the Diff Tool
import theme
import cmdLineUi
import globalFunc as glb
from globalFunc import Globals
import sys

# flags
COMMAND_LINE = True
DEBUG = True

# set global object
globals = Globals()

# load and validate
# load config
if glb.validateJson(glb.schemaDirectory() + 'configSchema.json', glb.homeDirectory() + 'config.local.json'):
	globals.loadConfig('config.local.json')
else:
	print "ERROR: Invalid Confguration"
	sys.exit()

# load themes
if glb.validateJson(glb.schemaDirectory() + 'themeSchema.json', glb.themesDirectory() + 'defaultTheme.json'):
	globals.loadTheme()
else:
	print "ERROR: Invalid Theme"
	sys.exit()

# toggle between command line & GUI
if COMMAND_LINE:
	if DEBUG:
		import htmlGen as hm
		# debugging area for testing new features quickly
		print "Testing Diff Tool..."
		print globals.configuration.theme
		print globals.theme.name
		
	cmdLn = cmdLineUi.CmdLineUi(globals)
	cmdLn.greet()
	cmdLn.mainMenu()
else:
	# GUI (possible future implementation)
	pass

sys.exit()
