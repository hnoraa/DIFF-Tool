## Diff Tool
A small tool for comparing file versions

**NOTE: This is for Python 2.7 but will have a Pyhon 3 branch in the future**

## Description
Diff Tool is a tool for comparing 2 different versions of the same file. It produces an .html file as output
this file contains the results of the diff comparison. 

The .gitignore file has been set up to ignore config
files with a naming convention of *.local.json so when testing locally, you can copy config.json to 
config.local.json and use your own directory structure. Also, archive files in the versions directory
have been set to ignore as a privacy measure to potential users/contributers.

## Libraries Used
* os
* time
* json

## Tested on Following OSs
* Windows 10

## Tasks
4/25/2017
*[] adjust theme.json structure to be more conducive for translating to css
*[] implement saving in config.py (write to json file)
*[]

## Updates
<sub><sup>Table Generator: [Markdown Tables Generator](http://www.tablesgenerator.com/markdown_tables)</sup></sub>
| Date      | Contents |
|-----------|----------|
| 4/25/2017 | - Repository created. First implementation of this will be command line only and deal with .txt files only. |
|  | - Configuration JSON structure determined. |

## JSON File Structure
* config.json: holds configuration items for the app
```javascript
{
	"theme": "defaultTheme.json",
	"themeDirectory": "C:\\DiffTool\\Themes",
	"themes": [
		{"name": "defaultTheme", "file": "defaultTheme.json"},
		{"name": "darkTheme", "file": "darkTheme.json"}
	],
	"version": "0.0.1",
	"name": "Diff Tool",
	"description": "A file comparing tool",
	"author": "Aaron Horeth",
	"appDirectory": "C:\\DiffTool",
	"versionDirectory": "C:\\DiffTool\\Versions"
}
```
* theme.json: holds theme (css styles) for the diff .html page output
```javascript
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
```