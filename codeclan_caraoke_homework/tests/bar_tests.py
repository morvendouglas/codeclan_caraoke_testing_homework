import unittest
from src.bar import Bar

class TestBar(unittest.TestCase):

    def setUp(self):
        self.drink = 4
        self.food = 6
       
    def test_bar_has_drinks(self):
        self.assertEqual(4, self.drink)

    def test_bar_has_food(self):
        self.assertEqual(6, self.food)
        

    

