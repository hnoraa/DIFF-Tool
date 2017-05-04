# Diff Tool - main.py
# Entry point for the Diff Tool
import config, theme
import htmlGen as hg
import globalFunc as glb
from jsonschema import validate

# flags
COMMAND_LINE = True
DEBUG = False

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
		print "Testing config.py..."
		conf.about()
		conf.listThemes()
		
		print "Testing theme.py..."
		style.about()
		
		print "Testing html generation..."
		document = hg.HtmlGen(style, '')
		document.gen()
		document.save()
			
		glb.quit()
	else:
		print "Diff Tool"
else:
	# GUI (possible future implementation)
	pass
	
# file comparison
print "Comparing 2 files..."

# open two files
files = ["test_text_1.test.txt", "test_text_2.test.txt"]
diffs = []

# read files
f1 = open(files[0], "r")
linesF1 = f1.readlines()
linesF1 = [x.strip() for x in linesF1]
f1.close()

f2 = open(files[1], "r")
linesF2 = f2.readlines()
linesF2 = [x.strip() for x in linesF2]
f2.close()
diffLength = len(linesF1) if len(linesF1) > len(linesF2) else len(linesF2)

if len(linesF1) > len(linesF2):
	add = len(linesF1) - len(linesF2)
	for x in range(0, add):
		linesF2.append(' ')
		
elif len(linesF1) < len(linesF2):
	add = len(linesF2) - len(linesF1)
	for x in range(0, add):
		linesF1.append(' ')

for x in range(0, diffLength):
	difference = False if linesF1[x] == linesF2[x] else True
	type = "" if difference == False else ("+" if len(linesF1[x]) < len(linesF2[x]) else "-") 
	
	diffs.append({
		"firstFile": linesF1[x],
		"secondFile": linesF2[x],
		"difference": difference,
		"type": type
	})
	
for x in range(0, len(diffs)):
	print diffs[x]
	
	
	
	
	
	
	
	
	