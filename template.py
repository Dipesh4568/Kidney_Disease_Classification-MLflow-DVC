import os
from pathlib import Path
import logging 

#logging string 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'cnnClassifier'

#List of files to create in project
list_of_files = [
    ".github/workflow/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    'config/config.yml',
    'dvc.yml',
    'param.yml',
    'requirements.txt',
    'setup.py',
    'research/trails.ipynb',
    'templates/index.html'
]


# create file and folder one by one
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Logic to create directory
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
    
    #Logic to create file inside drectory if not present
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file: {filepath}')

    #Message for completion
    else:
        logging.info(f'{filename} is already exists')