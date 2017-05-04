# Diff Tool - htmlGen.py
# html generation
class HtmlGen():
	def __init__(self, theme, info):
		self.theme = theme
		self.theme.createTheme()
		self.css = self.theme.css
		self.info = info
		self.doc = ''
		
	def gen(self):
		# generate HTML file
		self.doc = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<title>Diff Tool</title>\n'
		for x in self.css:
			self.doc = ''.join([self.doc, x])
		self.doc = ''.join([self.doc, '</head>\n<body>\n', '</body>\n</html>'])
		
	def save(self):
		# save HTML file
		f = open("test.html", "w")
		f.write(self.doc)
		f.close()