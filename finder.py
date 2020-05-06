#!/usr/bin/python3
import src.match_engine as engine
from src.messenger import show_message, show_mectrics

if __name__ == "__main__":
  try:
    """
    Run the app
    """
    engine.run()

  except KeyboardInterrupt:
    show_message("[RED]Process interrupted by user[ENDC]")
