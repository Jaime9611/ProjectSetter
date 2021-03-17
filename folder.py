from pathlib import Path
from typing import List


MAIN_FOLDER = 'C:/Users/JAB/Documents/WEB'


class Project:
    def __init__(self, project_name, folders):
        self.BASE_DIR = Path(MAIN_FOLDER)
        self.FOLDERS = folders
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


if __name__ == '__main__':
    d = {
        'files': ['index.html', '.gitignore'],
        "subfolders": {
            "css": ["style.css"],
            "js": ["main.js"],
            "assets": {"images": [], "icons": []}
        }
    }
    p = Project('TEST', d)
    p.create_project()