import re

def parseint(value, fallback=0):
  """
  Convert a string number to integer
  """
  if value == None:
    return fallback

  try:
    return int(value)
  except ValueError:
    return fallback

def normalizestr(value: str):
  """
  Just remove unnecessary characters from value
  """
  if type(value) != str:
    return value

  return re.sub(r"\n", lambda m: "", value)

def get_ext(path: str):
  """
  Returns the file extension, otherwise return None
  """
  if type(path) != str:
    return None

  value_regex = re.compile("\.([\w\d]+?)$")
  matches = value_regex.search(path)
  return matches.group(1) if matches else None

def re_test(pattern: str, value: str):
  """
  Just fire the pattern in value and return a boolean
  """
  if type(pattern) != str or type(value) != str:
    return False

  value_regex = re.compile(pattern)
  return bool(value_regex.search(value))
