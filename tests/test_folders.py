import pytest

from .context import folders


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
