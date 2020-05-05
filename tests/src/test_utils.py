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

  def test_extract_extension(self):
    self.assertEqual("py", utils.extract_extension("main.py"))
    self.assertEqual("gz", utils.extract_extension("file.tar.gz"))
    self.assertIsNone(utils.extract_extension("index.-js"))
    self.assertIsNone(utils.extract_extension("index.-"))
    self.assertIsNone(utils.extract_extension("index."))
    self.assertIsNone(utils.extract_extension(""))
    self.assertIsNone(utils.extract_extension(None))

  def test_pattern_test(self):
    self.assertTrue(utils.pattern_test("\d", "123"))
    self.assertFalse(utils.pattern_test("\d", "abc"))
    self.assertFalse(utils.pattern_test(None, "123"))
    self.assertFalse(utils.pattern_test("\d", None))

if __name__ == "__main__":
  unittest.main()
