import re
import time
from src.colors import get_colors
from src.utils import parseint
from src.params import isquiet

def message(text: str):
  """
  Prints the messages on screen
  """
  colored_text = text

  for name, color in get_colors().items():
    regex_color = re.compile(re.escape(name))
    colored_text = re.sub(regex_color, lambda i: color, colored_text)

  print(colored_text)

def print_matches(regex, line_number, line_content):
  """
  Prints the line of file with matches
  """
  text = highlight(regex, processtext(regex, line_content))
  message("[YELLOW][BOLD]" + line_number + "[ENDC] " + text)

def highlight(regex, value):
  """
  Highlights the text found
  """
  return regex.sub(lambda m: "[BG-GREEN]" + m.group(0) + "[ENDC]", value)

def processtext(regex, value):
  """
  Process the text to pretty presentation
  """
  if value and len(value) > 50:
    wrap_length = 30
    matches_length = len(regex.findall(value))

    if matches_length > 1:
      wrap_length = 20
    elif matches_length == 2:
      wrap_length = 10
    elif matches_length >= 3:
      wrap_length = 5

    wrapper_text = list(map(lambda text: compresstext(text, wrap_length), regex.split(value)))
    return regex.search(value).group(0).join(wrapper_text)

  return value

def compresstext(text, length):
  """
  Compress long text to show on the screen
  """
  if type(text) != str:
    return text

  if len(text) > parseint(length):
    compiled_regex = re.compile("(.{" + str(length) + "}?)$")
    match = compiled_regex.search(text)
    if match:
      return "[YELLOW]...[ENDC]" + match.group(1)

  return text

def show_mectrics(metric):
  """
  Print the metrics of time execution, matches and skip on the screen
  """
  if isquiet() == False:
    message("[RED]---[ENDC]")
    s = " [RED]|[ENDC] " # it's just a separator
    time_ = "[GREEN][BOLD]{:.3f}[ENDC] seconds".format(time.time() - metric.get_metric("start_time", 0))
    files = "[GREEN][BOLD]{}[ENDC] files".format(metric.get_metric("files_count"))
    lines = "[GREEN][BOLD]{}[ENDC] lines matches".format(metric.get_metric("lines_matches_count"))
    skip = "[GREEN][BOLD]{}[ENDC] skip".format(metric.get_metric("skip_count"))
    text = "{time_}{s}{file}{s}{line}{s}{skip}".format(s=s, time_=time_, file=files, line=lines, skip=skip)

    message(text)

def help_():
  """
  Shows the commands descriptions
  """
  from os import path
  from src.disc_manager import loadfile

  file = loadfile(path.dirname(__file__) + "/../help_splash.txt")
  content = "\n".join(file) if file else ""
  message(content)
