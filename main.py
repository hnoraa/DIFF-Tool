# Diff Tool - main.py
# Entry point for the Diff Tool
import theme
import cmdLineUi
import globalFunc as glb
import sys

# flags
COMMAND_LINE = True
DEBUG = True

# load and validate
# load config
if glb.validateJson(glb.schemaDirectory() + 'configSchema.json', glb.homeDirectory() + 'config.local.json'):
	conf = glb.loadConfig('config.local.json')
else:
	print "ERROR: Invalid Confguration"
	sys.exit()

# load themes
if glb.validateJson(glb.schemaDirectory() + 'themeSchema.json', glb.themesDirectory() + 'defaultTheme.json'):
	style = theme.Theme(conf)
else:
	print "ERROR: Invalid Theme"
	sys.exit()

# toggle between command line & GUI
if COMMAND_LINE:
	if DEBUG:
		# debugging area for testing new features quickly
		print "Testing Diff Tool..."
	
	cmdLn = cmdLineUi.CmdLineUi(conf)
	cmdLn.greet()
	cmdLn.mainMenu()
else:
	# GUI (possible future implementation)
	pass

sys.exit()
