import subprocess
import os
import platform


def start_git(route):
    call = subprocess.run(['git', 'init', route])


def start_vscode(route):
    call = subprocess.run(['code', route], shell=True)


def show_dir_path(route):
    result = subprocess.run(['cd', route, '&&', 'pwd'], 
        shell=True, capture_output=True).stdout.decode('utf-8')
    command = 'echo | set /p nul=' + result.strip() + '| clip'
    os.system(command)


def get_pwd_path():
    result = subprocess.run(['pwd'], 
        shell=True, capture_output=True).stdout.decode('utf-8')

    if result.startswith('/c/') and platform.system() == 'Windows':
        result = result.replace('/c/', 'C:/')

    return result.strip()