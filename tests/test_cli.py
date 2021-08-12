import unittest
import subprocess
from pathlib import Path

from .context import cli_commands

class CliTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_dir = Path(__file__).parent / 'TestDir'
        cls.test_dir.mkdir()

    def test_temporary_dir_created(self):
        self.assertTrue(self.test_dir.exists())

    def test_start_git_repository(self):
        cli_commands.start_git(self.test_dir)

        dir_files = self.test_dir.iterdir()
        dir_files = [file.name for file in dir_files]
        print(dir_files)

        self.assertIn('.git', dir_files)

    def test_get_pwd(self):
        pwd = cli_commands.get_pwd_path()

        self.assertRegex(pwd, r'^/|.+/.*$')

    @classmethod
    def tearDownClass(cls):
        remove = subprocess.run(['rm', '-rf', cls.test_dir], shell=True)



if __name__ == '__main__':
    unittest.main()