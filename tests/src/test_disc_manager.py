import os
import unittest
import src.disc_manager as disc_manager


class TestDiscManager(unittest.TestCase):

    def setUp(self):
        self.path = os.getcwd() + "/tests/list-dir-test"

    def tearDown(self):
        self.path = None

    def test_get_listdir(self):
        expected = [
            self.path + "/other-test.txt",
            self.path + "/test.txt",
            self.path + "/one-dir"
        ]

        self.assertEqual(expected, disc_manager.get_listdir(self.path))
        self.assertEqual([], disc_manager.get_listdir(self.path + "/whatever"))
        self.assertEqual([], disc_manager.get_listdir(self.path + "/test.txt"))
        self.assertEqual([], disc_manager.get_listdir("/whatever"))
        self.assertEqual([], disc_manager.get_listdir(""))

    def test_add_slash(self):
        self.assertEqual("/", disc_manager.add_end_slash(""))
        self.assertEqual("/", disc_manager.add_end_slash("/"))
        self.assertEqual("/test/", disc_manager.add_end_slash("/test"))
        self.assertEqual("/test/", disc_manager.add_end_slash("/test/"))
        self.assertIsNone(disc_manager.add_end_slash(None))
        self.assertTrue(disc_manager.add_end_slash(True))
        self.assertFalse(disc_manager.add_end_slash(False))

    def test_is_directory(self):
        self.assertTrue(disc_manager.is_directory(self.path + "/one-dir"))
        self.assertFalse(disc_manager.is_directory(self.path + "/test.txt"))
        self.assertFalse(disc_manager.is_directory("/root"))
        self.assertFalse(disc_manager.is_directory("/root/whatever"))

    def test_isfile(self):
        self.assertFalse(disc_manager.isfile(self.path + "/one-dir"))
        self.assertTrue(disc_manager.isfile(self.path + "/test.txt"))
        self.assertFalse(disc_manager.isfile("/root"))
        self.assertFalse(disc_manager.isfile("/root/.profile"))

    def test_isreadable(self):
        self.assertTrue(disc_manager.isreadable(self.path + "/one-dir"))
        self.assertTrue(disc_manager.isreadable(self.path + "/test.txt"))
        self.assertFalse(disc_manager.isreadable("/root"))
        self.assertFalse(disc_manager.isreadable("/root/whatever"))

    def test_loadfile(self):
        expected = ["simple test", "second line"]
        self.assertEqual(expected, disc_manager.loadfile(self.path + "/test.txt"))
        self.assertEqual([], disc_manager.loadfile("/whatever.txt"))
        self.assertEqual([], disc_manager.loadfile(""))

    def test_get_filename(self):
        self.assertEqual("", disc_manager.get_filename(False))
        self.assertEqual("", disc_manager.get_filename(True))
        self.assertEqual("", disc_manager.get_filename(None))
        self.assertEqual("", disc_manager.get_filename("/"))
        self.assertEqual("", disc_manager.get_filename(""))
        self.assertEqual("test.txt", disc_manager.get_filename("/test.txt"))
        self.assertEqual("test.txt", disc_manager.get_filename("lll/test.txt"))
        self.assertEqual("test.txt", disc_manager.get_filename("test.txt"))


if __name__ == "__main__":
    unittest.main()
