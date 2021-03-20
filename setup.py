from setuptools import setup

setup(
    name='ProjectSetter',
    version='0.1',
    py_modules=['hello', 'folders', 'cli_commands'],
    install_requires=[
        'Click',
    ],
    include_package_data=True,
    entry_points='''
        [console_scripts]
        project-set=hello:cli
    ''',
)