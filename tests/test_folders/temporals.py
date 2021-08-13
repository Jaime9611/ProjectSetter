from project_setter.cli_commands import LOGGER
import pytest
import logging

LOGGER = logging.getLogger(__name__)

@pytest.fixture(scope="function")
def tmp_folder(tmp_path_factory):
    print(type(tmp_path_factory))
    d = tmp_path_factory.mktemp('TestDir')
    LOGGER.debug(str(d))
    return d

def get_main_files(folder):
        created_files = folder.iterdir()
        created_files = [file.name for file in created_files]

        return created_files

def get_all_files(folder):
    created_files = []
    for item in folder.iterdir():
        if item.is_dir():
            child_list = [
                f'{f.parent.name}/{f.name}' for f in item.iterdir()
                ]
            created_files += child_list
        else:
            created_files.append(item.name)

    return created_files