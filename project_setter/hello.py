import click
from . import folders
from . import cli_commands
from . import data
from .data import Project as project_type


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

    if mode == 'CURRENT':
        MAIN_FOLDER = cli_commands.get_pwd_path()
    else:
        MAIN_FOLDER = data.get_base_path(project_type.WEB)

        if mode != 'MAIN':
            MAIN_FOLDER += f'{mode}/'

    webproject = folders.WebProject(project_name, MAIN_FOLDER)

    successful = webproject.create_project()
    if successful:
        click.echo(f'Project created succesfull in {webproject.project_path}')
        cli_commands.start_git(webproject.project_path)
        cli_commands.show_dir_path(webproject.project_path)
        # cli_commands.start_vscode(webproject.project_path)
        click.echo('Project Path copied to clipboard...')
    else:
        click.echo('Project Already Exists.')



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

    if mode == 'CURRENT':
        MAIN_FOLDER = cli_commands.get_pwd_path()
    else:
        MAIN_FOLDER = data.get_base_path(project_type.PYTHON)

        if mode != 'MAIN':
            MAIN_FOLDER += f'{mode}/'

    pyproject = folders.PyProject(project_name, MAIN_FOLDER)

    existed = pyproject.create_project(pkg)
    if not existed:
        click.echo(f'Project created succesfull in {pyproject.project_path}')
        cli_commands.start_git(pyproject.project_path)
        cli_commands.show_dir_path(pyproject.project_path)
        # cli_commands.start_vscode(pyproject.project_path)
        click.echo('Project Path copied to clipboard...')
    else:
        click.echo('Project Already Exists.')
