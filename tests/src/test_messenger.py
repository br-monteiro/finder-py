import re
import unittest
import src.messenger as messenger

class TestMessenger(unittest.TestCase):

  def setUp(self):
    self.text = "tests and 123 test"
    self.text_without_match = "tests and test"
    self.text_long = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. 123 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took 123 a galley"
    self.regex = re.compile("123")

  def test_highlight(self):
    expected = "tests and [BG-GREEN]123[ENDC] test"
    self.assertEqual(expected, messenger.highlight(self.regex, self.text))
    self.assertEqual(self.text_without_match, messenger.highlight(self.regex, self.text_without_match))
    self.assertEqual("", messenger.highlight(self.regex, ""))

  def test_compresstext(self):
    self.assertEqual("[YELLOW]...[ENDC]est", messenger.compresstext(self.text, 3))
    self.assertEqual("[YELLOW]...[ENDC]d 123 test", messenger.compresstext(self.text,10))
    self.assertEqual("", messenger.compresstext("", 10))
    self.assertEqual(self.text, messenger.compresstext(self.text, 18))
    self.assertEqual(100, messenger.compresstext(100, 18))
    self.assertIsNone(messenger.compresstext(None, 18))

  def test_processtext(self):
    self.assertEqual("[YELLOW]...[ENDC]pesetting industry. 123[YELLOW]...[ENDC]nknown printer took 123 a galley", messenger.processtext(self.regex, self.text_long))
    self.assertEqual(self.text, messenger.processtext(re.compile("Lorem Ipsum is"), self.text))
    self.assertEqual("Lorem Ipsum[YELLOW]...[ENDC]industry. 123 Lorem Ipsum[YELLOW]...[ENDC]er took 123 a galley", messenger.processtext(re.compile("Ipsum"), self.text_long))
    self.assertEqual("Lorem Ipsum is[YELLOW]...[ENDC]nown printer took 123 a galley", messenger.processtext(re.compile("Lorem Ipsum is"), self.text_long))
    self.assertEqual("", messenger.processtext(re.compile("Lorem Ipsum is"), ""))
    self.assertIsNone(messenger.processtext(re.compile("Lorem Ipsum is"), None))

if __name__ == "__main__":
  unittest.main()
