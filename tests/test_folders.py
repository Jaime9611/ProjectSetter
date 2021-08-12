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

    def test_tmp_dir_exists(self, tmp_folder):
        tmp_folder.exists()

    def test_project_creation(self, tmp_folder):
        received = folders.Project('NewProject', tmp_folder)

        assert received.BASE_DIR == tmp_folder

    def test_web_project_creation(self, tmp_folder):
        project_name = "WebTest1"

        web_project = folders.WebProject(project_name, tmp_folder)
        web_project.create_project()

        created_dirs = tmp_folder.iterdir()
        created_dirs = [file.name for file in created_dirs]
        LOGGER.debug(created_dirs)

        assert project_name in created_dirs

    def test_web_project_main_structure_correct(self, tmp_folder):
        project_name = "WebTest2"
        web_project = folders.WebProject(project_name, tmp_folder)
        web_project.create_project()

        created = (tmp_folder / project_name).iterdir()
        created = [file.name for file in created]
        LOGGER.debug(created)

        expected = ['.gitignore', 'index.html', 'css', 'js', 'assets']

        assert sorted(created) == sorted(expected)

    def test_web_project_files_correct(self, tmp_folder):
        project_name = "WebTest3"
        web_project = folders.WebProject(project_name, tmp_folder)
        web_project.create_project()

        created = []
        for item in (tmp_folder / project_name).iterdir():
            if item.is_dir():
                child_list = [
                    f'{f.parent.name}/{f.name}' for f in item.iterdir()
                    ]
                created += child_list
            else:
                created.append(item.name)
        LOGGER.debug(created)

        expected = ['.gitignore', 'assets/icons', 'assets/images', 'index.html', 'js/main.js', 'css/style.css']

        assert sorted(created) == sorted(expected)

