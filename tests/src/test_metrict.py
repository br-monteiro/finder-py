import unittest
from src.metrict import Metric


class TestMetric(unittest.TestCase):

    def setUp(self):
        self.metric = Metric()

    def test_get_metrics(self):
        result = self.metric.get_metrics()
        self.assertTrue('lines_matches_count' in result)
        self.assertTrue('files_count' in result)
        self.assertTrue('skip_count' in result)

    def test_set_metric(self):
        self.metric.set_metric('test', 'ok')
        result = self.metric.get_metrics()
        self.assertTrue('test' not in result)
        self.assertFalse(self.metric.get_metric('ok', False))

        self.metric.set_metric('test', 7)
        result = self.metric.get_metrics()
        self.assertEqual(7, self.metric.get_metric('test'))

    def test_get_metric(self):
        self.assertEqual(0, self.metric.get_metric('files_count'))
        self.assertIsNone(self.metric.get_metric('whatever'))
        self.assertEqual('fallback', self.metric.get_metric('whatever', 'fallback'))

    def test_increment(self):
        self.assertIsNone(self.metric.get_metric('test'))
        self.metric.set_metric('test', 7)
        self.metric.increment('test')
        self.assertEqual(8, self.metric.get_metric('test'))
        self.metric.increment('test')
        self.metric.increment('test')
        self.assertEqual(10, self.metric.get_metric('test'))
        self.metric.increment('test-test')
        self.assertIsNone(self.metric.get_metric('test-test'))


if __name__ == "__main__":
    unittest.main()
