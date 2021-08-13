import logging
import subprocess
import re


LOGGER = logging.getLogger(__name__)


class TestCommands:
    def test_project_setter_command(self):
        result = subprocess.run(['project-setter'], 
            capture_output=True).stdout.decode('utf-8')

        pattern = r'Commands:[\s]*mkpy[\s\S]*mkweb'

        assert re.search(pattern, result)
        