import argparse
from pathlib import Path


# list of files and dirs not to rename
do_not_change_these = [
    "README.md",
    "src"
]


def _parse_args() -> argparse.Namespace:
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
    parser.add_argument("-r", "--recursive", action="store_true")

    return parser.parse_args()


def _append_do_not_change_list(append_name: [str]) -> None:
    """
    Append user povided files or dirs to the do not change list

    :param list append_name:
    :return: None
    """
    if append_name is not None:
        print(f"Ignoring: {append_name}")
        do_not_change_these.append(append_name)


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


def _uppercase(path_object: Path) -> None:
    """
    TODO

    :param Path dir: A Path object to iterate
    :return: None
    """
    
    path_object.rename(path_object.with_name(path_object.name.upper().replace("-", "_")))
            

def _lowercase(path_object: Path) -> None:
    """
    TODO

    :param Path dir: A Path object to iterate
    :return: None
    """
    
    path_object.rename(path_object.with_name(path_object.name.lower().replace("-", "_")))

    
def _rename(dir: Path, recursive: bool = False) -> None:
    """
    TODO
    """

    if recursive:
        for root, dirs, files in dir.walk(top_down=False):
            for name in dirs:
                if name not in do_not_change_these:
                    old = root / name
                    new = root / name.upper().replace("-", "_")
                    old.rename(new)
            for name in files:
                if name not in do_not_change_these:
                    old = root / name
                    new = root / name.lower().replace("-", "_")
                    old.rename(new)
        return 

    for x in dir.iterdir():
        if x.is_file() and not x.name.startswith(".") and x.name not in do_not_change_these:
            _lowercase(x)
        if x.is_dir() and not x.name.startswith(".") and x.name not in do_not_change_these:
            _uppercase(x)

def main() -> None:
    """
    Calls all the helper functions 

    :param str user_path: A user provided path (str) to a directory
    :return: None
    """

    args = _parse_args()
    path_object = _get_path_object(args.path)

    _rename(path_object, args.recursive)
  
    _print_all_objects(path_object)


if __name__ == "__main__":
    main()