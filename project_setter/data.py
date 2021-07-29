import json
import pkg_resources

PATHS = pkg_resources.resource_filename('project_setter', 'resources/project_paths.json')
STRUCTURES = pkg_resources.resource_filename('project_setter', 'resources/structures.json')

# Variables
WEB = 'web'
PYTHON = 'python'


def _get_data(source, project_type):
    
    with open(source) as f:
        data = json.load(f)

    return data[project_type]


def get_project_structure(project):

    return _get_data(STRUCTURES, project)


def get_base_path(project):

    return _get_data(PATHS, project)

