# Diff Tool - gui.py
# graphical interface
from Tkinter import *
import tkFileDialog as fd
import tkMessageBox as mb


class DiffToolWindow(Frame):
	def __init__(self, parent, glbs):
		Frame.__init__(self, parent)
		
		self.g = glbs
		self.htm = None
		
		self.w = 800
		self.h = 600
		
		self.parent = parent
		self.parent.title(self.g.configuration.name)
		self.pack(fill=BOTH, expand=1)
		self.centerWindow()
		self.createMenubar()

	def createMenubar(self):
		menubar = Menu(self.parent)
		self.parent.config(menu=menubar)
		
		fileMenu = Menu(menubar)
		fileMenu.add_command(label='Open Project', command=self.onProjectOpen)
		fileMenu.add_command(label='Save Project', command=self.onProjectSave)
		fileMenu.add_command(label='Exit', command=self.quit)
		
		helpMenu = Menu(menubar)
		helpMenu.add_command(label='About', command=self.onAbout)
		
		configMenu = Menu(menubar)
		configMenu.add_command(label='Parameters', command=self.onConfigShowParams)
		
		menubar.add_cascade(label='File', menu=fileMenu)
		menubar.add_cascade(label='Configuration', menu=configMenu)
		menubar.add_cascade(label='Help', menu=helpMenu)

	def centerWindow(self):
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - self.w) / 2
		y = (sh - self.h) / 2
		self.parent.geometry('%dx%d+%d+%d' % (self.w, self.h, x, y))

	def onProjectOpen(self):
		ftypes = [('JSON Files', '*.json')]
		dlg = fd.Open(self, filetypes=ftypes)
		fl = dlg.show()
		
		if fl != '':
			text = self.g.readFile(fl)

	def onProjectSave(self):
		pass

	def onAbout(self):
		about = self.g.configuration.about(gui=True)
		mb.showinfo('About ' + self.g.configuration.name, about)
		
	def onConfigShowParams(self):
		text = 'Author: ' + self.g.configuration.author + '\n'
		text = ''.join([text, 'Description:\n' + self.g.configuration.description])
		text = ''.join([text, '\n' + self.g.configuration.listThemes(gui=True)])
		mb.showinfo('Configuration Parameters', text)