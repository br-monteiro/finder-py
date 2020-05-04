import re
from src.colors import get_colors
from src.utils import parse_int

def show_message(text: str):
  """
  Prints the messages on screen
  """
  colored_text = text

  for name, color in get_colors().items():
    regexColor = re.compile(re.escape(name))
    colored_text = re.sub(regexColor, lambda i: color, colored_text)

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
      return "..." + match.group(1)

  return text
