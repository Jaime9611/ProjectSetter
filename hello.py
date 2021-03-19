import json

import click
import folders


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

    with open('./data/project_paths.json') as f:
        MAIN_FOLDER = json.load(f)['webFolder']

    if mode != 'MAIN':
        MAIN_FOLDER += f'{mode}/'

    webproject = folders.WebProject(project_name, MAIN_FOLDER)
    webproject.create_project()
    click.echo(f'Project created succesfull in {webproject.project_path}')


if __name__ == '__main__':
    cli()