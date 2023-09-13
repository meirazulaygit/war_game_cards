from card_game import CardGame


card_game = CardGame()

for i in range(10):
    print(f"Round {i + 1}:")
    # while card_game.player1.deck_of_player_cards and card_game.player2.deck_of_player_cards:
    card1 = card_game.player1.get_card()
    print(f"card of {card_game.player1.name} = {card1}")
    card2 = card_game.player2.get_card()
    print(f"card of {card_game.player2.name} = {card2}")
    if card1 > card2:
        print(f"{card_game.player1.name} wins this round!")
        card_game.player1.add_card(card1)
        card_game.player1.add_card(card2)
        ''' the winner add the cards'''
    elif card2 > card1:
        print(f"{card_game.player2.name} wins this round!")
        card_game.player2.add_card(card1)
        card_game.player2.add_card(card2)
        ''' the winner add the cards'''

    elif card1 == card2:
        print("It's a tie! do not have a winner in this round.")

winner = card_game.get_winner()
if winner:
    print(f"The winner is {winner}")
else:
    print("It's a tie! do not have a winner in this game.")

# elif card2 == card1:
#     print(f"{card_game.player2.name} wins this round!")
#     card_game.player2.add_card(card1)
#     card_game.player2.add_card(card2)
# elif card1 < card2:
#     print(f"{card_game.player1.name} wins this round!")
#     card_game.player1.add_card(card1)
#     card_game.player1.add_card(card2)
