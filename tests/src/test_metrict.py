import unittest
from src.metrict import Metric

class TestMetrict(unittest.TestCase):

  def setUp(self):
    self.mtrc = Metric()

  def test_get_metricts(self):
    result = self.mtrc.get_metrics()
    self.assertTrue('lines_matches_count' in result)
    self.assertTrue('files_count' in result)
    self.assertTrue('skip_count' in result)

  def test_set_metrict(self):
    self.mtrc.set_metrict('test', 'ok')
    result = self.mtrc.get_metrics()
    self.assertTrue('test' not in result)
    self.assertFalse(self.mtrc.get_metric('ok', False))

    self.mtrc.set_metrict('test', 7)
    result = self.mtrc.get_metrics()
    self.assertEqual(7, self.mtrc.get_metric('test'))

  def test_get_metrict(self):
    self.assertEqual(0, self.mtrc.get_metric('files_count'))
    self.assertIsNone(self.mtrc.get_metric('whatever'))
    self.assertEqual('fallback', self.mtrc.get_metric('whatever', 'fallback'))

  def test_increment(self):
    self.assertIsNone(self.mtrc.get_metric('test'))
    self.mtrc.set_metrict('test', 7)
    self.mtrc.increment('test')
    self.assertEqual(8, self.mtrc.get_metric('test'))
    self.mtrc.increment('test')
    self.mtrc.increment('test')
    self.assertEqual(10, self.mtrc.get_metric('test'))
    self.mtrc.increment('test-test')
    self.assertIsNone(self.mtrc.get_metric('test-test'))

if __name__ == "__main__":
  unittest.main()
