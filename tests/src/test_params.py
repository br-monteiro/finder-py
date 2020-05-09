import os
import unittest
import src.cli as cli
import src.params as params
from sys import argv

class TestParams(unittest.TestCase):

  def setUp(self):
    cli.arguments_map = cli.process_arguments([
      "by=test",
      "path=/home/user",
      "-recursive",
      "-quiet",
      "-raw",
      "recursive-level=5",
      "file-match=\\w+",
      "file-dont-match=123",
      "path-match=\\w+",
      "path-dont-match=123",
      "except-extension=php,java",
      "only-extension=js,py"
    ])

  def tearDown(self):
    cli.clear_arguments()

  def test_get_by(self):
    self.assertEqual("test", params.get_by())
    cli.clear_arguments()
    self.assertIsNone(params.get_by())

  def test_get_argument(self):
    self.assertEqual("/home/user/", params.get_path())
    cli.clear_arguments()
    path = os.getcwd() + "/"
    self.assertEqual(path, params.get_path())

  def test_is_recursive(self):
    self.assertTrue(params.is_recursive())
    cli.clear_arguments()
    cli.set_argument("-r", True)
    self.assertTrue(params.is_recursive())
    cli.clear_arguments()
    self.assertFalse(params.is_recursive())

  def test_get_recursive_level(self):
    self.assertEqual(5, params.get_recursive_level())
    cli.clear_arguments()
    self.assertEqual(3, params.get_recursive_level())
    cli.set_argument("recursive-level", 7)
    self.assertEqual(7, params.get_recursive_level())
    cli.set_argument("recursive-level", "abc")
    self.assertEqual(3, params.get_recursive_level())
    cli.clear_arguments()
    cli.set_argument("rl", 77)
    self.assertEqual(77, params.get_recursive_level())

  def test_get_file_match(self):
    self.assertEqual("\\w+", params.get_file_match())
    cli.clear_arguments()
    self.assertIsNone(params.get_file_match())
    cli.set_argument("fm", "*-test-*")
    self.assertEqual("*-test-*", params.get_file_match())

  def test_get_file_dont_match(self):
    self.assertEqual("123", params.get_file_dont_match())
    cli.clear_arguments()
    self.assertIsNone(params.get_file_dont_match())
    cli.set_argument("fdm", "*-test-*")
    self.assertEqual("*-test-*", params.get_file_dont_match())

  def test_get_path_match(self):
    self.assertEqual("\\w+", params.get_path_match())
    cli.clear_arguments()
    self.assertIsNone(params.get_path_match())
    cli.set_argument("pm", "*-test-*")
    self.assertEqual("*-test-*", params.get_path_match())

  def test_get_path_dont_match(self):
    self.assertEqual("123", params.get_path_dont_match())
    cli.clear_arguments()
    self.assertIsNone(params.get_path_dont_match())
    cli.set_argument("pdm", "*-test-*")
    self.assertEqual("*-test-*", params.get_path_dont_match())

  def test_get_except_extensions(self):
    self.assertEqual(["php", "java"], params.get_except_extensions())
    cli.clear_arguments()
    self.assertEqual([], params.get_except_extensions())
    cli.set_argument("ee", "json,md")
    self.assertEqual(["json", "md"], params.get_except_extensions())

  def test_get_only_extensions(self):
    self.assertEqual(["js", "py"], params.get_only_extensions())
    cli.clear_arguments()
    self.assertEqual([], params.get_only_extensions())
    cli.set_argument("oe", "php,html")
    self.assertEqual(["php", "html"], params.get_only_extensions())

  def test_is_quiet(self):
    self.assertTrue(params.is_quiet())
    cli.clear_arguments()
    cli.set_argument("-q", True)
    self.assertTrue(params.is_quiet())
    cli.clear_arguments()
    self.assertFalse(params.is_quiet())

  def test_is_raw(self):
    self.assertTrue(params.is_raw())
    cli.set_argument("-raw", True)
    self.assertTrue(params.is_raw())
    cli.clear_arguments()
    self.assertFalse(params.is_raw())

  def test_is_help(self):
    if argv.count('-v'):
      argv.remove('-v')
    self.assertFalse(params.is_help())
    argv.append("--help")
    self.assertTrue(params.is_help())


if __name__ == "__main__":
  unittest.main()
