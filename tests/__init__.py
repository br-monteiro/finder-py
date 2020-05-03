import unittest
import tests.src.test_cli as test_cli
import tests.src.test_disc_manager as test_disc_manager

def load_tests(loader, tests, pattern):
  suite = unittest.TestSuite()
  suite.addTests(loader.loadTestsFromModule(test_cli))
  suite.addTests(loader.loadTestsFromModule(test_disc_manager))

  return suite
