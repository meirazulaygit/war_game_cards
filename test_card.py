from unittest import TestCase
from card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card1 = Card('CLUB', '3')
        self.card2 = Card('Heart', '3')
        ''' create cards '''

    def test_init_valid(self):
        self.assertEqual(self.card1.suit, 'CLUB')
        ''' check if suit of card is equal to 'CLUB' '''
        self.assertEqual(self.card1.value, '3')
        '''check if value of card is equal to '3' '''
        self.assertIsInstance(self.card1.suit, str)
        ''' check if suit of card is type of string '''
        self.assertIsInstance(self.card1.value, str)
        ''' check if value of card is type of string  '''

    def test_init_invalid(self):
        self.assertNotEqual(self.card1.suit, 'CAW')
        ''' check if suit of card is not equal to 'CLUB' '''
        self.assertNotEqual(self.card1.value, '15')
        '''check if value of card is equal to '3' '''

    def test_greater_than(self):
        self.assertTrue(self.card2 > self.card1)
        ''' check if card2 is greater then card1'''
        self.assertFalse(self.card1 > self.card2)
        ''' check if card1 is greater then card2'''

    def test_is_not_equal(self):
        card1 = Card('CLUB', '3')
        card2 = Card('Heart', '3')
        self.assertFalse(card1 == card2)
        ''' check if card2 is not equal then card1'''

    def test_equal(self):
        card1 = Card('CLUB', '3')
        card2 = Card('CLUB', '3')
        self.assertTrue(card2 == card1)
        ''' check if card2 is equal then card1'''
