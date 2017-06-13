## Diff Tool
A tool for comparing file versions

**NOTE: This is for Python 2.7 but will probably have a Python 3 branch in the future**

## Description
Diff Tool is a tool for comparing 2 different versions of the same file. It produces an .html file as output
this file contains the results of the diff comparison. 

The .gitignore file has been set up to ignore config
files with a naming convention of \*.local.json so when testing locally, you can copy config.json to 
config.local.json and use your own directory structure. Also, archive files in the versions directory
have been set to ignore as a privacy measure to potential users/contributors.

## Updates
| Date        | Contents                                                                                                    |
|-------------|-------------------------------------------------------------------------------------------------------------|
|  06/13/2017 | - Added GUI to project.                                                                                     |
|             | - Clean up configuration file and schema to remove directories and version.                                 |
|             | - Updated display methods in config.py to reflect addition of gui.                                          |
|  06/09/2017 | - Tied together diff code with html generation code.                                                        |
|             | - Fixed default theme css.                                                                                  |
|             | - Allow users to edit project parameters (including name which re-creates the file with the new name).      |
|             | - Cleaned up existing project code.                                                                         |
|             | - Allow users to delete projects.                                                                           |
|             | - Allow users to search via search criteria (string with * as wild cards).                                  |
|  06/08/2017 | - Fixing html layout, working on generating html docs.                                                      |
|             | - Ability to generate html from command line ui.                                                            |
|  06/02/2017 | - Allow users to upload a new version to project.                                                           |
|             | - New versions update the current version number in the project.                                            |
|             | - Fixed project code so global project allows you to use project class methods.                             |
|             | - Tied in diff code to project code.                                                                        |
|             | - Allow users to compare 2 files, results are printed to the screen.                                        |
|  06/01/2017 | - Merged versionControl.py with project.py.                                                                 |
|  05/14/2017 | - Created globals class to hold project, config and theme.                                                  |
|  05/13/2017 | - Added latest version to project schema.                                                                   |
|             | - Updated project logic so latest version can be updated.                                                   |
|  05/10/2017 | - Added versioning logic.                                                                                   |
|  05/09/2017 | - Created zip archives for projects.                                                                        |
|             | - Naming convention for zipped files and zip files contents created.                                        |
|             | - Check to see if project name already exists before creating it.                                           |
|  05/05/2017 | - Create and save projects.                                                                                 |
|             | - Open a project.                                                                                           |
|             | - Project schema.                                                                                           |
|  05/04/2017 | - Basic HTML generation.                                                                                    |
|             | - Basic file comparison.                                                                                    |
|             | - Command Line UI.                                                                                          |
|  04/28/2017 | - Validation for JSON schema created and tested against config and theme.                                   |
|  04/27/2017 | - Created Config JSON schema.                                                                               |
|             | - Created Theme JSON schema.                                                                                |
|  04/26/2017 | - Started work on core functionality.                                                                       |
|  04/25/2017 | - Repository created. First implementation of this will be command line only and deal with .txt files only. |
|             | - Configuration JSON structure determined.                                                                  |
|             | - Added checks for Linux/Windows for cross-platform compatibility.                                          |

## Libraries Used
* os
* time
* json
* sys
* jsonschema
* uuid
* zipfile
* re
* Tkinter

## Tested on Following OSs
* Windows 10
* Ubuntu 16.04.2 LTS

## To Do
* [X] remove directories from config object
* [X] add project name to title in html doc
* [X] lines with just blank space don't show up on html doc
* [X] give html doc the name of the project
* [X] where should html docs go?
* [X] when loading a project in Linux, file name is case sensitive
* [X] ability to delete a project
* [X] search projects based on search string
* [X] make sure file loading and other operations have try catch statements
* [X] if no project is loaded, dont allow user to access compare option
* [X] project info in html diff header div
* [X] merge versionControl.py and project.py
* [X] zip files are to be stored in zip directory
		(currently stored in root directory)
* [X] add latest version number to project schema to keep 
		track of latest version index
* [X] check to see if project already exists when creating a new project 
		(based on project name only)
* [ ] **increase functionality of diff code, it should look to see if 0 or
		more characters are different between each line on each file**
* [X] organize app so common code goes into globalFunc.py
* [X] insure that all config parameters are being used in the app
* [X] global project for app (currently opened project)
* [X] project schema (update config schema)
* [X] projects directory
* [X] projects will be created as json files
* [X] load project
* [X] save project
* [X] come up with UI for command line
* [X] allow user to create a project (means loading a file for the first time)
* [X] allow user to open a project 
		(opening lists all versions of the 'project' aka file)
* [X] project management ability
		(edit, rename, update, add new versions, compare)
* [X] allow user to select 2 versions in the project to compare
* [X] allow user to change config items
* [X] UI validation (in case incorrect data is entered) for command line UI
* [X] compare two files (.txt files in this first version) for addition and/or 
		subtraction only (in this first version 05/04/2017)
* [X] write differences to html file
* [X] generate html
* [X] create "project" to keep file versions contained within
* [X] zip archive of project contains all file versions
* [X] when reading from zip file, determine latest version to compare with 
		currently selected version
* [X] come up with file versioning scheme (i.e. file_v_000_timestamp.txt)
* [X] create JSON schema files for config and theme
* [X] validate against those schemas to ensure app can run correctly
* [X] adjust theme.json structure to be more conducive for translating to css
* [X] implement saving in config.py (write to json file)
* [X] load theme json and create basic css structure
* [X] decide layout for html output file
* [X] Windows/Linux cross platform

## JSON File Structure
* config.json: holds configuration items for the app
```javascript
{
	"theme": "defaultTheme.json",
	"themeDirectory": "C:\\DiffTool\\Themes",
	"themes": [{
			"name": "defaultTheme",
			"file": "defaultTheme.json"
		},
		{
			"name": "darkTheme",
			"file": "darkTheme.json"
		}
	],
	"name": "Diff Tool",
	"description": "A file comparing tool",
	"author": "Aaron Horeth"
}
```
* configSchema.json: the schema for proper config file layout
```javascript
{
	"$schema": "http://json-schema.org/draft-04/schema#",
	"title": "Config",
	"description": "Configuration object",
	"type": "object",
	"properties": {
		"name": {
			"description": "Name of the application",
			"type": "string"
		},
		"author": {
			"description": "Author of the application",
			"type": "string"
		},
		"themes": {
			"type": "array",
			"items": {"$ref": "#/definitions/name", "$ref": "#/definitions/file"},
			"definitions": {
				"name": {
					"type": "string"
				},
				"file": {
					"type": "string"
				}
			}
		},
		"theme": {
			"description": "Default theme",
			"type": "string"
		},
		"description": {
			"description": "Description of the application",
			"type": "string"
		}
	}
}
```
* theme.json: holds theme (css styles) for the diff .html page output
```javascript
{
	"name": "Default Theme",
	"author": "Aaron Horeth",
	"date": "April 25, 2017",
	"description": "This is the default theme, it consists of a dark page background color with a lighter diff region.",
	"body": [
		"body {margin: 0 auto; background-color: #171738;}"
	],
	"main": [
		"#main {position:absolute;top:0;bottom:0;left:0;right:0;padding:10px;}",
		".diff {font-family:\"Lucida Console\",\"Courier New\",monospace; background-color:#efeae6;}"
	],
	"diffHeader": [
		"#diffHeader {position:absolute;top:0;bottom:0;left:0;right:0;padding:10px;}"
	],
	"diffBody": [
		"#diffBody {}",
		"#diffLine {}",
		".diffChange {font-weight: bold;}",
		".diffLineAddition {foreground: #ff6b6b; background-color: #4ecdc4;}",
		".diffLineSubtraction {foreground: #8bb174; background-color: #b6465f;}"
	]
}
```
* themeSchema.json: the schema for proper theme file layout
```javascript
{
	"$schema": "http://json-schema.org/draft-04/schema#",
	"title": "Theme",
	"description": "Theme objects",
	"type": "object",
	"properties": {
		"name": {
			"description": "Name of the theme",
			"type": "string"
		},
		"author": {
			"description": "Author of the theme",
			"type": "string"
		},
		"description": {
			"description": "Description of the theme",
			"type": "string"
		},
		"body": {
			"type": "array"
		},
		"main": {
			"type": "array"
		},
		"diffHeader": {
			"type": "array"
		},
		"diffBody": {
			"type": "array"
		}
	}
}
```
* project.json: the json data for projects
```javascript
{
	"description" : "test",
	"createDate" : "May 05, 2017",
	"name" : "test",
	"author" : "test",
	"guid": "f7a905e3-7c7e-419f-b822-37dc86dd3ecf",
	"latestVersion": 1
}
```
* projectSchema.json: the schema for proper project layout
```javascript
{
	"$schema": "http://json-schema.org/draft-04/schema#",
	"title": "Project",
	"description": "Project objects",
	"type": "object",
	"properties": {
		"name": {
			"description": "Name of the project",
			"type": "string"
		},
		"author": {
			"description": "Author of the project",
			"type": "string"
		},
		"description": {
			"description": "Description of the project",
			"type": "string"
		},
		"createDate": {
			"description": "Date the project was created",
			"type": "string"
		},
		"guid": {
		    "description": "GUID that identifies the project in the version directory",
		    "type": "string"
		},
		"latestVersion": {
			"description": "The latest version of the file",
			"type": "integer"
		}
	}
}
```

Table Generator: [Markdown Tables Generator](http://www.tablesgenerator.com/markdown_tables)

Markdown Editor: [DILLINGER](http://dillinger.io/)

CSS Color Scheme: [coolors](https://coolors.co/efeae6-171738-b6465f-b5ca8d-8bb174)

JSON Validator: [JSONLint](http://jsonlint.com/)
