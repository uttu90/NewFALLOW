import os
import json
from FALLOW import config


def get_projects(file_name='projects.json'):
    file_name = os.path.join(config.path, file_name)
    if not os.path.isfile(file_name):
        return {}
    else:
        with open(file_name, 'r') as project_file:
            return json.load(project_file)


def put_projects(projects, file_name='projects.json'):
    file_name = os.path.join(config.path, file_name)
    with open(file_name, 'w') as project_file:
        json.dump(projects, project_file)
