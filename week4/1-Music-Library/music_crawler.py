from playlist import Playlist
from song import Song
from os import listdir
from datetime import timedelta
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3


class MusicCrawler:

    def __init__(self, path):
        self.path = path
        self.mp3_paths = [
            item for item in listdir(path) if item.endswith(".mp3")]

    def generate_playlist(self):
        playlist = Playlist(name="Music")

        for mp3_path in self.mp3_paths:
            audio = MP3(self.path + mp3_path, ID3=EasyID3)

            artist = audio["artist"][0]
            album = audio["album"][0]
            title = audio["title"][0]
            length = str(timedelta(seconds=int(audio.info.length)))

            current_song = Song(title, artist, album, length)
            current_song.name = mp3_path

            playlist.add_song(current_song)

        return playlist
