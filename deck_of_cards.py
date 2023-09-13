from card import Card
import random
from random import randint


class DeckOfCards:

    def __init__(self):
        self.deckOfCards = []

        suits = {1: 'Heart', 2: 'CLUB', 3: 'DIAMOND', 4: 'SPADE'}
        values = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        for suit in suits:
            for value in values:
                self.deckOfCards.append(Card(suit, value))

    def cards_shffle(self):
        random.shuffle(self.deckOfCards)
        # print(self.deckOfCards)

    def deal_one(self):
        if not self.deckOfCards:
            return None
        # new_card = random.choice(self.deckOfCards)
        # index = self.deckOfCards.index(new_card)
        index = randint(0, len(self.deckOfCards) - 1)
        new_card = self.deckOfCards.pop(index)
        # print(new_card)
        # print(self.deckOfCards)
        return new_card



# cards1 = DeckOfCards()
# cards1.cards_shffle()
# cards1.deal_one()

