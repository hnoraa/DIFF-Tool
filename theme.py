# Diff Tool - theme.py
# defines the theme object
import globalFunc as glb


class Theme:
	def __init__(self, config):
		# only parameter is the full path of the config.json file
		self.themeFile = glb.themesDirectory() + config.theme
		
		if len(self.themeFile) > 0:
			self.clearObject()
			
			self.getJsonString()
			
			if len(self.jsonString) > 0:
				self.loadTheme(True)
			else:
				print 'WARNING: No Theme file has been loaded. Please load a theme.'
		else:
			print 'WARNING: No Theme file has been loaded. Please load a theme.'
	
	def getJsonString(self):
		# returns a json string from self.themeFile
		self.jsonString = ''
		self.jsonString = glb.getJsonString(self.themeFile)
	
	def clearObject(self):
		self.name = ''
		self.date = ''
		self.author = ''
		self.description = ''
		self.body = []
		self.main = []
		self.diffHeader = []
		self.diffBody = []
		self.css = []
	
	def loadTheme(self, firstLoad=False):
		if not firstLoad:
			# refresh json string, in case config has changed
			self.getJsonString()
		
		# populate object
		self.name = self.jsonString["name"]
		self.author = self.jsonString["author"]
		self.date = self.jsonString["date"]
		self.description = self.jsonString["description"]
		self.body = self.jsonString["body"]
		self.main = self.jsonString["main"]
		self.diffHeader = self.jsonString["diffHeader"]
		self.diffBody = self.jsonString["diffBody"]
	
	def createTheme(self):
		self.css.append('<style type="text/css">')
		
		# body css
		for d in self.body:
			self.css.append('\t' + d)
		
		# main content area
		for m in self.main:
			self.css.append('\t' + m)
		
		# diff header area
		for h in self.diffHeader:
			self.css.append('\t' + h)
		
		# diff body area
		for b in self.diffBody:
			self.css.append('\t' + b)
		
		self.css.append('</style>')
	
	def about(self):
		print '=' * 80
		print 'About: ' + self.name
		print 'Created: ' + self.date
		print 'Author: ' + self.author
		print self.description
		print '=' * 80
		return ''
