import sys
import re

arguments_map = {}

def process_arguments(raw_arguments: list):
  """
  Process the arguments from CLI. The value of sys.argv
  """
  arguments = {}
  for argument in raw_arguments:
    matches = re.search(r'^(.+?)=[\'"]?(.+?)[\'"]?$', argument)

    if matches:
      arg = matches.group(1).lower()
      value = matches.group(2)

      arguments.update({
        arg: value
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
  if name in arguments_map:
    return arguments_map[name]
  return None

if len(arguments_map) == 0:
  # process the arguments and populates the Dict arguments_map
  arguments_map = process_arguments(sys.argv[1:])
