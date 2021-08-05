import json
import pkg_resources
from enum import Enum

PATHS = pkg_resources.resource_filename('project_setter', 'resources/project_paths.json')
STRUCTURES = pkg_resources.resource_filename('project_setter', 'resources/structures.json')

# Variables
class Project(Enum):
    WEB = 'web'
    PYTHON = 'python'


def _get_data(source, project_type):

    with open(source) as f:
        data = json.load(f)

    assert type(data[project_type.value]) == str or type(data[project_type.value]) == dict, 'Function not returning a String or Dict object.'

    return data[project_type.value]


def get_project_structure(project):
    assert isinstance(project, Project), 'Argument type not a Project variable.'

    return _get_data(STRUCTURES, project)


def get_base_path(project):
    assert isinstance(project, Project), 'Argument type not a Project variable.'

    return _get_data(PATHS, project)

