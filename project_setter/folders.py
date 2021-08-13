"""Folders Script

This script contains classes that represent the types of Projects, it's route access, name and files it has.

This script has the following classes:
    * Project - Parent class that represents a general Project.
    * WebProject - Child class that represents a WEB Project.
    * PyProject - Child class that represents a PYTHON Project.
"""

from pathlib import Path

from . import data
from .data import Project as project_type


class Project:
    """Class that represents a general project.

    Attributes
    __________
    BASE_DIR : Path
        Parent directory where the project will be created.
    project_path : Path
        Child directory that will contain the project.

    Methods
    _______
    _check_base()
        Secondary method that verifies if the BASE_DIR already exists.
    _create_files(parent_path, files)
        Secondary method to create files in the given path.
    _create_subfolders(parent_path, files)
        Secondary method to create subfolders in the given path.
    create_project()
        Primary method that creates the files and subfolders.
    """

    def __init__(self, project_name, root):
        """Inicializes the attributes

        Parameters
        __________
        project_name : String object
            Project's name.
        root : String object
            String with the path to the project.
        """
        assert type(project_name) == str, "Project name not a String"
        assert " " not in project_name, "Project name must not have spaces"
        assert type(root) == str, "Root argument not a String"


        self.BASE_DIR = Path(root)
        self._check_base()
        self.project_path = self.BASE_DIR / project_name

    def _check_base(self):
        """Verifies if the Main folder exists otherwise it will create it."""

        try:
            self.BASE_DIR.mkdir()
        except FileExistsError:
            pass

    def _create_files(self, parent_path, files):
        """Helper method for create file in the given path
        
        Parameters
        _________
        parent_path : Path Object
            Path with the location of the parent folder.
        files : List Object
            List of strings with the files' names.
        """

        for file in files:
            new_file = parent_path / file
            new_file.touch()

    def _create_subfolders(self, parent_path, subfolders):
        """Helper method for create subfolders in the given path
        
        Parameters
        _________
        parent_path : Path Object
            Path with the parent location.
        subfolders : List Object
            List of strings with the subfolders' names.
        """

        for folder in subfolders:
            new_folder = parent_path / folder
            new_folder.mkdir()
            if subfolders[folder]:
                if type(subfolders[folder]) == list:
                    self._create_files(new_folder, subfolders[folder])
                elif type(subfolders[folder]) == dict:
                    new_parent = new_folder
                    self._create_subfolders(new_parent, subfolders[folder])

    def create_project(self):
        """"Method to create files and subfolders of the project.
        
        Returns
        _______
        existed : Boolean Object
            Determines if the project was created or if it already exists, True if project already exists, False otherwise.
        """

        existed = False
        try:
            self.project_path.mkdir()

            for folder in self.FOLDERS:
                if folder == 'files':
                    self._create_files(self.project_path, self.FOLDERS[folder])
                elif folder == 'subfolders':
                    self._create_subfolders(self.project_path, self.FOLDERS[folder])
        except FileExistsError:
            existed = True

        assert type(existed) == bool, "Function not returning not a boolean"

        return existed


class WebProject(Project):
    """Child class that represents a WEB project.
    
    Attributes
    __________
    Folders : Dict Object
        Dictionary containing files and subfolders structure for a WEB project.
    """

    def __init__(self, project_name, root):
        """Inicializes the attributes of his parent and FOLDERS attribute."""
        super().__init__(project_name, root)
        self.FOLDERS = data.get_project_structure(project_type.WEB)


class PyProject(Project):
    """Child class that represents a WEB project.
    
    Attributes
    __________
    Folders : Dict Object
        Dictionary containing files and subfolders structure for a WEB project.
    """

    def __init__(self, project_name, root):
        """Inicializes his parent attributes and FOLDERS attribute."""
        super().__init__(project_name, root)
        self.project_name = project_name
        self.FOLDERS = data.get_project_structure(project_type.PYTHON)

    def create_project(self, pkg):
        """Method for create a python project.
        
        This method overrides his parent, to be able to change the project structure contained in FOLDERS.
        """

        assert type(pkg) == bool, "pkg argument has to be boolean"

        if pkg:
            pkg_folder = self.project_name.lower()
            self.FOLDERS['subfolders'][pkg_folder] = [
                '__init__.py', 'main.py']
            self.FOLDERS['subfolders']['tests'] = ['test.py']
        else:
            self.FOLDERS['files'] += ['main.py', 'test.py']

        return super().create_project()

