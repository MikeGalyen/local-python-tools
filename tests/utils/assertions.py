from src.file_name_formatter import ignore, _ignore_list, append_ignore_list


def assert_name_in_ignore_list_after_append(name: [str], expected_name: str):
    append_ignore_list(name)
    assert expected_name in _ignore_list
    _ignore_list.pop()


def assert_name_not_in_ignore_list(name: str):
    pass
