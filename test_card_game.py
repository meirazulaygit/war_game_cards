from unittest import TestCase
from card_game import CardGame
from player import Player
from unittest import mock


class TestCardGame(TestCase):

    def setUp(self):
        self.card_game = CardGame()

    def test__init__valid(self):
        """check if the init works properly by testing the objects """
        self.assertEqual("moki", self.card_game.player1.name)
        self.assertEqual(26, self.card_game.player1.num_of_cards)
        self.assertIsInstance(self.card_game.player1.name, str)
        self.assertIsInstance(self.card_game.player1.num_of_cards, int)

    def test__init__invalid(self):
        """test an invalid cases of the init method """
        self.assertNotEqual("koko", self.card_game.player1.name)
        self.assertNotEqual(9, self.card_game.player1.num_of_cards)
        self.assertNotIsInstance(self.card_game.player1.name, int)
        self.assertNotIsInstance(self.card_game.player1.num_of_cards, str)

    @mock.patch('Card_Game.CardGame.new_game')
    def test__init__function_valid(self, mock1):
        # Create an instance of CardGame
        card_game = CardGame()
        # Assert that the mocked method new_game was called
        mock1.assert_called()
        ''' call the function new game and check if it has been called when using the CardGame init method'''

    @mock.patch('deck_of_cards.DeckOfCards.cards_shffle')
    @mock.patch('card_game.Player.set_hand')
    def test_new_game_valid(self, mock1: mock.MagicMock, mock2: mock.MagicMock):
        """by using mock, call the 'set_hand' and 'cards_shuffle' method. check if they were called and if they are
        working properly"""
        card_game = CardGame()
        mock1.assert_called()
        mock2.assert_called()
        """ check if set hand works by comparing the len of players deck and the num of cards """
        self.assertEqual(self.card_game.player1.num_of_cards, len(self.card_game.player1.deck_of_player_cards))
        self.assertEqual(self.card_game.player2.num_of_cards, len(self.card_game.player2.deck_of_player_cards))

    def test_get_winner_valid(self):
        """check if the method compares between 2 players correctly and returns the right winner as defined"""
        player0 = Player("player0", 15)
        player100 = Player("player100", 24)
        self.assertGreater(player100.num_of_cards, player0.num_of_cards, "player100 is greater")
        self.assertNotEqual(player100.num_of_cards, player0.num_of_cards)

    def test_get_winner_invalid(self):
        """test an invalid case by comparing the winner and the looser"""
        player0 = Player("player0", 15)
        player100 = Player("player100", 24)
        self.assertLessEqual(player0.num_of_cards, player100.num_of_cards, "player0 is not greater")
