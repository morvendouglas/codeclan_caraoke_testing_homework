import unittest
from src.venue import Venue
from src.room import Room
from src.song import Song
from src.guest import Guest
from src.bar import Bar

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room1", [], [], 4, 0)
        self.guest1 = Guest("Tom Green", 100, Song("Dancing Queen", "Abba"))
        self.guest2 = Guest("Joe Black", 250, Song("We Will Rock You", "Queen"))
        self.room.guests = [self.guest1.name, self.guest2.name]
        self.song1 = Song("Breakaway", "Kelly Clarkson")
        self.song2 = Song("Highway to Hell", "AC/DC")
        self.room.songs = [self.song1.title, self.song2.title]
        self.room2 = Room("Room2", [], [], 1, 0)
        self.room2.guests = [self.guest1.name, self.guest2.name]

    def test_room_has_name(self):
        self.assertEqual("Room1", self.room.name)
        
    def test_room_has_songs(self):
        self.assertEqual(["Breakaway", "Highway to Hell"], self.room.songs)

    def test_room_has_guests(self):
        self.assertEqual(["Tom Green", "Joe Black"], self.room.guests)    

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_guest_checks_in(self):
        self.assertEqual(["Tom Green", "Joe Black", "Lila Parks"], self.room.check_in("Lila Parks"))

    def test_guest_checks_out(self):
        self.assertEqual(["Tom Green"], self.room.check_out("Joe Black"))

    def test_check_for_song(self):
        self.assertEqual("We have that song!", self.room.check_for_song(Song("Breakaway", "Kelly Clarkson")))

    def test_add_song(self):
        add_song = Song("Shivers", "Ed Sheeran")
        self.assertEqual(["Breakaway", "Highway to Hell", "Shivers"], self.room.add_song(add_song.title))

    def test_room_has_spaces(self):
        self.assertEqual("Room has spaces", self.room.check_capacity())

    def test_room_has_reached_full_capacity(self):
        self.assertEqual("Room is full", self.room2.check_capacity())

    def test_room_tracks_entry_fees_and_bar_tab(self):
        self.assertEqual(0, self.room.guests_spending)

    def test_add_guest_entry_fees_to_room(self):
        self.assertEqual(24, self.room.add_entry_fees_to_room())

    def test_add_drink_to_room(self):
        drink = Bar(5, 10)
        self.assertEqual(5, self.room.add_drink_to_room(drink))

    def test_add_food_to_room(self):
        food = Bar(5, 10)
        self.assertEqual(10, self.room.add_food_to_room(food))

    # def test_add_guests_spending_to_till(self):
    #     drink = Bar(5, 10)
    #     food = Bar(5, 10)
    #     till = Venue("The OO CodeClan Caraoke", [], 1200)
    #     self.assertEqual(1239, self.room.add_total_guest_spending_to_till(food, drink, till))
        
    
