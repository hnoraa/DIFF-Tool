# Diff Tool - cmdLineUi.py
# command line user interface
import project as p


class CmdLineUi:
	def __init__(self, globals):
		self.g = globals
	
	def greet(self):
		print self.g.configuration.about()
	
	def mainMenu(self):
		q = False
		
		while not q:
			print '=' * 80
			print 'Please select from the following options:'
			print ' - [0] Create a Project'
			print ' - [1] Manage Projects'
			print ' - [2] Compare Files [in current project]'
			print ' - [3] Configuration'
			print ' - [4] Help'
			print ' - [5] Quit'
			print '=' * 80
			if self.g.currentProject is not None:
				print 'Current Project: ' + self.g.currentProject['name']
				print '=' * 80
			else:
				print 'There is no project currently selected. Please open/create a project'
				print '    using the menu options above [0 - Create], [1 - Manage].'
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
				self.compareFiles()
			elif choice == '3':
				# configuration
				self.configMenu()
			elif choice == '4':
				# help
				self.helpMenu()
			elif choice == '5':
				# quit
				print 'Exiting ' + self.g.configuration.name
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
	
	def createProjectMenu(self):
		q = False
		
		while not q:
			print 'Create a Project:'
			print '=' * 80
			print 'Please select from the following options:'
			print ' - [0] Create New Project'
			print ' - [1] Back'
			print '=' * 80
			print ''
			choice = raw_input('Selection: ')
			print ''
			
			if choice == '0':
				# create a project
				prj = p.Project()
				
				print 'Creating a new Project...'
				name = raw_input('Project Name: ')
				exists = prj.projectExists(name)
				if exists:
					print 'Project with name: ' + name + ' already exists!'
					q = True
				else:
					author = raw_input('Project Author: ')
					desc = raw_input('Project Description: ')
					f = raw_input('Path to file: ')
			
					try:
						prj.create({'name': name, 'author': author, 'description': desc}, f, self.g)
					except RuntimeError:
						print 'Project: ' + name + ' not created'
						print str(RuntimeError.message)
					finally:
						print 'Project: ' + name + ' successfully created!'
						q = True
			elif choice == '1':
				# go back
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
	
	def openProjectMenu(self):
		q = False
		
		while not q:
			print 'Manage Projects:'
			print '=' * 80
			print 'Please select from the following options:'
			print ' - [0] List Projects'
			print ' - [1] Search Projects'
			print ' - [2] Open Project'
			print ' - [3] Delete Project'
			print ' - [4] Back'
			print '=' * 80
			print ''
			choice = raw_input('Selection: ')
			print ''
			
			if choice == '0':
				# list all projects
				project = p.Project()
				project.listProjects()
			elif choice == '1':
				# search for projects (via wildcard)
				searchString = raw_input('Search for project(s) (*: wildcard): ')
				q = True
			elif choice == '2':
				# open a project
				project = raw_input('Project Name: ')
				prj = p.Project()
				prj.load(project, self.g)
				print prj.project['name'] + ' successfully loaded!'
				
				# return to main menu
				q = True
			elif choice == '3':
				# delete project
				# check to see if project exists
				
				# return to main menu
				q = True
			elif choice == '4':
				# go back
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
	
	def compareFiles(self):
		q = False
		
		if self.g.currentProject is None:
			print 'There is no project currently selected. Please open/create a project'
			print '    using the menu options above [0 - Create], [1 - Open].'
			q = True
		
		while not q:
			print 'Compare files'
			q = True
	
	def configMenu(self):
		q = False
		
		while not q:
			print 'Configuration:'
			print '=' * 80
			print 'Please select from the following options:'
			print ' - [0] List Parameters'
			print ' - [1] Change a Parameter'
			print ' - [2] List Themes'
			print ' - [3] Set Current Theme'
			print ' - [4] Back'
			print '=' * 80
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
				self.g.configuration.updateConfig(key, value)
				print key.title() + ' successfully updated!'
				
				# reload the config file
				self.g.configuration.loadConfig()
				self.displayParams()
			elif choice == '2':
				# display themes
				self.g.configuration.listThemes()
			elif choice == '3':
				# change current theme
				self.g.configuration.listThemes()
				theme = raw_input('Selection: ')
				
				# change the current theme
				self.g.configuration.updateConfig('theme', theme)
				
				# reload the config file
				self.g.configuration.loadConfig()
				self.g.configuration.listThemes()
			elif choice == '4':
				# back
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
	
	def displayParams(self):
		print '=' * 80
		print '         [version] - ' + self.g.configuration.version
		print '     [description] - ' + self.g.configuration.description
		print '          [author] - ' + self.g.configuration.author
		print '    [appDirectory] - ' + self.g.configuration.appDirectory
		print '  [themeDirectory] - ' + self.g.configuration.themeDirectory
		print '[versionDirectory] - ' + self.g.configuration.versionDirectory
		print '=' * 80
		return ''
	
	def helpMenu(self):
		print 'Help:'
		self.g.configuration.about()
