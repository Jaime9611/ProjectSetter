import json
import pkg_resources

import click
from . import folders
from . import cli_commands


HELP_P = "Create project in 'PROJECTS' directory."
HELP_T = "Create project in 'PRACTICE' directory."
HELP_R = "Create project in the main directory (default)."


@click.group()
def cli():
    """Initial configuration"""
    pass


@cli.command()
@click.option('-p', '--project', 'mode', flag_value='PROJECTS',
    help=HELP_P)
@click.option('-t', '--test', 'mode', flag_value='PRACTICE',
    help=HELP_T)
@click.option('-o', '--other', 'mode', flag_value='MAIN', 
    default=True, help=HELP_R)
@click.argument('project_name')
def mkweb(project_name, mode):
    """Command to create a Web Project."""

    file_path = pkg_resources.resource_filename('project_setter', 'resources/project_paths.json')
    with open(file_path) as f:
        MAIN_FOLDER = json.load(f)['webFolder']

    if mode != 'MAIN':
        MAIN_FOLDER += f'{mode}/'

    webproject = folders.WebProject(project_name, MAIN_FOLDER)
    webproject.create_project()
    click.echo(f'Project created succesfull in {webproject.project_path}')
    cli_commands.start_git(webproject.project_path)
    cli_commands.show_dir_path(webproject.project_path)
    # cli_commands.start_vscode(webproject.project_path)