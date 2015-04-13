import unittest
from music_crawler import MusicCrawler


class MusicCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.test_crawler = MusicCrawler(self.path)

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.test_crawler, MusicCrawler))

if __name__ == '__main__':
    unittest.main()
