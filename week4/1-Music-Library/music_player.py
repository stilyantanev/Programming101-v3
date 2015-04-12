from subprocess import Popen, PIPE
from playlist import Playlist
from music_crawler import MusicCrawler


class MusicPlayer:

    def __init__(self):
        self.real_playlist = Playlist()
        self.process = Popen(["mpg123", ''], stdout=PIPE, stderr=PIPE)

    def add_songs(self, directory):
        crawler = MusicCrawler(directory)
        new_playlist = crawler.generate_playlist()

        for song in new_playlist.songs:
            self.real_playlist.add_song(song)

    def stop_playing(self):
        self.process.kill()

    def play_next(self, directory):
        current_song = self.real_playlist.next_song()
        full_path = directory + current_song.name
        self.process = Popen(["mpg123", full_path], stdout=PIPE, stderr=PIPE)
        print("Playing: {}".format(current_song.name))

    def play_previous(self, directory):
        current_song = self.real_playlist.previous_song()
        full_path = directory + current_song.name
        self.process = Popen(["mpg123", full_path], stdout=PIPE, stderr=PIPE)
        print("Playing: {}".format(current_song.name))

    def show_playlist(self):
        print(self.real_playlist.pprint_playlist())

    def change_shuffle_mode(self, mode):
        self.real_playlist.shuffle = mode

    def change_repeat_mode(self, mode):
        self.real_playlist.repeat = mode
