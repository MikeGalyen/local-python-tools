from file_name_formatter import _print_all_objects

from pathlib import Path

def test_print_all_objects():
    path = Path(".")
    _print_all_objects(path)