import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

#Writing code for creating files
#We can simply run this ->  [python template.py] in the terminal and it will execute all and thus create all files with inside the directory

project_name = 'cnnClassifier'

list_of_files = [
    ".github/workflows/.gitkeep",  #Used during Updation, helps us tell if there is no need to update in github at all. Will be removed when we do CICD pipelining and we'll replace this file under the folders with the CICD component
    #Note: All these come under src for easy changing of code and stuff and to keep well organized
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",  #This is for All Google Colab Experiments
    "templates/index.html"   #For Flask web implementation

]

for filepath in list_of_files:
    filepath = Path(filepath)  #We give this to Path class because it will convert all forward slashes to backslashes as only backslashes are recognized by Windows and it will then only recognize it as a filepath
    filedir, filename = os.path.split(filepath)  #For extracting the filename in the end separately

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)  #We're making the directory
        logging.info(f"Creating Directory: {filedir} for the file: {filename}")

    #for making files in the directory
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")
    