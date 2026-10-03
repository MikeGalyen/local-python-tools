from src.file_name_formatter import get_path_object, append_ignore_list, _ignore_list, ignore, uppercase_dirs, lowercase_files
from tests.utils.assertions import assert_name_in_ignore_list_after_append
from tests.utils.test_dir_utils import make_test_dirs, delete_test_dirs, make_test_file, make_random_test_files_and_dirs
from tests.utils.test_data.path_to_test_data_dir import get_test_data_dir_path

from pathlib import Path
import pathlib
import pytest

"""
Unit tests for file_name_formatter.py tool
"""


# get_path_object()

def test_get_path_object_return_type():
    assert type(get_path_object("/")) == pathlib.PosixPath


def test_get_path_object_error_handling():
    try:
        type(get_path_object("not-a-real-dir"))
    except NotADirectoryError:
        assert True
    else:
        assert False


def test_get_path_object_path():
    working_dir = Path.cwd().name
    assert get_path_object(Path.cwd()).name == working_dir


# append_ignore_list()

def test_append_ignore_list_returns_none():
    assert append_ignore_list(["FILE"]) == None


def test_append_ignore_list_with_str_name():
    assert_name_in_ignore_list_after_append(["test_name"], "test_name")


def test_append_ignore_list_defaults():
    assert "src" in _ignore_list 
    assert "README.md" in _ignore_list


# ignore()

def test_ignore_return_type():
    assert type(ignore("src")) == bool
    assert type(ignore("not-in-ignore-list")) == bool


def test_ignore_with_str():
    assert ignore("README.md")
    assert ignore("src")
    assert ignore(".python-version")
    assert not ignore("not-in-ignore-list")
    assert not ignore("s")


def test_ignore_with_wildcards():
    assert ignore("*.md")
    assert ignore("README*")
    assert ignore("*E*DME*")
    assert ignore("s*c")
    assert ignore("*python*")
    assert ignore("*")


# uppercase_dirs()

def test_uppercase_dirs_returns_none():
    make_test_dirs()
    test_dir_path = Path(f"{get_test_data_dir_path()}/temp/test-dir-0")
    assert uppercase_dirs(test_dir_path) == None
    delete_test_dirs()


def test_uppercase_dirs_non_exsistent_dir_error_handling():
    non_existent_dir = Path(f"{get_test_data_dir_path()}/not-a-real-dir")
    make_test_file("test.txt")
    try:
        uppercase_dirs(Path(f"{get_test_data_dir_path()}/test.txt"))
    except TypeError:
        assert True
    else:
        assert False
    delete_test_dirs()

@pytest.mark.devtest
def test_uppercase_dirs_one_level_to_upper():
    make_random_test_files_and_dirs(10, 6)
    delete_test_dirs()


# lowercase_files()


