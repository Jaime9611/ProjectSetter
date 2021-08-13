"""Main Script

Este es el script principal en el paquete, pues manda a llamar a los demas modulos, a traves de comandos en el shell.

Este script contiene las siguientes funciones:
  * cli - Esta función declara un grupo de comandos click.
  * mkweb - Esta función representa un comando del shell para crear un proyecto WEB.
  * mkpy - Esta función representa un comando del shell para crear un proyecto PYTHON.
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
    """Verifica el modo de escogido para el proyecto, obtiene su root path y y llama a los metodos encargados de crear el tipo de proyecto
    
    Parameters
    __________
    project_name : String object
        Contiene el nombre del proyecto escrito en el shell.
    project_name : Enum.Project object
        Contiene el tipo de proyecto que se desea crear.
    mode : String object
        Contiene el modo escogido en el shell por los flags.
    pkg : Boolean object
        Booleano para indicar si el pkg hace parte de los parametros (usado para projectos de tipo Project.PYTHON).
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
    if not existed:
        click.echo(f'Project created succesfull in {project_path}')
        cli_commands.start_git(project_path)
        cli_commands.show_dir_path(project_path)
        # cli_commands.start_vscode(project.project_path)
        click.echo('Project Path copied to clipboard...')
    else:
        click.echo('Project Already Exists.')