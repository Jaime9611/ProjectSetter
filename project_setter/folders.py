from pathlib import Path

from . import data
from .data import Project as project_type


class Project:
    def __init__(self, project_name, root):
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
        for file in files:
            new_file = parent_path / file
            new_file.touch()

    def _create_subfolders(self, parent_path, subfolders):
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
        try:
            self.project_path.mkdir()
        except FileExistsError as e:
            return False

        for folder in self.FOLDERS:
            if folder == 'files':
                self._create_files(self.project_path, self.FOLDERS[folder])
            elif folder == 'subfolders':
                self._create_subfolders(self.project_path, self.FOLDERS[folder])

        return True


class WebProject(Project):
    def __init__(self, project_name, root):
        super().__init__(project_name, root)
        self.FOLDERS = data.get_project_structure(project_type.WEB)


class PyProject(Project):
    def __init__(self, project_name, root):
        super().__init__(project_name, root)
        self.project_name = project_name
        self.FOLDERS = data.get_project_structure(project_type.PYTHON)

    def create_project(self, pkg):
        if pkg:
            pkg_folder = self.project_name.lower()
            self.FOLDERS['subfolders'][pkg_folder] = [
                '__init__.py', 'main.py']
            self.FOLDERS['subfolders']['tests'] = ['test.py']
        else:
            self.FOLDERS['files'] += ['main.py', 'test.py']

        return super().create_project()

