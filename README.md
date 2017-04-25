## Diff Tool
A small tool for comparing file versions
**NOTE: This is for Python 2.7 but will have a Pyhon 3 branch in the future**

## Description
Diff Tool is a tool for comparing 2 different versions of the same file. It produces an .html file as output
this file contains the results of the diff comparison.

## Libraries
* os
* time
* json

## Tested on following OSs
* Windows 10

## Updates
4/25/2017 - Repository created. First implementation of this will be command line only and deal with .txt files only.

## JSON file structure
* config.json: holds configuration items for the app
    {
	    "theme": "defaultTheme.json",
	    "themeDirectory": "",
	    "themes": [{
		    "defaultTheme": "defaultTheme.json"
	    }],
		"directory": "",
		"version": "0.0.1",
		"name": "DIFF Tool",
		"author": "Aaron Horeth",
		"scriptDirectory": "C:\\DiffTool",
		"versionDirectory": ""
    }
* theme.json: holds theme (css styles) for the diff .html page output
	{
		"name": "Default Theme",
		"author": "Aaron Horeth",
		"date": "April 25, 2017",
		"description": "This is the default theme, it consists of a dark page background color with a lighter diff region.",
		"page-color": "#171738",
		"body-color": "#efeae6",
		"addition-color": [{
			"foreground": "#ff6b6b"
		}, {
			"background": "#4ecdc4"
		}],
		"subtraction-color": [{
			"foreground": "#8bb174"
		}, {
			"background": "#b6465f"
		}]
	}