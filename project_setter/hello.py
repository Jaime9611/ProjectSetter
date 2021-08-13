"""Main Script

This is the main script in the package. It calls the other modules throught shell commands.

This script has the following functions:
  * cli() - This funcion declares a group of commands.
  * mkweb() - This function represents a shell command to create a WEB project.
  * mkpy() - This function represents a shell command to create a PYTHON project.
"""


import click
from . import folders
from . import cli_commands
from . import data
from .data import Project as project_enums


HELP_P = "Create project in 'PROJECTS' directory."
HELP_T = "Create project in 'PRACTICE' directory."
HELP_R = "Create project in the main directory."
HELP_C = "Create project in the current directory (default)."


@click.group()
def cli():
    """Initial configuration"""
    pass


@cli.command()
@click.option('-p', '--project', 'mode', flag_value='PROJECTS',
    help=HELP_P)
@click.option('-t', '--test', 'mode', flag_value='PRACTICE',
    help=HELP_T)
@click.option('-m', '--main', 'mode', flag_value='MAIN', 
    help=HELP_R)
@click.option('-c', '--current', 'mode', flag_value='CURRENT', 
    default=True, help=HELP_C)
@click.argument('project_name')
def mkweb(project_name, mode):
    """Command to create a Web Project."""

    _make_project(project_name, project_enums.WEB, mode)


@cli.command()
@click.option('-p', '--project', 'mode', flag_value='PROJECTS',
    help=HELP_P)
@click.option('-t', '--test', 'mode', flag_value='PRACTICE',
    help=HELP_T)
@click.option('-o', '--other', 'mode', flag_value='MAIN', 
    help=HELP_R)
@click.option('-c', '--current', 'mode', flag_value='CURRENT', 
    default=True, help=HELP_C)
@click.option('-pkg', '--package','pkg', is_flag=True, default=False)
@click.argument('project_name')
def mkpy(project_name, mode, pkg):
    """Command to create a Python Project."""
    
    _make_project(project_name, project_enums.PYTHON, mode, pkg)


def _make_project(project_name, project_type, mode, pkg=False):
    """Verifies the choosed mode, obtains project type and call the classes corresponding to each project type.
    
    Parameters
    __________
    project_name : String object
        Contains the project's name typed in the shell.
    project_name : Enum.Project object
        Contains the project's type.
    mode : String object
        Contains the choosed mode in the shell.
    pkg : Boolean object
        Boolean that indicates if pkg is part of the function's parameters (used in Project.PYTHON projects).
    """

    if mode == 'CURRENT':
        MAIN_FOLDER = cli_commands.get_pwd_path()
    else:
        MAIN_FOLDER = data.get_base_path(project_type)

        if mode != 'MAIN':
            MAIN_FOLDER += f'{mode}/'


    if project_type == project_enums.WEB:
        project = folders.WebProject(project_name, MAIN_FOLDER)
        existed = project.create_project()
    elif project_type == project_enums.PYTHON:
        project = folders.PyProject(project_name, MAIN_FOLDER)
        existed = project.create_project(pkg)

    _show_message(existed, project.project_path)    



def _show_message(existed, project_path):
    """Shows the message after all the process in ready

    This function also calls the cli_commands' functions for create a git repo and copy the dir path to the clipboard.

    """

    if not existed:
        click.echo(f'Project created succesfull in {project_path}')
        cli_commands.start_git(project_path)
        cli_commands.show_dir_path(project_path)
        # cli_commands.start_vscode(project.project_path)
        click.echo('Project Path copied to clipboard...')
    else:
        click.echo('Project Already Exists.')