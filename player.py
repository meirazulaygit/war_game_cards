from deck_of_cards import DeckOfCards
from random import randint


class Player:
    def __init__(self, name, num_of_cards=26):
        ''' create player in game '''
        self.name = name
        self.deck_of_player_cards = []
        self.num_of_cards = num_of_cards

        if self.num_of_cards > 26 or self.num_of_cards < 10:
            self.num_of_cards = 26
        ''' if  num of player cards bigger from 26 or smaller from 10  so num of cards wil be 26'''

    def set_hand(self, deck_of_cards: DeckOfCards):
        ''' this function set hand of card to player '''
        for i in range(self.num_of_cards):
            card = deck_of_cards.deal_one()
            self.deck_of_player_cards.append(card)

    def get_card(self):
        ''' this function return 1 random card of player hand and remove this card from player hand '''
        if not self.deck_of_player_cards:
            return "no more card in player cards"
        index = randint(0, len(self.deck_of_player_cards) - 1)
        card = self.deck_of_player_cards.pop(index)
        # print(card)
        # print(self.deck_of_player_cards)
        return card

    def add_card(self, card: DeckOfCards):
        ''' this function make 1 card to player hand '''
        self.deck_of_player_cards.append(card)

# deckOfPlayer = DeckOfCards()
# # deckOfPlayer.cards_shffle()
#
# player1 = Player("koko", num_of_cards=20)
# player1.set_hand(deckOfPlayer)
#
# print(player1.name)
# print(player1.deck_of_player_cards)
