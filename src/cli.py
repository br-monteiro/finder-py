import sys
import re

arguments_map = {}

def process_arguments(raw_arguments: list):
  """
  Process the arguments from CLI. The value of sys.argv
  """
  arguments = {}
  for argument in raw_arguments:
    # catch the arguments with associated values
    matches = re.search(r'^([a-z][a-z0-9-]+?)=[\'"]?(.+?)[\'"]?$', argument)

    if matches:
      arg = matches.group(1).lower()
      value = matches.group(2)

      arguments.update({
        arg: value
      })
      continue

    # catch the simple arguments
    matches = re.search(r'^(-[a-z][a-z0-9-]*?)$', argument)
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
  return arguments_map

def get_argument(name: str):
  """
  Returns one argument from CLI by name
  If there is no argument, returns None
  """
  return arguments_map[name] if name in arguments_map else None

def set_argument(key, value):
  """
  Set a new value into 'arguments_map'
  """
  arguments_map.update({
    key: value
  })

if len(arguments_map) == 0:
  # process the arguments and populates the Dict arguments_map
  arguments_map = process_arguments(sys.argv[1:])
