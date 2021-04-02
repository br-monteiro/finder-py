from time import time


class Metric:

    def __init__(self):
        self._metrics = {
            "lines_matches_count": 0,
            "files_count": 0,
            "skip_count": 0,
            "start_time": time()
        }

    def get_metrics(self):
        """ Returns the all Dict of metrics """
        return self._metrics

    def set_metric(self, name, value):
        """ Set a new value to a metric. If there's no metric, create the entry on Dict """
        if isinstance(name, str) and isinstance(value, int):
            self._metrics.update({
                name: value
            })

    def get_metric(self, name, fallback=None):
        """ Returns the value of metric. In fail case, returns the fallback value """
        return self._metrics[name] if name in self._metrics else fallback

    def increment(self, name):
        """ Increment the value of a metrics """
        if name in self._metrics:
            self._metrics[name] += 1
