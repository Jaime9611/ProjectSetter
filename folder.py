from pathlib import Path
import json


class Project:
    def __init__(self, project_name, root):
        self.BASE_DIR = Path(root)
        self.project_path = self.BASE_DIR / project_name

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
            print('Este folder ya existe.')
            return e

        for folder in self.FOLDERS:
            if folder == 'files':
                self._create_files(self.project_path, self.FOLDERS[folder])
            elif folder == 'subfolders':
                self._create_subfolders(self.project_path, self.FOLDERS[folder])


class WebProject(Project):
    def __init__(self, project_name, root):
        super().__init__(project_name, root)
        with open('./data/structures.json') as f:
            folders = json.load(f)
        self.FOLDERS = folders['web']