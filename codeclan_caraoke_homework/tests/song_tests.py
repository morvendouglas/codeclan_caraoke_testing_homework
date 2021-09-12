import unittest
from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("I Guess That's Why They Call It The Blues", "Elton John")

    def test_song_has__title(self):
        self.assertEqual("I Guess That's Why They Call It The Blues", self.song.title)

    def test_song_has__artist(self):
        self.assertEqual("Elton John", self.song.artist)
    