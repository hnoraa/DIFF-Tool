# Diff Tool - main.py
# Entry point for the Diff Tool
import config, theme
import globalFunc as glb
from jsonschema import validate

# flags
COMMAND_LINE = True
DEBUG = True

# load config
conf = glb.loadConfig('config.local.json')

# load themes

if COMMAND_LINE:
	pass
else:
	# GUI (possible future implementation)
	pass
	
if DEBUG:
	print "Testing config.py..."
	conf.about()
	conf.listThemes()
	
	print "Updating config file"
	conf.updateConfig("author", "Aaron E. Horeth")

	print "Testing theme.py..."
	style = theme.Theme(conf)
	style.about()
	style.createTheme()
	for c in style.css:
		print c
		
	print "Testing file loading..."
	file = glb.homeDirectory() + 'test_text_1.test.txt'

	txt = open(file)
	t = txt.read()
	txt.close()

	print t
	print type(t)

	x = glb.getFileLineList(file)
	print x
	print type(x)
	
	# test json schema
	schema = {
		"type": "object",
		"properties": {
			"price": { "type": "number" },
			"name": { "type": "string" }
		}
	}
	
	validate({"name": "Eggs", "price": 20.99}, schema)
	validate({"name": "Eggs", "price": "Invalid"}, schema)
	
	
	
