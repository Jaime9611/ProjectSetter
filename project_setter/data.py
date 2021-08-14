"""Data Script

This script is used to access the .json resources with the path and folder structure data.

This script has the following:
    * PATHS - Variable with the project_paths.json location.
    * STRUCTURES - Variable with the structures.json location.
    * Project - Enum class with the project types' names.
    * _get_data(source, project_type) - Helper function to obtain the json data.
    * get_project_structure(project) - Function that returns the project's layout structure of the given project type(Enum.Project).
    * get_base_path(project) - Function that returns the project's main folder path of the given project type(Enum.Project).
"""

import json
import pkg_resources
from enum import Enum

PATHS = pkg_resources.resource_filename('project_setter', 'resources/project_paths.json')
STRUCTURES = pkg_resources.resource_filename('project_setter', 'resources/structures.json')

# Variables
class Project(Enum):
    """Enum class with the names of the types of projects.
    
    Attributes
    __________
    WEB : String
        Stores the name used for the web's project type.
    PYTHON : String
        Stores the name used for the python's project type.
    """

    WEB = 'web'
    PYTHON = 'python'


def _get_data(source, project_type):
    """Helper method that returns the json data.

    Parameters
    __________
    source : String Object
        Receives the .json file location.
    project_type : Enum.Project Object
        Contains the project's type.

    Returns
    _______
    String or Dict
        String or dictionary containing the data extracted from the .json file.
    """

    with open(source) as f:
        data = json.load(f)

    assert type(data[project_type.value]) == str or type(data[project_type.value]) == dict, 'Function not returning a String or Dict object.'

    return data[project_type.value]


def get_project_structure(project):
    """Function that obtains the project's folder structure.

    This function calls the helper function _get_data().
    """
    assert isinstance(project, Project), 'Argument type not a Project variable.'

    return _get_data(STRUCTURES, project)


def get_base_path(project):
    """Method that returns the project's parent path.

    This function calls the helper function _get_data().
    """

    assert isinstance(project, Project), 'Argument type not a Project variable.'

    return _get_data(PATHS, project)

