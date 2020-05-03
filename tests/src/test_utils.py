import unittest
import src.utils as utils

class TestUtils(unittest.TestCase):

  def test_parse_int(self):
    self.assertEqual(2, utils.parse_int('2'))
    self.assertEqual(2, utils.parse_int('02'))
    self.assertEqual(-2, utils.parse_int('-2'))
    self.assertEqual(0, utils.parse_int('--2'))
    self.assertEqual(0, utils.parse_int('abc'))
    self.assertEqual(True, utils.parse_int('abc', True))
    self.assertEqual(None, utils.parse_int('abc', None))
    self.assertEqual(False, utils.parse_int('', False))
    self.assertEqual(False, utils.parse_int(None, False))

if __name__ == "__main__":
  unittest.main()
