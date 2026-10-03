from pathlib import Path

TESTS_PATH = Path(__file__).parent.absolute()

def get_test_data_dir_path():
    return TESTS_PATH