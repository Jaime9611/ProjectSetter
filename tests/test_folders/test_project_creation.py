from ..context import folders
from .temporals import tmp_folder
from .temporals import get_main_files
from .temporals import get_all_files


class TestFoldersStructure:
    def test_tmp_dir_exists(self, tmp_folder):
        tmp_folder.exists()

    def test_project_creation(self, tmp_folder):
        created = folders.Project('NewProject', str(tmp_folder))

        assert created.BASE_DIR == tmp_folder

    def test_web_project_creation(self, tmp_folder):
        project_name = "WebTest1"

        web_project = folders.WebProject(project_name, str(tmp_folder))
        web_project.create_project()

        created_files = get_main_files(tmp_folder)

        assert project_name in created_files

    def test_web_project_main_structure_correct(self, tmp_folder):
        project_name = "WebTest2"
        web_project = folders.WebProject(project_name, str(tmp_folder))
        web_project.create_project()

        folder = tmp_folder / project_name
        created = get_main_files(folder)

        expected = ['.gitignore', 'index.html', 'css', 'js', 'assets']

        assert sorted(created) == sorted(expected)

    def test_web_project_files_correct(self, tmp_folder):
        project_name = "WebTest3"
        web_project = folders.WebProject(project_name, str(tmp_folder))
        web_project.create_project()

        folder = tmp_folder / project_name
        created = get_all_files(folder)

        expected = ['.gitignore', 'assets/icons', 'assets/images', 'index.html', 'js/main.js', 'css/style.css']

        assert sorted(created) == sorted(expected)

    def test_python_simple_project_correct(self, tmp_folder):
        project_name = "PythonTest1"
        py_project = folders.PyProject(project_name, str(tmp_folder))
        py_project.create_project(pkg=False)

        folder = tmp_folder / project_name
        created = get_main_files(folder)

        expected = [
            "MANIFEST.in", "pyproject.toml", "setup.cfg",
            "setup.py", ".gitignore", "main.py", "test.py",
        ]

        assert sorted(created) == sorted(expected)

    def test_python_pkg_project_correct(self, tmp_folder):
        project_name = "PythonTest3"
        py_project = folders.PyProject(project_name, str(tmp_folder))
        py_project.create_project(pkg=True)

        folder = tmp_folder / project_name
        created = get_all_files(folder)

        expected = [
            "MANIFEST.in", "pyproject.toml", "setup.cfg",
            "setup.py", ".gitignore",
            f"{project_name.lower()}/main.py",
            f"{project_name.lower()}/__init__.py",
            "tests/test.py",
        ]

        assert sorted(created) == sorted(expected)



