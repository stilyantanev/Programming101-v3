import unittest
from playlist import Playlist
from song import Song


class PlaylistTest(unittest.TestCase):

    def setUp(self):
        self.test_playlist = Playlist("Dance", False, False)
        self.song = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.test_playlist, Playlist))

    def test_valid_members(self):
        self.assertEqual(self.test_playlist.name, "Dance")
        self.assertEqual(self.test_playlist.repeat, False)
        self.assertEqual(self.test_playlist.shuffle, False)
        self.assertEqual(self.test_playlist.current_song_index, 0)
        self.assertEqual(self.test_playlist.songs, [])
        self.assertEqual(self.test_playlist.played_songs, set())

    def test_add_song(self):
        self.test_playlist.add_song(self.song)

        self.assertTrue(self.song in self.test_playlist.songs)

    def test_remove_song_in_playlist(self):
        self.test_playlist.songs = [self.song]
        self.test_playlist.remove_song(self.song)

        self.assertEqual(self.test_playlist.songs, [])

    def test_add_songs(self):
        song1 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")
        song2 = Song("Love", "Inna", "Hot", "3:40")
        self.test_playlist.add_songs([song1, song2])

        self.assertTrue(song1 in self.test_playlist.songs)
        self.assertTrue(song2 in self.test_playlist.songs)

    def test_total_length(self):
        song1 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")
        song2 = Song("Love", "Inna", "Hot", "3:40")
        self.test_playlist.songs = [song1, song2]

        self.assertEqual(self.test_playlist.total_length(), "00:08:15")

    def test_artists(self):
        song1 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")
        song2 = Song("Love", "Inna", "Hot", "3:40")
        self.test_playlist.songs = [song1, song2]
        result = {"Rihanna": 1, "Inna": 1}

        self.assertEqual(self.test_playlist.artists(), result)

    def test_shuffle_song(self):
        song1 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")
        song2 = Song("Love", "Inna", "Hot", "3:40")
        self.test_playlist.songs = [song1, song2]

        self.assertTrue(isinstance(self.test_playlist.shuffle_song(), Song))

    def test_next_song(self):
        song1 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")
        song2 = Song("Love", "Inna", "Hot", "3:40")
        playlist = Playlist("Dance", True, False)
        playlist.songs = [song1, song2]

        self.assertEqual(playlist.next_song(), song1)
        self.assertEqual(playlist.next_song(), song2)

    def test_previous_song(self):
        song1 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")
        song2 = Song("Love", "Inna", "Hot", "3:40")
        playlist = Playlist("Dance", True, False)
        playlist.songs = [song1, song2]

        self.assertEqual(playlist.previous_song(), song1)
        self.assertEqual(playlist.previous_song(), song2)

    def test_pprint_playlist(self):
        song1 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")
        song2 = Song("Love", "Inna", "Hot", "3:40")
        song3 = Song("One", "Ed Sheeran", "X", "4:13")

        self.test_playlist.add_song(song1)
        self.test_playlist.add_song(song2)
        self.test_playlist.add_song(song3)

        result = '''Artist      Song    Length
----------  ------  --------
Rihanna     Rehab   4:35
Inna        Love    3:40
Ed Sheeran  One     4:13'''
        self.assertEqual(self.test_playlist.pprint_playlist(), result)

    def test_prepare_json(self):
        song1 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")
        song2 = Song("Love", "Inna", "Hot", "3:40")
        self.test_playlist.songs = [song1, song2]
        song_dicts = [song1.__dict__, song2.__dict__]
        result = {"name": self.test_playlist.name, "songs": song_dicts}

        self.assertEqual(self.test_playlist.prepare_json(), result)

if __name__ == '__main__':
    unittest.main()
