import os
import codecs
from src.utils import normalize_str

def get_list_dir(path: str):
  """
  Returns a list of file name from the rirectory passed by parameter
  """
  if is_directory(path) == False:
    return []
  return list(map(lambda item: add_end_slash(path) + item, os.listdir(path)))

def add_end_slash(value: str):
  """
  Added a slash at the end of value
  """
  if type(value) != str:
    return value

  return value if value.endswith("/") else value + "/"

def is_directory(path: str):
  """
  Checks if the path is a readable directory
  """
  return os.path.isdir(path) and is_readable(path)

def is_file(path: str):
  """
  Checks if the path is a readable file
  """
  return os.path.isfile(path) and is_readable(path)

def is_readable(path: str):
  """
  Checks if the path is a readable source
  """
  return os.access(path=path, mode=os.R_OK)

def load_file(path: str):
  """
  Reads a file and returns its contents as List
  If the file is not readable, returns an empty List
  """
  content = []

  if is_file(path) == False:
    return content

  file = codecs.open(path, "r",  encoding="utf-8", errors="ignore")

  for line in file:
    content.append(normalize_str(line))
  file.close()

  return content

def get_file_name_from(path: str):
  """
  Extract the file name and return it
  """
  if type(path) != str:
    return ""
  chunks = path.split("/")
  return chunks[-1]
