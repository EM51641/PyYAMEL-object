import os


def get_path():
    """
    get path of the test file
    """
    dir_path = os.path.dirname(__file__)
    path = os.path.join(dir_path, "test.yaml")
    return path
