# Diff Tool - cmdLineUi.py
# command line user interface
import globalFunc as glb
class CmdLineUi():
	def __init__(self, conf):
		self.conf = conf
		
	def greet(self):
		print 'test'
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
			choice = raw_input("Selection: ")
			
			if choice == '0':
				self.createProjectMenu()
			elif choice == '1':
				self.openProjectMenu()
			elif choice == '2':
				self.configMenu()
			elif choice == '3':
				self.helpMenu()
			elif choice == '4':
				print 'Exiting ' + self.conf.name
				q = True
			else:
				print 'Invalid choice, please retry'
		glb.quit()
		
	def createProjectMenu(self):
		q = False
		
		while(not q):
			print '='*80
			print 'Create a Project:'
			print 'Please select from the following options:'
			print ' - [0] Back'
			print '='*80
			choice = raw_input("Selection: ")
			
			if choice == '0':
				q = True
			else:
				print 'Invalid choice, please retry'
		
	def openProjectMenu(self):
		q = False
		
		while(not q):
			print '='*80
			print 'Open a Project:'
			print 'Please select from the following options:'
			print ' - [0] Back'
			print '='*80
			choice = raw_input("Selection: ")
			
			if choice == '0':
				q = True
			else:
				print 'Invalid choice, please retry'
	
	def configMenu(self):
		q = False
		
		while(not q):
			print '='*80
			print 'Configuration:'
			print 'Please select from the following options:'
			print ' - [0] List Parameters'
			print ' - [1] Change a Parameter'
			print ' - [2] List Themes'
			print ' - [3] Set Current Theme'
			print ' - [4] Back'
			print '='*80
			choice = raw_input("Selection: ")
			
			if choice == '0':
				self.displayParams()
			elif choice == '1':
				self.displayParams()
				
				# make a change to a parameter
				key = raw_input("Parameter: ")
				value = raw_input("New Value: ")
				self.conf.updateConfig(key, value)
				
				# reload the config file
				self.conf.loadConfig()
				
				self.displayParams()
			elif choice == '2':
				self.conf.listThemes()
			elif choice == '3':
				self.conf.listThemes()
				theme = raw_input("Selection: ")
				
				# change the current theme
				self.conf.updateConfig("theme", theme)
				
				# reload the config file
				self.conf.loadConfig()
				
				self.conf.listThemes()
			elif choice == '4':
				q = True
			else:
				print 'Invalid choice, please retry'
	
	def displayParams(self):
		print '='*80
		print '          [author] - ' + self.conf.author
		print '         [version] - ' + self.conf.version
		print '     [description] - ' + self.conf.description
		print '    [appDirectory] - ' + self.conf.appDirectory
		print '  [themeDirectory] - ' + self.conf.themeDirectory
		print '[versionDirectory] - ' + self.conf.versionDirectory
		print self.conf.theme
		print '='*80
		print ''
	
	def helpMenu(self):
		self.conf.about()