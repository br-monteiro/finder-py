import os
from src.cli import get_argument
from src.disc_manager import add_end_slash
from src.utils import parse_int

def get_path():
  """
  Returs the value of path argument
  """
  return add_end_slash(get_argument("path") or os.getcwd())

def get_by():
  """
  Returns the value of 'by' argument
  This value is used to be matching in files
  The value of 'by' argument is the search term
  """
  return get_argument("by")

def is_recursive():
  """
  Indicate that recursivity is enabled
  """
  return bool(get_argument('-recursive'))

def get_recursive_level():
  """
  Returns the max recursive level
  """
  MAX_LEVEL = 3
  level = get_argument('recursive-level')

  if level == None:
    return MAX_LEVEL

  return parse_int(level, MAX_LEVEL)

def get_file_match():
  """
  Returns the value of 'file-match' argument
  """
  return get_argument('file-match')

def get_file_dont_match():
  """
  Returns the value of 'file-dont-match' argument
  """
  return get_argument('file-dont-match')

def get_path_match():
  """
  Returns the value of 'path-match' argument
  """
  return get_argument('path-match')

def get_path_dont_match():
  """
  Returns the value of 'path-dont-match' argument
  """
  return get_argument('path-dont-match')

def get_jump():
  """
  Returns the quantity of ignored matches
  """
  jump = get_argument('jump')

  if jump == None:
    return 0

  return parse_int(jump)

def abstract_get_extension(argument):
  """
  Abstract the returns of 'except-extension' and 'only-extension'
  """
  extensions = get_argument(argument)

  if extensions == None:
    return []

  return extensions.split(",")

def get_except_extensions():
  """
  Returns the values of 'except-extension' argument
  """
  return abstract_get_extension('except-extension')

def get_only_extensions():
  """
  Returns the values of 'only-extension' argument
  """
  return abstract_get_extension('only-extension')

def get_max_file():
  """
  Returns the values of 'max-file' argument
  """
  return parse_int(get_argument('max-file'), None)
