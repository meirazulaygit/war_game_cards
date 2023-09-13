class Card:
    ''' create cards '''
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.suits = {1: 'Heart', 2: 'CLUB', 3: 'DIAMOND', 4: 'SPADE'}
        self.values = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

    '''  check  if card is greater then other card   '''
    def __gt__(self, other):
        if self.value == other.value:
            return self.suit > other.suit
        else:
            return self.value > other.value

    '''  check  if card is equal other card   '''
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    ''' returns a printable representation of an object in Python '''
    def __repr__(self):
        return f"value = {self.values[self.value]}, suit = {self.suits[self.suit]}"