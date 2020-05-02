import unittest
import src.cli as cli

class TestCli(unittest.TestCase):

  def test_process_arguments(self):
    expected = {
      "test1": "testendjend =jndjend",
      "test2": "=jrfnrjfnjr",
      "test4": " teste"
    }
    arguments = cli.process_arguments([
      "test1='testendjend =jndjend'",
      "test2==jrfnrjfnjr",
      "test3=",
      " kndeknde",
      "test4=' teste'"
    ])

    self.assertEqual(arguments, expected)
    self.assertEqual(cli.get_arguments(), expected)

  def test_get_argument(self):
    cli.arguments_map = cli.process_arguments([
      "test1='testendjend =jndjend'",
      "test2==jrfnrjfnjr",
      "test3=",
      " kndeknde",
      "test4=' teste'"
    ])

    self.assertEqual("testendjend =jndjend", cli.get_argument("test1"))
    self.assertEqual("=jrfnrjfnjr", cli.get_argument("test2"))
    self.assertEqual(" teste", cli.get_argument("test4"))
    self.assertIsNone(cli.get_argument("test3"))

if __name__ == "__main__":
  unittest.main()
