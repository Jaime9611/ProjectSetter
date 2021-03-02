import click

import folder


HELP_GIT = "Create or not a git repository."


@click.group()
def cli():
    """Initial configuration"""
    click.echo('Requirements')


@cli.command()
@click.argument('project_name')
@click.option('--git', '-g', 'add_repo', is_flag=True, help=HELP_GIT)
def create(project_name, add_repo):
    click.echo('Name: %s - Git: %s' % (project_name, add_repo))


if __name__ == '__main__':
    cli()