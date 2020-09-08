import os
import shutil
import json
import re


# Default configurations
default = {
    "Images": ["jpg", "jpeg", "png", "webp", "gif"],
    "Videos": ["mp4"],
    "Music": ["mp3", "ogg"],
    "Pdfs": ["pdf"],
    "Documents": ["docx", "doc", "xlsx", "xls", "pptx", "ppt", "odt"],
    "Softwares": ["msi", "exe", "deb"],
    "Compressed": ["zip", "rar", "7z", "tar.xz"],
    "Vectors": ["svg", "eps"],
    "Illustrator": ["ai"],
    "Photoshop": ["ps"],
    "C": ["c"]
}


# Read the config file if exists otherwise use default config
try:
    with open('config.json') as file:
        config = json.loads(file.read())
except:
    config = default
    with open('config.json', 'w') as file:
        json.dump(config, file)

# Get the file extension
extension_re = re.compile(r'\.([a-zA-Z0-9]{1,8})$')
def get_extension(file):
    if extension_re.search(file):
        return extension_re.search(file).group(1)
    return None


# Check if directory exists and make directory if doesn't
def check_dir(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)


# Move the file to its relevant directory
def move_file(file):
    extension = get_extension(file)
    for dir in config:
        if extension in config[dir]:
            check_dir(dir)
            shutil.move(file, dir)
            return
    check_dir('Others')
    shutil.move(file, "Others")


# Get all the files in the directory
def main():
    for object in os.listdir():
        if os.path.isfile(object):
            if object != 'file_sorter.py' and object != 'config.json':
                move_file(object)
            

main()
