import re

def parse_int(value, fallback=0):
  """
  Convert a string number to integer
  """
  if value == None:
    return fallback

  try:
    return int(value)
  except ValueError:
    return fallback

def normalize_str(value: str):
  """
  Just remove unnecessary characters from value
  """
  if type(value) != str:
    return value

  return re.sub(r'\n', lambda m: '', value)