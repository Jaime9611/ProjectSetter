import subprocess
import os


def start_git(route):
    call = subprocess.run(['git', 'init', route])
    while True:
        try:
            call.check_returncode()
            break
        except subprocess.CalledProcessError:
            print('process failed')
            break


def start_vscode(route):
    print(route)
    call = subprocess.run(['code', route], shell=True)
    while True:
        try:
            call.check_returncode()
            break
        except subprocess.CalledProcessError:
            print('process failed')
            break

def show_dir_path(route):
    subprocess.run(['cd', route, '&&', 'pwd'], shell=True)


if __name__ == '__main__':
    start_git()