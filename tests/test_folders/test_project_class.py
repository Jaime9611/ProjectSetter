import pytest

from ..context import folders
from .temporals import tmp_folder

class TestFoldersClasses:
    def test_tmp_dir_exists(self, tmp_folder):
        tmp_folder.exists()

    def test_project_name_with_spaces(self, tmp_folder):
        with pytest.raises(AssertionError) as asrtinfo:
            result = folders.WebProject("New Project", str(tmp_folder))

        assert 'Project name must not have spaces' in str(asrtinfo.value)

    def test_project_name_not_string(self, tmp_folder):
        with pytest.raises(AssertionError) as asrtinfo:
            result = folders.WebProject(3, str(tmp_folder))

        assert 'Project name not a String' in str(asrtinfo.value)

    def test_project_root_not_string(self, tmp_folder):
        with pytest.raises(AssertionError) as asrtinfo:
            result = folders.WebProject("NewProject", tmp_folder)

        assert 'Root argument not a String' in str(asrtinfo.value)

    def test_python_project_creation_pkg_not_boolean(self, tmp_folder):
        project = folders.PyProject("NewProject", str(tmp_folder))
        with pytest.raises(AssertionError) as asrtinfo:
            project.create_project(pkg="True")

        assert 'pkg argument has to be boolean' in str(asrtinfo.value)

    def test_project_creation_returning_boolean_value(self, tmp_folder):
        project_name = "NewWeb"
        web_project = folders.WebProject(project_name, str(tmp_folder))

        successful = web_project.create_project()

        assert type(successful) == bool

    def test_project_already_created(self, tmp_folder):
        project_name = "NewWeb"
        web_project = folders.WebProject(project_name, str(tmp_folder))

        existed = web_project.create_project() # First time
        existed = web_project.create_project() # Second time

        assert existed == True