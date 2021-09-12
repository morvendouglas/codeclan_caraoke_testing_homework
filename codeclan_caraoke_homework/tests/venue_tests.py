import unittest
from src.venue import Venue
from src.guest import Guest
from src.room import Room

class TestVenue(unittest.TestCase):
    def setUp(self):
        self.venue = Venue("The OO CodeClan Caraoke", [], 1200)
        room1 = Room("Room1", [], [], 4, 0)
        room2 = Room("Room2", [], [], 1, 0)
        self.venue.rooms = [room1.name, room2.name]

    def test_venue_has_a_name(self):
        self.assertEqual("The OO CodeClan Caraoke", self.venue.name)

    def test_venue_has_rooms(self):
        self.assertEqual(["Room1", "Room2"], self.venue.rooms)

    def test_venue_has_till(self):
        self.assertEqual(1200, self.venue.till)

    


