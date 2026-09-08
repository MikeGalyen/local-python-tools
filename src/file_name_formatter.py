import argparse
from pathlib import Path

# list of files to not rename
do_not_change_these_files = [
    "README.md"
]

# list of dirs not to change
do_not_change_these_dirs = [
    "src"
]

######################################################
#                  Helper Functions                  #
######################################################


def get_path_object(user_path: str) -> Path:
    """
    Convert a user str file path into a Path obejct

    :param str user_path: A user provided path (str) to a directory
    :return: A Path object based on the user provided path str
    """
    return Path(user_path)


def print_all_objects(dir: Path) -> None:
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


def uppercase_dirs(dir: Path) -> None:
    """
    Iterate over objects in a directory and convert the naming of directories to 
    be all uppercase and convert any hyphens to underscores.

    :param Path dir: A Path object to iterate
    :return: None
    """
    for x in dir.iterdir():
        if x.is_dir() and not x.name.startswith(".") and x.name not in do_not_change_these_dirs:
            x.rename(x.name.upper().replace("-", "_"))


def lowercase_files(dir: Path) -> None:
    """
    Iterate over objects in a directory and convert the naming of files to 
    be all lowercase and convert any hyphens to underscores.

    :param Path dir: A Path object to iterate
    :return: None
    """
    for x in dir.iterdir():
        if x.is_file() and not x.name.startswith(".") and x.name not in do_not_change_these_files:
            x.rename(x.name.lower().replace("-", "_"))


def rename(user_path: str) -> None:
    """
    Calls all the helper functions in order to rename dirs and files based on the patterns, dir = all capital letters 
    with underscores and files = all lowercase letters with underscores.

    :param str user_path: A user provided path (str) to a directory
    :return: None
    """
    # set path object from user string
    path_object = get_path_object(user_path)
    # change all dir names to be in all caps and convert hyphens to undersores
    uppercase_dirs(path_object)
    # change all file names to be in all lower case and convert hyphens to underscores
    lowercase_files(path_object)
    # print a formatted list of dirs then a formatted list of files
    print_all_objects(path_object)


######################################################
#                      Main                          #
######################################################


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Case changer",
        description="Changes dirs to uppercase and files to lowercase and both with underscores"
    )

    parser.add_argument("path")

    args = parser.parse_args()

    rename(args.path)