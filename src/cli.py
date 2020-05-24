import sys
import re

_arguments_map = {}

def process_arguments(raw_arguments: list):
  """
  Process the arguments from CLI. The value of sys.argv
  """
  arguments = {}
  for argument in raw_arguments:
    # catch the arguments with associated values
    matches = re.search(r"^([a-z][a-z0-9-]+?)=['\"]?(.+?)['\"]?$", argument)

    if matches:
      arg = matches.group(1).lower()
      value = matches.group(2)

      arguments.update({
        arg: value
      })
      continue

    # catch the simple arguments
    matches = re.search(r"^(-[a-z][a-z0-9-]*?)$", argument)
    if matches:
      arg = matches.group(1)
      arguments.update({
        arg: True
      })
  return arguments

def get_arguments():
  """
  Returns the Arguments Map values
  """
  global _arguments_map
  return _arguments_map

def get_argument(name: str):
  """
  Returns one argument from CLI by name
  If there is no argument, returns None
  """
  global _arguments_map
  return _arguments_map[name] if name in _arguments_map else None

def set_argument(key, value):
  """
  Set a new value into '_arguments_map'
  """
  global _arguments_map
  _arguments_map.update({
    key: value
  })

def clear_arguments():
  """
  Clear all arguments from '_arguments_map'
  """
  set_arguments({})

def set_arguments(arguments: dict):
  global _arguments_map
  _arguments_map = arguments

if len(_arguments_map) == 0:
  # process the arguments and populates the Dict _arguments_map
  set_arguments(process_arguments(sys.argv[1:]))
