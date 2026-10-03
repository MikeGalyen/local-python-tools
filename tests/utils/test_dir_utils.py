from .test_data.path_to_test_data_dir import get_test_data_dir_path

from logging import Logger
from pathlib import Path
from shutil import rmtree
from random import randint

log = Logger(__name__)

def _get_temp_dir_path() -> str:
    return f"{get_test_data_dir_path()}/temp"

def _create_temp_dir() -> None:
    temp_dir_path = _get_temp_dir_path()
    try:
        Path.mkdir(temp_dir_path)
    except FileExistsError as e:
        log.warning("temp dir already exists")

def make_test_dirs(nest_levels: int = 1) -> None:
    _create_temp_dir()
    test_dirs = []
    for level in range(0, nest_levels):
        test_dirs.append(f"test-dir-{level}")
        new_dir = f"{_get_temp_dir_path()}/{"/".join(test_dirs)}"
        try:
            Path.mkdir(new_dir)
        except FileExistsError as e:
            log.warning(f"file {new_dir} already exists")

def make_test_file(file_name: str) -> None:
    _create_temp_dir()
    Path.touch(f"{_get_temp_dir_path()}/{file_name}")

def make_random_test_files_and_dirs(up_to_n_files: int = 1, n_levels: int = 1) -> None:
    dirs = []
    _create_temp_dir()
    temp_dir = Path(_get_temp_dir_path())
    for x in range(0, n_levels):
        test_dir = f"test-dir-{x}"
        dirs.append(test_dir)
        test_dir_full_path = f"{temp_dir}/{"/".join(dirs)}"
        Path.mkdir(test_dir_full_path)
        test_dir_path_object = Path(test_dir_full_path)
        for x in range(1, randint(1, up_to_n_files)):
            Path.touch(f"{test_dir_full_path}/Test-File-{x}")


def delete_test_dirs() -> None:
    try:
        rmtree(_get_temp_dir_path())
    except FileNotFoundError:
        log.warning("temp file may have already been deleted")
    except Exception:
        log.warning(f"temp dir may not have been deleted")
        
