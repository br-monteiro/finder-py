import src.params as params
from src.utils import get_ext, re_test
from src.disc_manager import isfile, get_filename


def path_match(path):
    """
    Checks if a value was entered in the argument 'path-match'
    In case of success, fire the pattern in current 'path'
    """
    _path_match = params.get_path_match()

    if not _path_match:
        return None

    return re_test(_path_match, path)


def path_dont_match(path):
    """
    Checks if a value was entered in the argument 'path-dont-match'
    In case of success, fire the pattern in current 'path'
    """
    _path_dont_match = params.get_path_dont_match()

    if not _path_dont_match:
        return None

    return re_test(_path_dont_match, path)


def isfile_match(path):
    """
    Checks if a value was entered in the argument 'file-match'
    In case of success, fire the pattern in current 'path'
    """
    file_match = params.get_file_match()

    if not file_match:
        return None

    return re_test(file_match, path)


def isfile_dont_match(path):
    """
    Checks if a value was entered in the argument 'file-dont-match'
    In case of success, fire the pattern in current 'path'
    """
    file_dont_match = params.get_file_dont_match()

    if not file_dont_match:
        return None

    return re_test(file_dont_match, path)


def only_extension(extension):
    """
    Check if the file has a allowed extension
    """
    _only_extension = params.get_only_extensions()
    return bool(len(_only_extension) and extension not in _only_extension)


def except_extension(extension):
    """ Check if the file has a allowed extension """
    _except_extension = params.get_except_extensions()
    return bool(len(_except_extension) and extension in _except_extension)


def you_shall_not_pass(current_path):
    """
    Check the value of 'path-dont-match'
    If the path is not allowed, then continue the loop
    """
    if path_dont_match(current_path):
        return True

    """
    Check the value of 'path-match'
    If the path is not allowed, then continue the loop
    """
    if path_match(current_path) is False:
        return True

    if isfile(current_path):
        file_name = get_filename(current_path)

        """
        Check the value of 'file-dont-match'
        If the path is not allowed, then continue the loop
        """
        if isfile_dont_match(file_name):
            return True

        """
        Check the value of 'file-match'
        If the path is not allowed, then continue the loop
        """
        if isfile_match(file_name) is False:
            return True

        extension = get_ext(current_path)

        # Check if the file has a allowed extension
        if only_extension(extension):
            return True

        # Check if the file has a allowed extension
        if except_extension(extension):
            return True
    return False
