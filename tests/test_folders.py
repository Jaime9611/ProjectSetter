import logging
from project_setter.data import Project

import pytest

from .context import folders

LOGGER = logging.getLogger(__name__)


class TestFolders:
    @pytest.fixture(scope="class")
    def tmp_folder(self, tmp_path_factory):
        print(type(tmp_path_factory))
        d = tmp_path_factory.mktemp('TestDir')

        return d

    def _get_main_files(self, folder):
        created_files = folder.iterdir()
        created_files = [file.name for file in created_files]
        LOGGER.debug(created_files)

        return created_files

    def _get_all_files(self, folder):
        created_files = []
        for item in folder.iterdir():
            if item.is_dir():
                child_list = [
                    f'{f.parent.name}/{f.name}' for f in item.iterdir()
                    ]
                created_files += child_list
            else:
                created_files.append(item.name)
        LOGGER.debug(created_files)

        return created_files

    def test_tmp_dir_exists(self, tmp_folder):
        tmp_folder.exists()

    def test_project_creation(self, tmp_folder):
        created = folders.Project('NewProject', tmp_folder)

        assert created.BASE_DIR == tmp_folder

    def test_web_project_creation(self, tmp_folder):
        project_name = "WebTest1"

        web_project = folders.WebProject(project_name, tmp_folder)
        web_project.create_project()

        created_files = self._get_main_files(tmp_folder)

        assert project_name in created_files

    def test_web_project_main_structure_correct(self, tmp_folder):
        project_name = "WebTest2"
        web_project = folders.WebProject(project_name, tmp_folder)
        web_project.create_project()

        folder = tmp_folder / project_name
        created = self._get_main_files(folder)

        expected = ['.gitignore', 'index.html', 'css', 'js', 'assets']

        assert sorted(created) == sorted(expected)

    def test_web_project_files_correct(self, tmp_folder):
        project_name = "WebTest3"
        web_project = folders.WebProject(project_name, tmp_folder)
        web_project.create_project()

        folder = tmp_folder / project_name
        created = self._get_all_files(folder)

        expected = ['.gitignore', 'assets/icons', 'assets/images', 'index.html', 'js/main.js', 'css/style.css']

        assert sorted(created) == sorted(expected)

    def test_python_simple_project_correct(self, tmp_folder):
        project_name = "PythonTest1"
        py_project = folders.PyProject(project_name, tmp_folder)
        py_project.create_project(pkg=False)

        folder = tmp_folder / project_name
        created = self._get_main_files(folder)

        expected = [
            "MANIFEST.in", "pyproject.toml", "setup.cfg",
            "setup.py", ".gitignore", "main.py", "test.py",
        ]

        assert sorted(created) == sorted(expected)

    def test_python_pkg_project_correct(self, tmp_folder):
        project_name = "PythonTest3"
        py_project = folders.PyProject(project_name, tmp_folder)
        py_project.create_project(pkg=True)

        folder = tmp_folder / project_name
        created = self._get_all_files(folder)

        expected = [
            "MANIFEST.in", "pyproject.toml", "setup.cfg",
            "setup.py", ".gitignore",
            f"{project_name.lower()}/main.py",
            f"{project_name.lower()}/__init__.py",
            "tests/test.py",
        ]

        assert sorted(created) == sorted(expected)

    
    def test_project_already_created(self, tmp_folder):
        project_name = "PythonTest4"
        py_project = folders.PyProject(project_name, tmp_folder)

        successful = py_project.create_project(pkg=True) # First time
        successful = py_project.create_project(pkg=True) # Second time

        assert successful == False



