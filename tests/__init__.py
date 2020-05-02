import unittest
import tests.src.test_cli as test_cli

def load_tests(loader, tests, pattern):
  suite = unittest.TestSuite()
  suite.addTests(loader.loadTestsFromModule(test_cli))

  return suite
