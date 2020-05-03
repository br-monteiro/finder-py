import os
import unittest
import src.disc_manager as disc_manager

class TestDiscManager(unittest.TestCase):

  def setUp(self):
    self.path = os.getcwd() + "/tests/list-dir-test"

  def tearDown(self):
    self.path = None

  def test_get_list_dir(self):
    expected = [
      self.path + "/one-dir",
      self.path + "/test.txt",
      self.path + "/other-test.txt"
    ]
    self.assertEqual(expected, disc_manager.get_list_dir(self.path))

  def test_add_slash(self):
    self.assertEqual("/", disc_manager.add_end_slash(""))
    self.assertEqual("/", disc_manager.add_end_slash("/"))
    self.assertEqual("/test/", disc_manager.add_end_slash("/test"))
    self.assertEqual("/test/", disc_manager.add_end_slash("/test/"))

  def test_is_directory(self):
    self.assertTrue(disc_manager.is_directory(self.path + "/one-dir"))
    self.assertFalse(disc_manager.is_directory(self.path + "/test.txt"))
    self.assertFalse(disc_manager.is_directory("/root"))
    self.assertFalse(disc_manager.is_directory("/root/whatever"))

  def test_is_file(self):
    self.assertFalse(disc_manager.is_file(self.path + "/one-dir"))
    self.assertTrue(disc_manager.is_file(self.path + "/test.txt"))
    self.assertFalse(disc_manager.is_file("/root"))
    self.assertFalse(disc_manager.is_file("/root/.profile"))

  def test_is_readable(self):
    self.assertTrue(disc_manager.is_readable(self.path + "/one-dir"))
    self.assertTrue(disc_manager.is_readable(self.path + "/test.txt"))
    self.assertFalse(disc_manager.is_readable("/root"))
    self.assertFalse(disc_manager.is_readable("/root/whatever"))

  def test_load_file(self):
    expected = ["simple test\n", "second line"]
    self.assertEqual(expected, disc_manager.load_file(self.path + "/test.txt"))
    self.assertEqual([], disc_manager.load_file("/whatever.txt"))
    self.assertEqual([], disc_manager.load_file(""))

if __name__ == "__main__":
  unittest.main()
