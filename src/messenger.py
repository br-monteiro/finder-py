import re
import time
from src.colors import get_colors
from src.utils import parse_int
from src.params import is_quiet

def show_message(text: str):
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
  text = highlight(regex, process_text(regex, line_content))
  show_message("[YELLOW][BOLD]" + line_number + "[ENDC] " + text)

def highlight(regex, value):
  """
  Highlights the text found
  """
  return regex.sub(lambda m: "[BG-GREEN]" + m.group(0) + "[ENDC]", value)

def process_text(regex, value):
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

    wrapper_text = list(map(lambda text: compress_text(text, wrap_length), regex.split(value)))
    return regex.search(value).group(0).join(wrapper_text)

  return value

def compress_text(text, length):
  """
  Compress long text to show on the screen
  """
  if type(text) != str:
    return text

  if len(text) > parse_int(length):
    compiled_regex = re.compile("(.{" + str(length) + "}?)$")
    match = compiled_regex.search(text)
    if match:
      return "[YELLOW]...[ENDC]" + match.group(1)

  return text

def show_mectrics(metrics):
  """
  Print the metrics of time execution, matches and skip on the screen
  """
  if is_quiet() == False:
    show_message("[RED]---[ENDC]")
    s = " [RED]|[ENDC] " # it's just a separator
    process_time = "[GREEN][BOLD]{:.3f}".format(time.time() - metrics["start_time"]) + "[ENDC] seconds"
    files_count = "[GREEN][BOLD]" + str(metrics["files_count"]) + "[ENDC] files"
    lines_matches_count = "[GREEN][BOLD]" + str(metrics["lines_matches_count"]) + "[ENDC] lines matches"
    skip_count = "[GREEN][BOLD]" + str(metrics["skip_count"]) + "[ENDC] skip"

    show_message(process_time + s + files_count + s + lines_matches_count + s + skip_count)
