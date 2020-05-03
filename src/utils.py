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
