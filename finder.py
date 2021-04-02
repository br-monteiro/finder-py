#!/usr/bin/python3
import src.match_engine as engine
from src.messenger import message

if __name__ == "__main__":
    try:
        # Run the app
        engine.run()

    except KeyboardInterrupt:
        message("[RED]Process interrupted by user[ENDC]")
