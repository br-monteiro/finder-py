import sys

arguments_map = {}

def process_arguments():
  """
  Process the arguments from CLI
  """
  arguments = {}
  for item in sys.argv:
    chunks = item.split('=')

    if len(chunks) == 2:
      chunks[0] = chunks[0].lower()
      arguments.update({
        chunks[0]: chunks[1]
      })
  return arguments

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
  arguments_map = process_arguments()
