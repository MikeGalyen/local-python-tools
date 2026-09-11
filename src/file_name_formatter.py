import argparse
from pathlib import Path


# list of files and dirs not to rename
do_not_change_these = [
    "README.md",
    "src"
]


def _append_do_not_change_list(append_name: [str]) -> None:
    """
    Append user povided files or dirs to the do not change list

    :param list append_name:
    :return: None
    """
    if append_name is not None:
        print(f"Ignoring: {append_name}")
        do_not_change_these.append(append_name)


def _parse_args() -> None:
    """
    Parse user args from CLI input
    :return: None
    """
    parser = argparse.ArgumentParser(
    prog="Case changer",
    description="Changes directory names to uppercase and file names to lowercase with underscores"
    )

    parser.add_argument("path")
    parser.add_argument("-i", "--ignore")

    return parser.parse_args()


def _get_path_object(user_path: str) -> Path:
    """
    Convert a user str file path into a Path obejct

    :param str user_path: A user provided path (str) to a directory
    :return: A Path object based on the user provided path str
    """
    return Path(user_path)


def _print_all_objects(dir: Path) -> None:
    """
    Print the directories then the files at a speciied directory

    :param Path dir: A Path object to iterate
    :return: None
    """
    print("\n-DIRS")
    for object in dir.iterdir():
        if object.is_dir():
            print(object.name)
    print("\n-FILES")
    for object in dir.iterdir():
        if object.is_file():
            print(object.name)
    print("\n")


def _uppercase_dirs(dir: Path) -> None:
    """
    Iterate over objects in a directory and convert the naming of directories to 
    be all uppercase and convert any hyphens to underscores.

    :param Path dir: A Path object to iterate
    :return: None
    """
    for x in dir.iterdir():
        if x.is_dir() and not x.name.startswith(".") and x.name not in do_not_change_these:
            x.rename(x.with_name(x.name.upper().replace("-", "_")))
            

def _lowercase_files(dir: Path) -> None:
    """
    Iterate over objects in a directory and convert the naming of files to 
    be all lowercase and convert any hyphens to underscores.

    :param Path dir: A Path object to iterate
    :return: None
    """
    for x in dir.iterdir():
        if x.is_file() and not x.name.startswith(".") and x.name not in do_not_change_these:
            x.rename(x.with_name(x.name.lower().replace("-", "_")))


def main() -> None:
    """
    Calls all the helper functions 

    :param str user_path: A user provided path (str) to a directory
    :return: None
    """
    args = _parse_args()
    path_object = _get_path_object(args.path)
    _uppercase_dirs(path_object)
    _lowercase_files(path_object)
    _print_all_objects(path_object)


if __name__ == "__main__":
    main()