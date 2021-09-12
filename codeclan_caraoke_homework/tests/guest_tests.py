import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.person = Guest("Francesca James", 250, Song("Livin' On A Prayer", "Bon Jovi"))

    def test_guest_has__name(self):
        self.assertEqual("Francesca James", self.person.name)

    def test_guest_has__cash(self):
        self.assertEqual(250, self.person.cash)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Livin' On A Prayer", self.person.favourite_song.title)


        