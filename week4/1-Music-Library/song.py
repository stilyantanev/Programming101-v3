class Song:

    def __init__(self, title="", artist="", album="", length=""):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length
        self.name = ""

    def __str__(self):
        message = "{} - {} from {} - {}"

        return message.format(self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        equal_titles = self.title == other.title
        equal_artist = self.artist == other.artist
        equal_album = self.album == other.album
        equal_length = self.length == other.length

        return equal_titles and equal_artist and equal_album and equal_length

    def __hash__(self):
        return hash(self.title + self.artist + self.album + self.length)

    def length_of_song(self, seconds=False, minutes=False, hours=False):
        parts = self.length.split(':')
        parts_length = len(parts)

        if parts_length <= 1:
            raise ValueError

        if parts_length == 2:
            parts = ["0"] + parts

        if seconds:
            return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        elif minutes:
            return int(parts[0]) * 60 + int(parts[1])
        elif hours:
            return int(parts[0])
        else:
            return self.length
