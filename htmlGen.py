# Diff Tool - htmlGen.py
# html generation
import globalFunc as glb


class HtmlGen:
	def __init__(self, theme, info, diffs):
		self.theme = theme
		self.theme.createTheme()
		self.css = self.theme.css
		self.info = info
		self.doc = ''
		self.diffs = diffs
	
	def gen(self):
		# generate HTML file
		self.doc = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<title>Diff Tool</title>\n'
		divEnd = '</div>\n'
		br = '<br />\n'
		
		# css
		for x in self.css:
			self.doc = ''.join([self.doc, x + '\n'])
		self.doc = ''.join([self.doc, '\n'])
		
		self.doc = ''.join([self.doc, '</head>\n<body>\n'])
		self.doc = ''.join([self.doc, '<div id="main" class="diff">\n'])		# main div
		
		self.doc = ''.join([self.doc, '<div id="diffHeader">\n'])  				# diff header
		self.doc = ''.join([self.doc, '<p>' + self.info + '</p>\n'])
		self.doc = ''.join([self.doc, divEnd])  								# end diff header
		
		self.doc = ''.join([self.doc, '<div id="diffContainer">\n'])  			# diff container
		self.doc = ''.join([self.doc, '<div id="diffBody">\n'])  				# diff body
		
		self.doc = ''.join([self.doc, '<div id="col1" class="col">\n'])  		# column 1
		
		for i in range(len(self.diffs)):
			if len(self.diffs[i]["firstFile"]) == 1:
				self.diffs[i]["firstFile"] = br
				
			self.doc = ''.join([self.doc, '<div id="diffLine"'])
				
			if self.diffs[i]["difference"]:
				self.doc = ''.join([self.doc, ' class="diffChange '])
				if self.diffs[i]["type"] == "+":
					self.doc = ''.join([self.doc, ' diffLineAddition">' + self.diffs[i]["firstFile"] + divEnd])
				elif self.diffs[i]["type"] == "-":
					self.doc = ''.join([self.doc, ' diffLineSubtraction">' + self.diffs[i]["firstFile"] + divEnd])
			else:
				self.doc = ''.join([self.doc, '>' + self.diffs[i]["firstFile"] + divEnd])
		
		self.doc = ''.join([self.doc, divEnd])  								# end column 1
		
		self.doc = ''.join([self.doc, '<div id="col2" class="col">\n'])  		# column 2
		
		for i in range(len(self.diffs)):
			if len(self.diffs[i]["secondFile"]) == 1:
				self.diffs[i]["secondFile"] = br
				
			self.doc = ''.join([self.doc, '<div id="diffLine"'])
			if self.diffs[i]["difference"]:
				self.doc = ''.join([self.doc, ' class="diffChange '])
				if self.diffs[i]["type"] == "+":
					self.doc = ''.join([self.doc, ' diffLineAddition">' + self.diffs[i]["secondFile"] + divEnd])
				elif self.diffs[i]["type"] == "-":
					self.doc = ''.join([self.doc, ' diffLineSubtraction">' + self.diffs[i]["secondFile"] + divEnd])
			else:
				self.doc = ''.join([self.doc, '>' + self.diffs[i]["secondFile"] + divEnd])
			
		self.doc = ''.join([self.doc, divEnd])  								# end column 2
		
		self.doc = ''.join([self.doc, divEnd])  								# end diff body
		self.doc = ''.join([self.doc, divEnd])  								# end diff container
		self.doc = ''.join([self.doc, divEnd])  								# end main div
		self.doc = ''.join([self.doc, '</body>\n</html>'])
	
	def save(self):
		# save HTML file
		f = open("test.html", "w")
		f.write(self.doc)
		f.close()
