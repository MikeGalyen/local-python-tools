from src.file_name_formatter import get_path_object, append_ignore_list, ignore_list
from tests.utils.tests_path import TESTS_PATH

from pathlib import Path
import pathlib

"""
Unit tests for file_name_formatter.py tool
"""

# unit tests for get_path_object()

def test_get_path_object_return_type():
    assert type(get_path_object("/")) == pathlib.PosixPath

def test_get_path_object_error_type():
    try:
        type(get_path_object("not-a-real-dir"))
    except NotADirectoryError:
        assert True
    else:
        assert False

def test_get_path_object_path():
    assert get_path_object(Path.cwd()).name == "tests"

# unit tests for append_ignore_list()

def test_append_ignore_list_return_type():
    assert append_ignore_list("/") == None

def test_append_ignore_list_with_str_name():
    append_ignore_list(["test_name"])
    assert "test_name" in ignore_list

def test_append_ignore_list_with_wildcard_front():
    append_ignore_list(["*-test.txt"])
    append_ignore_list(["*.txt"])
    append_ignore_list(["*"])
    assert ".*-test.txt" in ignore_list
    assert ".*.txt" in ignore_list
    assert ".*" in ignore_list

def test_append_ignore_list_with_wildcard_back():
    append_ignore_list(["test.*"])
    append_ignore_list(["test*"])
    assert "test..*" in ignore_list
    assert "test.*" in ignore_list

def test_append_ignore_list_with_wildcard_middle():
    append_ignore_list(["test*.txt"])
    append_ignore_list(["test*txt"])
    append_ignore_list(["t*.txt"])
    assert "test.*.txt" in ignore_list
    assert "test.*txt" in ignore_list
    assert "t.*.txt" in ignore_list

def test_append_ignore_list_with_wildcard_combo():
    append_ignore_list(["test*.*"])
    append_ignore_list(["*test*txt"])
    assert "test.*..*" in ignore_list
    assert ".*test.*txt" in ignore_list


