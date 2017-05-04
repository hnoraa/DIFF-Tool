# Diff Tool - diff.py
# defines diff structure
class Diff():
	def __init__(self):
		self.fileNames = []
	
	def open(self):
		pass
		
	def compare(self):
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
		