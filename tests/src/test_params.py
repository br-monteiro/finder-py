import os
import unittest
import src.cli as cli
import src.params as params

class TestParams(unittest.TestCase):

  def setUp(self):
    cli.arguments_map = cli.process_arguments([
      "by=test",
      "path=/home/user",
      "-regex",
      "-recursive",
      "max-recursive-level=5",
      "file-match=\\w+",
      "file-dont-match=123",
      "jump=3",
      "except-extension=php,java",
      "only-extension=js,py",
      "max-file=4",
    ])

  def tearDown(self):
    cli.arguments_map = {}

  def test_get_by(self):
    self.assertEqual("test", params.get_by())
    cli.arguments_map = {}
    self.assertIsNone(params.get_by())

  def test_get_argument(self):
    self.assertEqual("/home/user/", params.get_path())
    cli.arguments_map = {}
    path = os.getcwd() + "/"
    self.assertEqual(path, params.get_path())

  def test_is_regex(self):
    self.assertTrue(params.is_regex())
    cli.arguments_map = {}
    self.assertFalse(params.is_regex())

  def test_is_recursive(self):
    self.assertTrue(params.is_recursive())
    cli.arguments_map = {}
    self.assertFalse(params.is_recursive())

  def test_get_recursive_level(self):
    self.assertEqual(5, params.get_recursive_level())
    cli.arguments_map = {}
    self.assertEqual(3, params.get_recursive_level())
    cli.arguments_map = {
      "max-recursive-level": "abc"
    }
    self.assertEqual(3, params.get_recursive_level())

  def test_get_file_match(self):
    self.assertEqual("\\w+", params.get_file_match())
    cli.arguments_map = {}
    self.assertIsNone(params.get_file_match())

  def test_get_file_dont_match(self):
    self.assertEqual("123", params.get_file_dont_match())
    cli.arguments_map = {}
    self.assertIsNone(params.get_file_dont_match())

  def test_get_jump(self):
    self.assertEqual(3, params.get_jump())
    cli.arguments_map = {}
    self.assertEqual(0, params.get_jump())

  def test_get_except_extensions(self):
    self.assertEqual(["php", "java"], params.get_except_extensions())
    cli.arguments_map = {}
    self.assertEqual([], params.get_except_extensions())

  def test_get_only_extensions(self):
    self.assertEqual(["js", "py"], params.get_only_extensions())
    cli.arguments_map = {}
    self.assertEqual([], params.get_only_extensions())

  def test_get_max_file(self):
    self.assertEqual(4, params.get_max_file())
    cli.arguments_map = {}
    self.assertIsNone(params.get_max_file())

if __name__ == "__main__":
  unittest.main()
