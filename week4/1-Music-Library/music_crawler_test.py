import unittest
from music_crawler import MusicCrawler
from playlist import Playlist


class MusicCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.path = "/home/stilyan/stilyan/Programming/HackBulgaria/Programming101-v3/week4/1-Music-Library/Music/"
        self.test_crawler = MusicCrawler(self.path)

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.test_crawler, MusicCrawler))

    def test_generate_playlist(self):
        self.assertTrue(
            isinstance(self.test_crawler.generate_playlist(), Playlist))

if __name__ == '__main__':
    unittest.main()
