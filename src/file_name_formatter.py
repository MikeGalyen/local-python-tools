import argparse
from pathlib import Path
import logging
import re


# list of files and dirs not to rename
ignore_list = [
    "README.md",
    "src"
]

#
log = logging.getLogger(__name__)


def parse_args() -> argparse.Namespace:
    """
    Parse user args from CLI input

    :return: None
    """

    parser = argparse.ArgumentParser(
    prog="Case changer",
    description="Changes directory names to uppercase and file names to lowercase with underscores"
    )

    parser.add_argument("path")
    parser.add_argument("-i", "--ignore", nargs="+")
    parser.add_argument("-r", "--recursive", action="store_true")
    parser.add_argument("-t", "--top", action="store_true")

    return parser.parse_args()


def ignore(name: str) -> boolean:
    """
    Check if name matches names in ignore list and handle wildcard *

    :param name str: a filename
    :return: boolean
    """
    for ignore_name in ignore_list:
        if ".*" in ignore_name:
            if re.fullmatch(ignore_name, name):
                return True
        elif name in ignore_list:
            return True
    return False
    


def append_do_not_change_list(append_name: [str]) -> None:
    """
    Append user povided files or dirs to the do not change list and replace wildcard * with .*

    :param list append_name: a list of strings to append to the do not change list
    :return: None
    """
    if append_name is not None:
        for name in append_name:
            if "*" in name:
                name_with_re_pattern = name.replace("*", ".*")
                ignore_list.append(name_with_re_pattern)
            else:
                ignore_list.append(name)
    print(f"Ignoring: {ignore_list}")


def get_path_object(user_path: str) -> Path:
    """
    Convert a user str file path into a Path obejct

    :param str user_path: A user provided path (str) to a directory
    :return: A Path object based on the user provided path str
    """

    return Path(user_path)


def uppercase_dirs(top_dir: Path, recursive: boolean = False, change_root: boolean = False) -> None:
    """
    Transform dir names to uppercase and replace hyphens with underscores

    :param Path dir: A Path object to iterate
    :return: None
    """

    if not top_dir.exists():
        log.error(f"Directory {top_dir.name} does not exist")
        raise FileNotFoundError

    if not top_dir.is_dir():
        log.error(f"{top_dir.name} is not a directory")
        raise TypeError

    if recursive:
        for root, dirs, files in top_dir.walk(top_down=False): 
            for name in dirs:
                if not ignore(name):
                    old = root / name
                    new = root / name.upper().replace("-", "_")
                    old.rename(old.with_name(new.name))
    
    else:
        for x in top_dir.iterdir():
            if x.is_dir() and not x.name.startswith(".") and not ignore(x.name):
                x.rename(x.with_name(x.name.upper().replace("-", "_")))

    if change_root:
        for root, dirs, files in top_dir.walk(top_down=False): 
            new = root.name.upper().replace("-", "_")
            root.rename(root.with_name(new))
            

def lowercase_files(top_dir: Path, recursive: boolean = False) -> None:
    """
    Transform filenames to lowercase and replace hyphens with underscores

    :param Path dir: A Path object to iterate
    :return: None
    """

    if not top_dir.exists():
        log.error(f"Directory {top_dir.name} does not exist")
        raise FileNotFoundError

    if not top_dir.is_dir():
        log.error(f"{top_dir.name} is not a directory")
        raise TypeError

    if recursive:
        for root, dirs, files in top_dir.walk(top_down=False): 
                for name in files:
                    if not ignore(name):
                        old = root / name
                        new = root / name.lower().replace("-", "_")
                        old.rename(old.with_name(new.name))

    else:
        for x in top_dir.iterdir():
            if x.is_file() and not x.name.startswith(".") and not ignore(x.name):
                x.rename(x.with_name(x.name.lower().replace("-", "_")))

    
def rename(dir: Path, recursive: bool = False, change_root: bool = False) -> None:
    """
    Rename files and dirs recursively or at one dir level

    :param dir Path: a path to iterate
    :param recursive bool: flag from CLI args for recursing dirs
    """
    
    lowercase_files(dir, recursive)
    uppercase_dirs(dir, recursive, change_root)


def main() -> int:
    """
    Calls all the helper functions 

    :param str user_path: A user provided path (str) to a directory
    :return int: 0 if successfull
    """

    args = parse_args()
    path_object = get_path_object(args.path)

    append_do_not_change_list(args.ignore)
    rename(path_object, args.recursive, args.top)

    return 0


if __name__ == "__main__":
    main()