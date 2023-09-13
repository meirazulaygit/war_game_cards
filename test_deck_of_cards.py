from unittest import TestCase
from deck_of_cards import DeckOfCards


class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck = DeckOfCards()

    def test_init_lenOfDeck_valid(self):
        self.assertTrue(len(self.deck.deckOfCards), 52)

    def test_init_lenOfDeck_invalid(self):
        self.assertNotEqual(len(self.deck.deckOfCards), 51)

    def test_cards_shffle_valid(self):
        in_order = list(self.deck.deckOfCards)
        self.deck.cards_shffle()
        shuffled_order = list(self.deck.deckOfCards)
        self.assertNotEqual(in_order, shuffled_order)

    # def test_cards_shffle_invalid(self):
    #     # in_order = list(self.deck.deckOfCards)
    #     self.deck.cards_shffle()
    #     shuffled_order1 = list(self.deck.deckOfCards)
    #     self.deck.cards_shffle()
    #     shuffled_order2 = list(self.deck.deckOfCards)
    #     self.assertNotEqual(shuffled_order1, shuffled_order2)

    def test_deal_one_valid(self):
        card1 = self.deck.deal_one()
        self.assertIsNotNone(card1)
        self.assertEqual(len(self.deck.deckOfCards), 51)

    def test_deal_one_invalid(self):
        self.deck.deal_one()
        self.assertNotEqual(len(self.deck.deckOfCards), 52)