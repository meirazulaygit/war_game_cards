from deck_of_cards import DeckOfCards
from player import Player


class CardGame:
    """create objects to reset the game """
    def __init__(self, name1="moki", name2="shoki", numOfCards=26):
        self.deck = DeckOfCards()
        self.player1 = Player(name1, numOfCards)
        self.player2 = Player(name2, numOfCards)
        self.new_game()

    def new_game(self):
        """start a new game by setting the 2 players a new deck of cards each"""
        self.deck.cards_shffle()
        self.player1.set_hand(self.deck)
        self.player2.set_hand(self.deck)

    def get_winner(self):
        """the method compares between the players number of cards. the player with the grater numbers of cards wins.
        the method returns the winner"""
        if self.player1.num_of_cards.__gt__(self.player2.num_of_cards):
            return f"the winner is {self.player1.name}"
        if self.player1.num_of_cards.__lt_(self.player2.num_of_cards):
            return f"the winner is {self.player2.name}"
        else:
            return None



