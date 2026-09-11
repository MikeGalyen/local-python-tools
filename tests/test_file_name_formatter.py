from file_name_formatter import _print_all_objects

from pathlib import Path

"""
Unit tests for file_name_formatter.py tool
"""

def test_print_all_objects():
    path = Path(".")
    _print_all_objects(path)