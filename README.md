## Diff Tool
A small tool for comparing file versions

**NOTE: This is for Python 2.7 but will have a Pyhon 3 branch in the future**

## Description
Diff Tool is a tool for comparing 2 different versions of the same file. It produces an .html file as output
this file contains the results of the diff comparison. 

The .gitignore file has been set up to ignore config
files with a naming convention of \*.local.json so when testing locally, you can copy config.json to 
config.local.json and use your own directory structure. Also, archive files in the versions directory
have been set to ignore as a privacy measure to potential users/contributers.

## Libraries Used
* os
* time
* json
* sys
* jsonschema

## Tested on Following OSs
* Windows 10
* Ubuntu 16.04.2 LTS

## Tasks (Date Indicates Date Task Came To Mind)
4/28/2017
* [ ] generate html
* [ ] possibly load html from a file to generate it and mix with css

4/27/2017
* [ ] create "project" to keep file versions contained within
* [ ] zip archive of project contains all file versions
* [ ] when reading from zip file, determine latest version to compare with currently selected version
* [ ] come up with file versioning scheme (i.e. file_v_000_timestamp.txt)

4/26/2017
* [X] create JSON schema files for config and theme
* [X] validate against those schemas to ensure app can run correctly

4/25/2017
* [X] adjust theme.json structure to be more conducive for translating to css
* [X] implement saving in config.py (write to json file)
* [X] load theme json and create basic css structure
* [X] decide layout for html output file
* [X] Windows/Linux cross platform

## Updates
| Date       | Contents                                                                                                    |
|------------|-------------------------------------------------------------------------------------------------------------|
|  4/28/2017 | - Validation for JSON schema created and tested against config and theme.                                   |
|  4/27/2017 | - Created Config JSON schema.                                                                               |
|            | - Created Theme JSON schema.                                                                                |
|  4/26/2017 | - Started work on core functionality.                                                                       |
|  4/25/2017 | - Repository created. First implementation of this will be command line only and deal with .txt files only. |
|            | - Configuration JSON structure determined.                                                                  |
|            | - Added checks for Linux/Windows for cross-platform compatibility.                                          |

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
		"appDirectory": {
			"description": "Main directory of the application",
			"type": "string"
		},
		"versionDirectory": {
			"description": "Version directory for the application",
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
		"version": {
			"description": "Version of the application",
			"type": "string"
		},
		"themeDirectory": {
			"description": "Theme directory for the application",
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

Table Generator: [Markdown Tables Generator](http://www.tablesgenerator.com/markdown_tables)

Markdown Editor: [DILLINGER](http://dillinger.io/)

CSS Color Scheme: [coolors](https://coolors.co/efeae6-171738-b6465f-b5ca8d-8bb174)

JSON Validator: [JSONLint](http://jsonlint.com/)
