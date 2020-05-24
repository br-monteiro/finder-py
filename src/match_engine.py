import re
import src.params as params
from src.metrict import Metric
from time import time
from src.messenger import message, print_matches, show_mectrics, help_
from src.disc_manager import isdirectory, isfile, get_listdir, loadfile
from src.skiprules import you_shall_not_pass

def discoverer(regex, path, level=0, metric:Metric = None):
  """
  Scout the current path and fire the 'regex' into files
  """
  if isdirectory(path):
    recursive_level = params.get_recursive_level()

    for current_path in get_listdir(path):
      """
      Increment files metrics
      """
      if isfile(current_path):
        metric.increment("files_count")
      """
      A wizard is never late, nor is he early,
      He arrives precisely when he means to! - Gandalf
      """
      if you_shall_not_pass(current_path):
        """
        Increment 'skip' metric
        """
        metric.increment("skip_count")
        continue

      """
      Release the Kraken
      """
      if isfile(current_path):
        search_in_file(regex, current_path, metric)

      elif isdirectory(current_path) and params.isrecursive() and level < recursive_level:
        discoverer(regex, current_path, level + 1, metric)

def search_in_file (regex, path, metric: Metric = None):
  """
  Search the term with 'regex' in file of 'path'
  """
  file_content = loadfile(path)
  current_path = None

  for (index, line) in enumerate(file_content):
    if regex.search(line):
      """
      Increment 'matches' metric
      """
      metric.increment("lines_matches_count")
      """
      print the path of file
      """
      if current_path != path:
        current_path = path
        message("[GREEN]" + path + "[ENDC]")

      print_matches(regex, str(index + 1), line)

def run():
  """
  Fire the chaos
  From this point, you're lost
  """
  if params.ishelp():
    help_()
    return # just stop the execution

  term = params.get_by()

  if term:
    """
    Escape the search term when 'raw' argument is informed
    """
    if params.israw():
      term = re.escape(term)

    mtrc = Metric()
    regex_term = re.compile(term)
    discoverer(regex_term, params.get_path(), 0, mtrc)
    show_mectrics(mtrc)

  else:
    message("[RED]you need to enter a search term[ENDC]")
    message("[GREEN]finder [YELLOW]--help[ENDC]")
