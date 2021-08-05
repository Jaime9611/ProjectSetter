import unittest
from pathlib import Path
import json

from .context import data

RESOURCES = Path(__file__).parent.parent / 'project_setter' /'resources'


class DataTests(unittest.TestCase):
    def test_get_base_path_web(self):
        with open(RESOURCES / 'project_paths.json') as f:
            expected = json.load(f)

        result = data.get_base_path(data.Project.WEB)

        self.assertEqual(result, expected['web'])

    def test_get_base_path_python(self):
        with open(RESOURCES / 'project_paths.json') as f:
            expected = json.load(f)

        result = data.get_base_path(data.Project.PYTHON)

        self.assertEqual(result, expected['python'])

    def test_incorrect_project_type_in_path(self):
        with open(RESOURCES / 'project_paths.json') as f:
            expected = json.load(f)

        with self.assertRaises(Exception) as context:
            result = data.get_base_path('python')

        self.assertTrue('Argument type not a Project.' in str(context.exception))

    def test_incorrect_project_type_in_structure(self):
        with open(RESOURCES / 'project_paths.json') as f:
            expected = json.load(f)

        with self.assertRaises(Exception) as context:
            result = data.get_project_structure('python')

        self.assertTrue('Argument type not a Project.' in str(context.exception))


if __name__ == "__main__":
    unittest.main()