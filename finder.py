#!/usr/bin/python3
import time
import src.match_engine as engine
from src.messenger import show_message

if __name__ == '__main__':
  try:
    start_time = time.clock()
    """
    Run the app
    """
    engine.run()

    show_message("[RED]---[ENDC]")
    show_message("[GREEN][BOLD]{:.3f}".format(time.clock() - start_time) + "[ENDC] seconds")

  except KeyboardInterrupt:
    show_message("[RED]Process interrupted by user[ENDC]")
