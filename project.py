# Diff Tool - project.py
# project management
import globalFunc as glb

class Project():
	def __init__(self):
		self.author = ''
		self.name = '' 
		self.description = ''
		self.createDate = ''
		
	def create(self, project):
		# create a project
		self.name = project.name
		self.description = project.description
		self.author = project.author
		self.createDate = glb.getTodaysDateAsString()
		
	def load(self):
		pass
	
	def save(self):
		pass