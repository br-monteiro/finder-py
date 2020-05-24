import os
import codecs
from src.utils import normalizestr

def get_listdir(path: str):
  """
  Returns a list of file name from the rirectory passed by parameter
  """
  if isdirectory(path) == False:
    return []
  return list(map(lambda item: addendslash(path) + item, os.listdir(path)))

def addendslash(value: str):
  """
  Added a slash at the end of value
  """
  if type(value) != str:
    return value

  return value if value.endswith("/") else value + "/"

def isdirectory(path: str):
  """
  Checks if the path is a readable directory
  """
  return os.path.isdir(path) and isreadable(path)

def isfile(path: str):
  """
  Checks if the path is a readable file
  """
  return os.path.isfile(path) and isreadable(path)

def isreadable(path: str):
  """
  Checks if the path is a readable source
  """
  return os.access(path=path, mode=os.R_OK)

def loadfile(path: str):
  """
  Reads a file and returns its contents as List
  If the file is not readable, returns an empty List
  """
  content = []

  if isfile(path) == False:
    return content

  file = codecs.open(path, "r",  encoding="utf-8", errors="ignore")

  for line in file:
    content.append(normalizestr(line))
  file.close()

  return content

def get_filename(path: str):
  """
  Extract the file name and return it
  """
  if type(path) != str:
    return ""
  chunks = path.split("/")
  return chunks[-1]
