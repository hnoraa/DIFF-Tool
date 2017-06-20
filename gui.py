# Diff Tool - gui.py
# graphical interface
import os
from Tkinter import *
import tkFileDialog as fd
import tkMessageBox as mb
import globalFunc as gf


class DiffToolWindow(Frame):
	def __init__(self, parent, glbs):
		Frame.__init__(self, parent)
		
		self.g = glbs
		self.htm = None
		self.size = [600, 600]  # size = (width, height)
		
		# labels
		self.projectNameLbl = StringVar()
		self.currentVerLbl = StringVar()
		self.authorLbl = StringVar()
		self.updateLabels('Project:', 'Current Version:', 'Author')
		
		self.fileList = StringVar()
		
		self.parent = parent
		self.parent.title(self.g.configuration.name)
		self.centerWindow()
		self.createMenubar()
		self.createGrid()
		
		self.pack(side='top', fill=BOTH, expand=True)
	
	def updateLabels(self, prj, ver, auth):
		self.projectNameLbl.set(prj)
		self.currentVerLbl.set(ver)
		self.authorLbl.set(auth)
	
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
	
	def createGrid(self):
		# parent grid config
		self.columnconfigure(0, weight=1, pad=5)
		self.columnconfigure(1, weight=1, pad=5)
		for i in range(3):
			self.rowconfigure(i, weight=1)
		
		# project name
		prjName = Label(self, textvariable=self.projectNameLbl)
		prjName.grid(row=0, column=0, sticky=NW, columnspan=2)
		
		# col 1
		col1 = Frame(self)
		col1.grid(row=1, column=0, sticky=NSEW, padx=3, pady=3)
		curVer = Label(col1, textvariable=self.currentVerLbl)
		curVer.grid(row=1, column=0, sticky=NW)
		author = Label(col1, textvariable=self.authorLbl)
		author.grid(row=2, column=0, sticky=NW)
		desc = Label(col1, text='Description:')
		desc.grid(row=3, column=0, sticky=NW)
		self.descriptionTxt = Text(col1, width=35, state=DISABLED)
		self.descriptionTxt.grid(row=4, column=0, sticky=NSEW)
		
		# col 2
		col2 = Frame(self)
		col2.grid(row=1, column=1, sticky=NSEW, padx=3, pady=3)
		files = Label(col2, text='Files in  Project:')
		files.grid(row=0, column=1, sticky=NW)
		self.fileList = Listbox(col2, width=45, height=28)
		self.fileList.grid(row=1, column=1, sticky=NSEW)
		
		# compare button
		compareBtn = Button(self, text='Compare', height=2)
		compareBtn.grid(row=2, column=0, columnspan=2, sticky=NSEW)
	
	def centerWindow(self):
		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()
		x = (sw - self.size[0]) / 2
		y = (sh - self.size[1]) / 2
		self.parent.geometry('%dx%d+%d+%d' % (self.size[0], self.size[1], x, y))
	
	def onProjectOpen(self):
		ftypes = [('JSON Files', '*.json')]
		dlg = fd.Open(self, filetypes=ftypes)
		fl = dlg.show()
		
		if fl != '':
			# read file contents, load project
			prj = os.path.basename(fl)
			prj = os.path.splitext(prj)[0]
			self.g.currentProject.load(prj)
			
			# get file list
			lst = self.g.currentProject.getFilesInArchive()
			
			# set label text
			self.updateLabels('Project: ' + self.g.currentProject.project["name"],
							  'Current Version: ' + str(self.g.currentProject.project["latestVersion"]),
							  'Author: ' + self.g.currentProject.project["author"])
			
			# set text area text
			self.descriptionTxt.config(state=NORMAL)
			self.descriptionTxt.insert(END, self.g.currentProject.project["description"])
			self.descriptionTxt.config(state=DISABLED)
			
			# set list box text
			for l in range(len(lst)):
				self.fileList.insert(END, lst[l])
	
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
