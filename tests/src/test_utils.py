import unittest
import src.utils as utils

class TestUtils(unittest.TestCase):

  def test_parseint(self):
    self.assertEqual(2, utils.parseint("2"))
    self.assertEqual(2, utils.parseint("02"))
    self.assertEqual(-2, utils.parseint("-2"))
    self.assertEqual(0, utils.parseint("--2"))
    self.assertEqual(0, utils.parseint("abc"))
    self.assertEqual(True, utils.parseint("abc", True))
    self.assertEqual(None, utils.parseint("abc", None))
    self.assertEqual(False, utils.parseint("", False))
    self.assertEqual(False, utils.parseint(None, False))

  def test_normalizestr(self):
    self.assertEqual("abc", utils.normalizestr("abc\n"))
    self.assertEqual("abcabc", utils.normalizestr("abc\nabc"))
    self.assertIsNone(utils.normalizestr(None))
    self.assertTrue(utils.normalizestr(True))
    self.assertFalse(utils.normalizestr(False))

  def test_get_ext(self):
    self.assertEqual("py", utils.get_ext("main.py"))
    self.assertEqual("gz", utils.get_ext("file.tar.gz"))
    self.assertIsNone(utils.get_ext("index.-js"))
    self.assertIsNone(utils.get_ext("index.-"))
    self.assertIsNone(utils.get_ext("index."))
    self.assertIsNone(utils.get_ext(""))
    self.assertIsNone(utils.get_ext(None))

  def test_re_test(self):
    self.assertTrue(utils.re_test("\d", "123"))
    self.assertFalse(utils.re_test("\d", "abc"))
    self.assertFalse(utils.re_test(None, "123"))
    self.assertFalse(utils.re_test("\d", None))

if __name__ == "__main__":
  unittest.main()
