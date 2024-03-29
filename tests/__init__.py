import unittest
import tests.src.test_cli as test_cli
import tests.src.test_disc_manager as test_disc_manager
import tests.src.test_params as test_params
import tests.src.test_utils as test_utils
import tests.src.test_messenger as test_messenger
import tests.src.test_colors as test_colors
import tests.src.test_metrict as test_metric


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_cli))
    suite.addTests(loader.loadTestsFromModule(test_disc_manager))
    suite.addTests(loader.loadTestsFromModule(test_params))
    suite.addTests(loader.loadTestsFromModule(test_utils))
    suite.addTests(loader.loadTestsFromModule(test_messenger))
    suite.addTests(loader.loadTestsFromModule(test_colors))
    suite.addTests(loader.loadTestsFromModule(test_metric))

    return suite
