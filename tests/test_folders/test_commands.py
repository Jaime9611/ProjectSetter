import logging
import subprocess
import re

from pathlib import PurePosixPath

from .temporals import tmp_folder
from .temporals import get_all_files
from .temporals import get_main_files


LOGGER = logging.getLogger(__name__)


class TestCommands:
    def test_project_setter_command(self):
        result = subprocess.run(['project-setter'], 
            capture_output=True).stdout.decode('utf-8')

        pattern = r'Commands:[\s]*mkpy[\s\S]*mkweb'

        assert re.search(pattern, result)

    def test_project_setter_help_command(self):
        result = subprocess.run(['project-setter', '--help'], 
            capture_output=True).stdout.decode('utf-8')

        pattern = r'Commands:[\s]*mkpy[\s\S]*mkweb'

        assert re.search(pattern, result)

    def test_web_project_command(self, tmp_folder):
        project_name = "WebProject1"
        command = [
            "cd", str(tmp_folder),
            "&&",
            "project-setter", "mkweb", project_name,
        ]
        result = subprocess.call(command, shell=True)

        created = get_main_files(tmp_folder)

        LOGGER.debug(created)

        assert project_name in created

        