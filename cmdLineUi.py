# Diff Tool - cmdLineUi.py
# command line user interface
import globalFunc as glb
import project as p

class CmdLineUi():
	def __init__(self, conf):
		self.conf = conf
		
	def greet(self):
		print self.conf.about()
		
	def mainMenu(self):
		q = False
		
		while(not q):
			print '='*80
			print 'Please select from the following options:'
			print ' - [0] Create a Project'
			print ' - [1] Open a Project'
			print ' - [2] Configuration'
			print ' - [3] Help'
			print ' - [4] Quit'
			print '='*80
			print ''
			choice = raw_input('Selection: ')
			print ''
			
			if choice == '0':
				# create a new project
				self.createProjectMenu()
			elif choice == '1':
				# open a project
				self.openProjectMenu()
			elif choice == '2':
				# configuration
				self.configMenu()
			elif choice == '3':
				# help
				self.helpMenu()
			elif choice == '4':
				# quit
				print 'Exiting ' + self.conf.name
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
		glb.quit()
		
	def createProjectMenu(self):
		q = False
		
		while(not q):
			print 'Create a Project:'
			print '='*80
			print 'Please select from the following options:'
			print ' - [0] Create New Project'
			print ' - [1] Back'
			print '='*80
			print ''
			choice = raw_input('Selection: ')
			print ''
			
			if choice == '0':
				name = raw_input('Project Name: ')
				author = raw_input('Project Author: ')
				desc = raw_input('Project Description: ')
				prj = p.Project()
				prj.create({'name': name, 'author': author, 'description': desc})
				prj.save()
			elif choice == '1':
				# go back
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
		
	def openProjectMenu(self):
		q = False
		
		while(not q):
			print 'Open a Project:'
			print '='*80
			print 'Please select from the following options:'
			print ' - [0] List Projects'
			print ' - [1] Select Project'
			print ' - [2] Back'
			print '='*80
			print ''
			choice = raw_input('Selection: ')
			print ''
			
			if choice == '0':
				project = p.Project()
				project.listProjects()
			elif choice == '1':
				# open a project
				project = raw_input('Project Name: ')
				prj = p.Project()
				prj.load(project)
				print prj.project
			elif choice == '2':
				# go back
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
	
	def configMenu(self):
		q = False
		
		while(not q):
			print 'Configuration:'
			print '='*80
			print 'Please select from the following options:'
			print ' - [0] List Parameters'
			print ' - [1] Change a Parameter'
			print ' - [2] List Themes'
			print ' - [3] Set Current Theme'
			print ' - [4] Back'
			print '='*80
			print ''
			choice = raw_input('Selection: ')
			print ''
			
			if choice == '0':
				# display parameters
				self.displayParams()
			elif choice == '1':
				# change a parameter
				self.displayParams()
				
				# make a change to a parameter
				key = raw_input('Parameter: ')
				value = raw_input('New Value: ')
				self.conf.updateConfig(key, value)
				
				# reload the config file
				self.conf.loadConfig()
				
				self.displayParams()
			elif choice == '2':
				# display themes
				self.conf.listThemes()
			elif choice == '3':
				# change current theme
				self.conf.listThemes()
				theme = raw_input('Selection: ')
				
				# change the current theme
				self.conf.updateConfig('theme', theme)
				
				# reload the config file
				self.conf.loadConfig()
				
				self.conf.listThemes()
			elif choice == '4':
				# back
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
	
	def displayParams(self):
		print '='*80
		print '          [author] - ' + self.conf.author
		print '         [version] - ' + self.conf.version
		print '     [description] - ' + self.conf.description
		print '    [appDirectory] - ' + self.conf.appDirectory
		print '  [themeDirectory] - ' + self.conf.themeDirectory
		print '[versionDirectory] - ' + self.conf.versionDirectory
		print '='*80
		return ''
	
	def helpMenu(self):
		print 'Help:'
		self.conf.about()