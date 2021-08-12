import logging

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
        created = folders.WebProject("NewProject", tmp_folder)
        created.create_project()

        dir_files = tmp_folder.iterdir()
        dir_files = [file.name for file in dir_files]
        LOGGER.debug(dir_files)

        assert "NewProjec" in dir_files

