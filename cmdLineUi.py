# Diff Tool - cmdLineUi.py
# command line user interface
import htmlGen as h


class CmdLineUi:
	def __init__(self, glbs):
		self.g = glbs
		self.htm = None
	
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
			if len(self.g.currentProject.project['name']) > 0:
				print 'Current Project: ' + self.g.currentProject.project['name']
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
				print 'Creating a new Project...'
				name = raw_input('Project Name: ')
				exists = self.g.currentProject.projectExists(name)
				
				if exists:
					print 'Project with name: ' + name + ' already exists!'
					q = True
				else:
					author = raw_input('Project Author: ')
					desc = raw_input('Project Description: ')
					f = raw_input('Path to file: ')
			
					try:
						self.g.currentProject.create({'name': name, 'author': author, 'description': desc}, f)
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
			print ' - [4] Edit Current Project Information'
			print ' - [5] Back'
			print '=' * 80
			print ''
			choice = raw_input('Selection: ')
			print ''
			
			if choice == '0':
				# list all projects
				self.g.currentProject.listProjects()
			elif choice == '1':
				# search for projects (via wildcard)
				searchString = raw_input('Search for project(s) (*: wildcard): ')
				q = True
			elif choice == '2':
				# open a project
				project = raw_input('Project Name: ')
				self.g.currentProject.load(project)
				print self.g.currentProject.project['name'] + ' successfully loaded!'
				
				# return to main menu
				q = True
			elif choice == '3':
				# delete project
				# check to see if project exists
				if self.g.currentProject is None or len(self.g.currentProject.project['name']) < 1:
					print 'There is no project currently selected. Please open/create a project'
					print '    using the menu options above [0 - Create], [1 - Open].'
					q = True
				else:
					# return to main menu
					print 'Project successfully deleted!'
					q = True
			elif choice == '4':
				# edit project parameters
				if self.g.currentProject is None or len(self.g.currentProject.project['name']) < 1:
					print 'There is no project currently selected. Please open/create a project'
					print '    using the menu options above [0 - Create], [1 - Open].'
					q = True
				else:
					# change a parameter
					self.displayProjectParams()
					
					# make a change to a parameter
					key = raw_input('Parameter: ')
					value = raw_input('New Value: ')
					self.g.currentProject.editProject(key, value)
					print key.title() + ' successfully updated!'
					
					# reload the config file
					self.displayProjectParams()
			elif choice == '5':
				# go back
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
		
	def compareFiles(self):
		q = False
		
		if self.g.currentProject is None or len(self.g.currentProject.project['name']) < 1:
			print 'There is no project currently selected. Please open/create a project'
			print '    using the menu options above [0 - Create], [1 - Open].'
			q = True
		
		while not q:
			print '=' * 80
			print 'Please select from the following options:'
			print ' - [0] Compare Versions'
			print ' - [1] Upload New Version'
			print ' - [2] Back'
			print '=' * 80
			print 'Current Project: ' + self.g.currentProject.project['name']
			print '=' * 80
			print ''
			choice = raw_input('Selection: ')
			print ''
			
			if choice == '0':
				# compare versions
				self.compareVersions()
			elif choice == '1':
				# add version to project
				self.uploadVersion()
			elif choice == '2':
				# go back
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
	
	def compareVersions(self):
		# compare 2 versions
		q = False
		
		if self.g.currentProject is None or len(self.g.currentProject.project['name']) < 1:
			print 'There is no project currently selected. Please open/create a project'
			print '    using the menu options above [0 - Create], [1 - Open].'
			q = True
		
		lst = self.g.currentProject.getFilesInArchive()
		vr = self.g.currentProject.listVersions()
		
		while not q:
			print 'Compare Versions: '
			print '=' * 80
			print 'Documents in Project: '
			for l in range(len(lst)):
				print '[' + str(vr[l]) + '] ' + lst[l]
			print ''
			print 'Select 2 Versions to Compare (ex: 1,2)'
			print '=' * 80
			print ''
			choice = raw_input('Selection: ')
			print ''
			vers = map(int, choice.split(','))
			
			if set(vers).issubset(vr):
				if len(vers) > 2 or len(vers) <= 1:
					print 'You can only compare 2 versions at a time.'
				
				print 'comparing...'
				# get files
				files = [lst[vers[0]-1], lst[vers[1]-1]]
				self.g.currentProject.compareFiles(files)
				
				info = 'Project: ' + self.g.currentProject.project["name"] + '<br /> Comparing Versions: [' + str(vers[0]) + '] and [' + str(vers[1]) + ']<br />'
				self.htm = h.HtmlGen(self.g.theme, info, self.g.currentProject.currentDiff)
				self.htm.gen()
				self.htm.save()
				
				print 'HTML doc created...'
				q = True
			else:
				print choice + ' is not correct'
				q = True
	
	def uploadVersion(self):
		# upload a new version
		q = False
		
		while not q:
			print 'Upload to Project:'
			print '=' * 80
			print 'Please select from the following options:'
			print ' - [0] Upload a New Version'
			print ' - [1] Back'
			print '=' * 80
			print ''
			choice = raw_input('Selection: ')
			print ''
			
			if choice == '0':
				print 'Uploading a New Version...'
				
				f = raw_input('Path to file: ')
				try:
					self.g.currentProject.versionDocument(f)
				except RuntimeError:
					print 'File: ' + f + ' not uploaded to project ' + self.g.currentProject.project['name']
					print str(RuntimeError.message)
				finally:
					print 'File: ' + f + ' successfully uploaded to project ' + self.g.currentProject.project['name'] + '!'
					q = True
			elif choice == '1':
				# go back
				q = True
			else:
				# invalid choice
				print 'Invalid choice, please retry'
	
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
	
	def displayProjectParams(self):
		print '=' * 80
		print '            [name] - ' + self.g.currentProject.project["name"]
		print '          [author] - ' + self.g.currentProject.project["author"]
		print '     [description] - ' + self.g.currentProject.project["description"]
		print '=' * 80
		return ''
	
	def helpMenu(self):
		print 'Help:'
		self.g.configuration.about()
