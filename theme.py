# Diff Tool - theme.py
# defines the theme object
import globalFunc as glb

class Theme():
	def __init__(self, config):
		# only parameter is the full path of the config.json file
		self.themeFile = glb.cwd() + config.theme
		
		if len(self.themeFile) > 0:
			self.clearObject()
			
			self.getJsonString()
			
			if len(self.jsonString) > 0:
				self.loadTheme(True)
			else:
				print 'WARNING: No Theme file has been loaded. Please load one for theme to continue.'
		else:
			print 'WARNING: No Theme file has been loaded. Please load one for theme to continue.'
			
	def getJsonString(self):
		# returns a json string from self.themeFile
		self.jsonString = ''
		self.jsonString = glb.getJsonString(self.themeFile)	
		
	def clearObject(self):
		self.name = ''
		self.date = ''
		self.author = ''
		self.description = ''
		self.pageColor = ''
		self.bodyColor = ''
		self.additionStyle = {}
		self.subtractionStyle = {}
			
	def loadTheme(self, firstLoad=False):		
		if firstLoad == False:
			# refresh json string, in case config has changed
			self.getJsonString()
		
		# populate object
		self.name = self.jsonString["name"]
		self.author = self.jsonString["author"]
		self.date = self.jsonString["date"]
		self.description = self.jsonString["description"]
		self.pageColor = self.jsonString["page-color"]
		self.bodyColor = self.jsonString["body-color"]
		self.additionStyle = self.jsonString["addition-color"]
		self.subtractionStyle = self.jsonString["subtraction-color"]
		
	def createTheme(self):
		pass
		
	def about(self):
		print '============================================================'
		print 'About:'
		print self.name
		print 'Created: ' + self.date
		print 'Author: ' + self.author
		print self.description
		print '============================================================'
