import subprocess
import os
import platform
import pathlib
import logging

LOGGER = logging.getLogger(__name__)


def start_git(route):
    assert isinstance(route, pathlib.Path), 'Parameter not a Path type.'

    call = subprocess.run(['git', 'init', route])


def start_vscode(route):
    assert isinstance(route, pathlib.Path), 'Parameter not a Path type.'

    call = subprocess.run(['code', route], shell=True)


def show_dir_path(route):
    assert isinstance(route, pathlib.Path), 'Parameter not a Path type.'

    result = subprocess.run(['cd', route, '&&', 'pwd'], 
        shell=True, capture_output=True).stdout.decode('utf-8')
    command = 'echo | set /p nul=' + result.strip() + '| clip'
    os.system(command)


def get_pwd_path():
    result = subprocess.run(['cd'], shell=True, capture_output=True).stdout.decode('utf-8')

    if result.startswith('/c/') and platform.system() == 'Windows':
        result = result.replace('/c/', 'C:/')

    assert type(result) == str, 'Not returning a String'

    return result.strip()