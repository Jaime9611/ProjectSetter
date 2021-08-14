"""Cli Commands Script

This script contains the function to make shell calls.

This script has the following:
    * start_git(route) - Function for create a git repo in the given path.
    * start_vscode(route) - Function that starts VSCode in the given path.
    * show_dir_path(route) - Function for obtain the project' path and copied it to the clipboard.
    * get_pwd_path() - Function to obtain the current working directory.
"""

import subprocess
import os
import platform
import pathlib
import logging

LOGGER = logging.getLogger(__name__)


def start_git(route):
    """Function that creates a new git repo in the given path.

    Parameters
    __________
    route : Path Object
        Project's path.
    """

    assert isinstance(route, pathlib.Path), 'Parameter not a Path type.'

    call = subprocess.run(['git', 'init', route])


def start_vscode(route):
    """Function that starts VSCode in the given path.

    Parameters
    __________
    route : Path Object
        Project's path.
    """

    assert isinstance(route, pathlib.Path), 'Parameter not a Path type.'

    call = subprocess.run(['code', route], shell=True)


def show_dir_path(route):
    """Function that copies the project' path to the clipboard.

    Parameters
    __________
    route : Path Object
        Project's path.
    """

    assert isinstance(route, pathlib.Path), 'Parameter not a Path type.'

    result = subprocess.run(['cd', route, '&&', 'pwd'], 
        shell=True, capture_output=True).stdout.decode('utf-8')
    command = 'echo | set /p nul=' + result.strip() + '| clip'
    os.system(command)


def get_pwd_path():
    """Function that obtains the project's location.

    Returns
    __________
    result : String Object
        String with the project's location.
    """

    result = subprocess.run(['cd'], shell=True, capture_output=True).stdout.decode('utf-8')

    if result.startswith('/c/') and platform.system() == 'Windows':
        result = result.replace('/c/', 'C:/')

    assert type(result) == str, 'Not returning a String'

    return result.strip()