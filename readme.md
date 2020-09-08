# Automatic file sorter

## Problem this script will solve
Were you on a situation when you have hundreds of files in a folder and you are on hard time finding your necessery files. It would have been very convenient if all the files were organized nicely by file types. Doing this manually would require huge amount of time and effort. So, this script will do that exact thing for you just by running the script in blink of eye.


## Technology used
* Regular expression
* shutil


## How to use

### Windows
You need to install python if not allready installed
* Place the file_sorter.py in the folder which you want to organize
* Double click on the file

### MacOS and linux
* Place the file_sorter.py in the folder which you want to organize
* Open terminal from the folder
* run `python3 file_sorter.py`

## Customizing
Add folder_name and and associated file extensions in bellow format in the config.json

```{
	"folder_name_1": ["extension1", "extension2"],
	"folder_name_2": ["extension1", "extension2"],
	"folder_name_3": ["extension1", "extension2"],
	"folder_name_4": ["extension1", "extension2"]
}```

N.B: Each entry must be seperated by comma


## Features to be added
* GUI for easily running
