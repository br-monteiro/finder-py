import unittest
import src.colors as colors

class TestColors(unittest.TestCase):

  def test_get_color(self):
    self.assertEqual("\033[32m", colors.get_color("[GREEN]"))
    self.assertEqual("\033[33m", colors.get_color("[YELLOW]"))
    self.assertEqual("\033[42m", colors.get_color("[BG-GREEN]"))
    self.assertEqual("\033[91m", colors.get_color("[RED]"))
    self.assertEqual("\033[0m", colors.get_color("[ENDC]"))
    self.assertEqual("\033[1m", colors.get_color("[BOLD]"))
    self.assertIsNone(colors.get_color("[WHATEVER]"))

if __name__ == "__main__":
  unittest.main()
