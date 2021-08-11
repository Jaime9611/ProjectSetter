import pytest
from pathlib import Path
import json

from .context import data

RESOURCES = Path(__file__).parent.parent / 'project_setter' /'resources'


class TestData():
    def test_get_base_path_web(self):
        with open(RESOURCES / 'project_paths.json') as f:
            expected = json.load(f)

        result = data.get_base_path(data.Project.WEB)

        assert result == expected['web']

    def test_get_base_path_python(self):
        with open(RESOURCES / 'project_paths.json') as f:
            expected = json.load(f)

        result = data.get_base_path(data.Project.PYTHON)

        assert result == expected['python']

    def test_get_structure_web(self):
        with open(RESOURCES / 'structures.json') as f:
            expected = json.load(f)

        result = data.get_project_structure(data.Project.WEB)

        assert result == expected['web']

    def test_get_structure_python(self):
        with open(RESOURCES / 'structures.json') as f:
            expected = json.load(f)

        result = data.get_project_structure(data.Project.PYTHON)

        assert result == expected['python']

    def test_incorrect_project_type_in_path(self):
        with open(RESOURCES / 'project_paths.json') as f:
            expected = json.load(f)

        with pytest.raises(Exception) as excinfo:
            result = data.get_base_path('python')

        assert 'Argument type not a Project variable.' in str(excinfo.value)

    def test_incorrect_project_type_in_structure(self):
        with open(RESOURCES / 'project_paths.json') as f:
            expected = json.load(f)

        with pytest.raises(Exception) as excinfo:
            result = data.get_project_structure('python')

        assert 'Argument type not a Project variable.' in str(excinfo.value)