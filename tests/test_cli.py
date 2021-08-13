import pytest
import subprocess
from pathlib import Path

from .context import cli_commands

class CliTest():
    @pytest.fixture(scope="function")
    def tmp_folder(self, tmp_path_factory):
        d = tmp_path_factory.mktemp('TestDir')

        return d

    def test_temporary_dir_created(self, tmp_folder):
        tmp_folder.exists()

    def test_start_git_repository(self, tmp_folder):
        cli_commands.start_git(tmp_folder)

        dir_files = tmp_folder.iterdir()
        dir_files = [file.name for file in dir_files]

        assert '.git' in dir_files

    def test_get_pwd(self, tmp_folder):
        subprocess.call(['cd', tmp_folder], shell=True)
        result = cli_commands.get_pwd_path()

        expected = subprocess.run(['cd', tmp_folder], shell=True, capture_output=True).stdout.decode('utf-8')

        assert result == expected