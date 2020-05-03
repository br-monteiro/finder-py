import unittest
import src.cli as cli

class TestCli(unittest.TestCase):

  def setUp(self):
    cli.arguments_map = cli.process_arguments([
      "test1='value =2'",
      "Test1='whatever",
      "test2==value",
      "-test2==whatever",
      "2test2==whatever",
      "test-quotes=\"value\"",
      "test3=",
      "test4=' value'",
      " kndeknde",
      "-test1",
      "-Test4",
      "-1test",
    ])

  def tearDown(self):
    cli.arguments_map = {}

  def test_process_arguments(self):
    expected = {
      "test-quotes": "value",
      "test1": "value =2",
      "test2": "=value",
      "test4": " value",
      "-test1": True
    }

    self.assertEqual(cli.get_arguments(), expected)

  def test_get_argument(self):
    self.assertEqual("value =2", cli.get_argument("test1"))
    self.assertEqual("=value", cli.get_argument("test2"))
    self.assertEqual(" value", cli.get_argument("test4"))
    self.assertIsNone(cli.get_argument("test3"))
    self.assertIsNone(cli.get_argument("-test3"))
    self.assertTrue(cli.get_argument("-test1"))

if __name__ == "__main__":
  unittest.main()
