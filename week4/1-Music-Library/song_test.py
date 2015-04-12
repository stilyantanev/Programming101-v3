import unittest
from song import Song


class SongTest(unittest.TestCase):

    def setUp(self):
        self.test_song = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")

    def test_create_new_instance(self):
        self.assertTrue(isinstance(self.test_song, Song))

    def test_valid_members(self):
        self.assertEqual(self.test_song.title, "Rehab")
        self.assertEqual(self.test_song.artist, "Rihanna")
        self.assertEqual(self.test_song.album, "Good Girl Gone Bad")
        self.assertEqual(self.test_song.length, "4:35")

    def test_str_dunder(self):
        title = self.test_song.title
        artist = self.test_song.artist
        album = self.test_song.album
        length = self.test_song.length

        self.message = "{} - {} from {} - {}"
        self.message = self.message.format(artist, title, album, length)

        self.assertEqual(str(self.test_song), self.message)

    def test_repr_dunder(self):
        title = self.test_song.title
        artist = self.test_song.artist
        album = self.test_song.album
        length = self.test_song.length

        self.message = "{} - {} from {} - {}"
        self.message = self.message.format(artist, title, album, length)

        self.assertEqual(repr(self.test_song), self.message)

    def test_eq_dunder_when_same(self):
        song1 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")
        song2 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")

        self.assertTrue(song1 == song2)

    def test_eq_dunder_when_not_same(self):
        song1 = Song("Rehab", "Rihanna", "Good Girl Gone Bad", "4:35")
        song2 = Song("Love", "Inna", "Hot", "3:40")

        self.assertTrue(song1 != song2)

    def test_hash_dunder(self):
        self.assertTrue(isinstance(hash(self.test_song), int))

    def test_length_of_song_spliting_to_parts(self):
        self.assertEqual(len(self.test_song.length.split(":")), 2)

    def test_length_of_song_with_two_parts(self):
        parts = self.test_song.length.split(":")
        parts = ["0"] + parts

        self.assertEqual(parts, ["0", "4", "35"])

    def test_length_of_song_with_parameter_seconds(self):
        self.assertEqual(self.test_song.length_of_song(seconds=True), 275)

    def test_length_of_song_with_parameter_minutes(self):
        self.assertEqual(self.test_song.length_of_song(minutes=True), 4)

    def test_length_of_song_with_parameter_hours(self):
        self.assertEqual(self.test_song.length_of_song(hours=True), 0)

    def test_length_of_song_without_parameter(self):
        self.assertEqual(self.test_song.length_of_song(), "4:35")

if __name__ == '__main__':
    unittest.main()
