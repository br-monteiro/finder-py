import os
from src.cli import get_argument
from src.disc_manager import add_end_slash
from src.utils import parse_int


def get_path():
    """ Returns the value of path argument """
    return add_end_slash(get_argument("path") or os.getcwd())


def get_by():
    """
    Returns the value of 'by' argument
    This value is used to be matching in files
    The value of 'by' argument is the search term
    """
    return get_argument("by")


def isrecursive():
    """ Indicate that recursively is enabled """
    return bool(get_argument("-recursive") or get_argument("-r"))


def get_recursive_level():
    """ Returns the max recursive level """
    MAX_LEVEL = 3
    level = get_argument("recursive-level") or get_argument("rl")

    if level is None:
        return MAX_LEVEL

    return parse_int(level, MAX_LEVEL)


def get_file_match():
    """ Returns the value of 'file-match' argument """
    return get_argument("file-match") or get_argument("fm")


def get_file_dont_match():
    """ Returns the value of 'file-dont-match' argument """
    return get_argument("file-dont-match") or get_argument("fdm")


def get_path_match():
    """ Returns the value of 'path-match' argument """
    return get_argument("path-match") or get_argument("pm")


def get_path_dont_match():
    """ Returns the value of 'path-dont-match' argument """
    return get_argument("path-dont-match") or get_argument("pdm")


def abstract_get_extension(argument):
    """ Abstract the return of 'except-extension' and 'only-extension' """
    extensions = get_argument(argument)

    if extensions is None:
        return []

    return extensions.split(",")


def get_except_extensions():
    """ Returns the value of 'except-extension' argument """
    argument_name = "except-extension" if get_argument("except-extension") else "ee"
    return abstract_get_extension(argument_name)


def get_only_extensions():
    """ Returns the value of 'only-extension' argument """
    argument_name = "only-extension" if get_argument("only-extension") else "oe"
    return abstract_get_extension(argument_name)


def is_quiet():
    """ Indicate that quiet mode is enabled """
    return bool(get_argument("-quiet") or get_argument("-q"))


def is_raw():
    """
  Indicates that the value raw of 'by' should be considered
  """
    return bool(get_argument("-raw"))


def is_help():
    """
  Check if the help mode is enabled
  """
    from sys import argv

    try:
        return argv.index("--help") == 1
    except ValueError:
        return False
