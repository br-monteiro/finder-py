import unittest
import src.cli as cli

class TestCli(unittest.TestCase):

  def setUp(self):
    arguments = cli.process_arguments([
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
    cli.set_arguments(arguments)

  def tearDown(self):
    cli.clear_arguments()

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

  def test_set_argument(self):
    self.assertIsNone(cli.get_argument("-test"))
    cli.set_argument("-test", True)
    self.assertTrue(cli.get_argument("-test"))
    cli.set_argument("test2", "whatever")
    self.assertEqual("whatever", cli.get_argument("test2"))
    cli.set_argument("test2", "whatever-test")
    self.assertEqual("whatever-test", cli.get_argument("test2"))

  def test_clear_arguments(self):
    cli.set_argument("test-a", "a")
    cli.set_argument("-test-b", True)
    self.assertEqual("a", cli.get_argument("test-a"))
    self.assertTrue(cli.get_argument("-test-b"))
    cli.clear_arguments()
    self.assertIsNone(cli.get_argument("test-a"))
    self.assertIsNone(cli.get_argument("-test-b"))


if __name__ == "__main__":
  unittest.main()
