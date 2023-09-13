from unittest import TestCase
from deck_of_cards import DeckOfCards
from player import Player
from unittest import mock
from card import Card


class TestPlayer(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()
        ''' create deck of cards'''
        self.player = Player("koko", num_of_cards=16)
        '''  create player '''

    def test__init__valid_name(self):
        self.assertEqual("koko", self.player.name)
        ''' check if this name is equal to player name'''

    def test__init__valid_players_cards(self):
        self.assertEqual(16, self.player.num_of_cards)
        ''' check if this num of cards is equal to num of card of player '''

    def test__init__invalid_name(self):
        self.assertNotEqual("kiki", self.player.name)
        ''' check if this name is  not equal to player name'''

    def test__init__invalid_players_cards(self):
        self.assertNotEqual(15, self.player.num_of_cards)
        ''' check if this num of cards is not equal to num of card  '''

    def test__init__valid_type(self):
        self.assertIsInstance(self.player.name, str)
        ''' check if this type of name is  equal to type of player name'''

    def test_set_hand_valid(self):
        self.player.set_hand(self.deck)
        self.assertTrue(len(self.player.deck_of_player_cards), 16)
        ''' check if this num of cards is  equal to num of card of player deck after set hand() '''

    @mock.patch('deck_of_cards.DeckOfCards.deal_one', return_value=Card(7, 1))
    def test_set_hand_call_deal_one(self, mock_deal_one):
        self.player.set_hand(self.deck)
        self.assertIn(Card(7, 1), self.player.deck_of_player_cards)
        ''' this test check if set hand function call deal one function correct'''

    def test_set_hand_invalid(self):
        self.player.set_hand(self.deck)
        self.assertNotEqual(len(self.player.deck_of_player_cards), 'sffg')
        self.assertNotEqual(len(self.player.deck_of_player_cards), 15)
        self.assertNotEqual(len(self.player.deck_of_player_cards), "16")
        ''' check if this num of cards or string is not equal to num of card of player deck after set hand() '''

    def test_get_card_valid(self):
        self.player.set_hand(self.deck)
        card1 = self.player.get_card()
        self.assertIsNotNone(card1)
        self.assertEqual(15, len(self.player.deck_of_player_cards))
        '''  check if after get_card function the deck of player is less 1 card'''

    def test_get_card_invalid(self):
        self.player.set_hand(self.deck)
        card1 = self.player.get_card()
        self.assertIsNotNone(card1)
        self.assertNotEqual(16, (len(self.player.deck_of_player_cards)))
        '''  check if after get_card function the deck of player is equal to deck of player card'''

    def test_add_card(self):
        self.player.set_hand(self.deck)
        sizeOfDeck = 16
        card1 = self.deck.deal_one()
        self.player.add_card(card1)
        self.assertEqual(len(self.player.deck_of_player_cards), sizeOfDeck + 1)
        ''' check if add_card is append 1 more card to deck of player cards'''
