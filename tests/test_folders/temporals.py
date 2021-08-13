import pytest

@pytest.fixture(scope="function")
def tmp_folder(tmp_path_factory):
    print(type(tmp_path_factory))
    d = tmp_path_factory.mktemp('TestDir')

    return d