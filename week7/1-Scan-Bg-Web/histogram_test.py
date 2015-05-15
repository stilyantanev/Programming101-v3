import unittest
from histogram import Histogram


class HistogramTest(unittest.TestCase):

    def setUp(self):
        self.server_histogram = Histogram()

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.server_histogram, Histogram))

    def test_valid_members(self):
        self.assertEqual(self.server_histogram.dictionary, {})

    def test_add_existing_element(self):
        self.server_histogram.dictionary["Apache"] = 99
        self.server_histogram.add("Apache")
        self.assertEqual(self.server_histogram.dictionary["Apache"], 100)

    def test_add_non_existing_element(self):
        self.server_histogram.add("Microsoft-IIS")
        self.server_histogram.add("Microsoft-IIS")
        self.server_histogram.add("Microsoft-IIS")
        self.assertEqual(self.server_histogram.dictionary["Microsoft-IIS"], 3)

    def test_count_non_existing_element(self):
        self.assertEqual(self.server_histogram.count("nginx"), None)

    def test_count_existing_element(self):
        self.server_histogram.dictionary["nginx"] = 200
        self.assertEqual(self.server_histogram.count("nginx"), 200)

if __name__ == '__main__':
    unittest.main()
