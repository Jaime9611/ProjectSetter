import click
from . import folders
from . import cli_commands
from . import data


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

    MAIN_FOLDER = data.get_base_path(data.WEB)

    if mode != 'MAIN':
        MAIN_FOLDER += f'{mode}/'
    
    webproject = folders.WebProject(project_name, MAIN_FOLDER)

    webproject.create_project()
    click.echo(f'Project created succesfull in {webproject.project_path}')
    cli_commands.start_git(webproject.project_path)
    cli_commands.show_dir_path(webproject.project_path)
    # cli_commands.start_vscode(webproject.project_path)

    click.echo('Project Path copied to clipboard...')


@cli.command()
@click.option('-p', '--project', 'mode', flag_value='PROJECTS',
    help=HELP_P)
@click.option('-t', '--test', 'mode', flag_value='PRACTICE',
    help=HELP_T)
@click.option('-o', '--other', 'mode', flag_value='MAIN', 
    default=True, help=HELP_R)
@click.option('-pkg', '--pkg', is_flag=True, default=False)
@click.argument('project_name')
def mkpy(project_name, mode, pkg):
    """Command to create a Python Project."""

    MAIN_FOLDER = data.get_base_path(data.PYTHON)

    if mode != 'MAIN':
        MAIN_FOLDER += f'{mode}/'

    pyproject = folders.PyProject(project_name, MAIN_FOLDER)

    pyproject.create_project(pkg)
    click.echo(f'Project created succesfull in {pyproject.project_path}')
    cli_commands.start_git(pyproject.project_path)
    cli_commands.show_dir_path(pyproject.project_path)
    # cli_commands.start_vscode(pyproject.project_path)

    click.echo('Project Path copied to clipboard...')
