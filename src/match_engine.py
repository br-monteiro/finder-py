import re
import src.params as params
from src.utils import extract_extension, pattern_test
from src.messenger import show_message, print_matches
from src.disc_manager import is_directory, is_file, get_list_dir, load_file

def discoverer(regex, path, level=0):
  """
  Scout the current path and fire the 'regex' into files
  """
  if is_directory(path):
    recursive_level = params.get_recursive_level()

    for current_path in get_list_dir(path):
      """
      Fire the all filter agurments

      A wizard is never late, nor is he early,
      He arrives precisely when he means to! - Gandalf
      """
      if you_shall_not_pass(current_path):
        continue

      """
      Release the Kraken
      """
      if is_file(current_path):
        search_in_file(regex, current_path)

      elif is_directory(current_path) and params.is_recursive() and level < recursive_level:
        discoverer(regex, current_path, level + 1)

def search_in_file (regex, path):
  """
  Search the term with 'regex' in file of 'path'
  """
  file_content = load_file(path)
  current_path = None

  for (index, line) in enumerate(file_content):
    if regex.search(line):
      """
      print the path of file
      """
      if current_path != path:
        current_path = path
        show_message("[GREEN]" + path + "[ENDC]")

      print_matches(regex, str(index + 1), line)

def is_path_match(path):
  """
  Checks if a value was entered in the argument 'path-match'
  In case of success, fire the pattern in current 'path'
  """
  path_match = params.get_path_match()

  if not path_match:
    return True

  return pattern_test(path_match, path)

def is_path_dont_match(path):
  """
  Checks if a value was entered in the argument 'path-dont-match'
  In case of success, fire the pattern in current 'path'
  """
  path_dont_match = params.get_path_dont_match()

  if not path_dont_match:
    return False

  return pattern_test(path_dont_match, path)

def is_file_match(path):
  """
  Checks if a value was entered in the argument 'file-match'
  In case of success, fire the pattern in current 'path'
  """
  file_match = params.get_file_match()

  if not file_match:
    return True

  return pattern_test(file_match, path)

def is_file_dont_match(path):
  """
  Checks if a value was entered in the argument 'file-dont-match'
  In case of success, fire the pattern in current 'path'
  """
  file_dont_match = params.get_file_dont_match()

  if not file_dont_match:
    return False

  return pattern_test(file_dont_match, path)

def you_shall_not_pass(current_path):
  """
  Check the value of 'path-dont-match'
  If the path is not allowed, then continue the loop
  """
  if is_path_dont_match(current_path):
    return True

  """
  Check the value of 'path-match'
  If the path is not allowed, then continue the loop
  """
  if is_path_match(current_path) == False:
    return True

  if is_file(current_path):
    file_extension = extract_extension(current_path)

    """
    Check the value of 'file-dont-match'
    If the path is not allowed, then continue the loop
    """
    if is_file_dont_match(current_path):
      return True

    """
    Check the value of 'file-match'
    If the path is not allowed, then continue the loop
    """
    if is_file_match(current_path) == False:
      return True

    """
    Check if the file has a allowed extension
    """
    only_extension = params.get_only_extensions()
    if len(only_extension) > 0 and file_extension not in only_extension:
      return True

    """
    Check if the file has a allowed extension
    """
    except_extension = params.get_except_extensions()
    if len(except_extension) > 0 and file_extension in except_extension:
      return True
  return False

def run():
  """
  Fire the chaos
  From this point, you're lost
  """
  term = params.get_by()

  if term:
    regexTerm = re.compile(term)
    path = params.get_path()
    discoverer(regexTerm, path)

  else:
    show_message("[RED]you need to enter a search term[ENDC]")
    show_message("[GREEN]finder by=[YELLOW]<term>[ENDC]")
