# Diff Tool - main.py
# Entry point for the Diff Tool
import config, theme, cmdLineUi
import htmlGen as hg
import globalFunc as glb

# flags
COMMAND_LINE = True
DEBUG = True

# load config
if glb.validateJson(glb.schemaDirectory()+'configSchema.json', glb.homeDirectory()+'config.local.json'):
	conf = glb.loadConfig('config.local.json')
else:
	print "ERROR: Invalid Confguration"
	glb.quit()

# load themes
if glb.validateJson(glb.schemaDirectory()+'themeSchema.json', glb.themesDirectory()+'defaultTheme.json'):
	style = theme.Theme(conf)
else:
	print "ERROR: Invalid Theme"
	glb.quit()

# toggle between command line & GUI
if COMMAND_LINE:
	if DEBUG:
		# debugging area for testing new features quickly
		print "Testing Diff Tool..."
		cmdLn = cmdLineUi.CmdLineUi(conf)
		cmdLn.greet()
		cmdLn.mainMenu()
	else:
		cmdLn = cmdLineUi.CmdLineUi(conf)
		cmdLn.greet()
		cmdLn.mainMenu()
else:
	# GUI (possible future implementation)
	pass

glb.quit()