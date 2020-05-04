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

  def test_normalize_str(self):
    self.assertEqual("abc", utils.normalize_str("abc\n"))
    self.assertEqual("abcabc", utils.normalize_str("abc\nabc"))
    self.assertIsNone(utils.normalize_str(None))
    self.assertTrue(utils.normalize_str(True))
    self.assertFalse(utils.normalize_str(False))

if __name__ == "__main__":
  unittest.main()
