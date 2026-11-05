"""
Loop Legends
The war game project IS303
"""
from player import Player
from cards import Card
from cards import Deck



print("Welcome to Two-Deck War!")

deck1 = Deck()
deck1.shuffle()

deck2 = Deck()
deck2.shuffle()


while len(deck1.cards) !=0 or len(deck2.cards) != 0:
    cards1 = int(deck1.cards[0].value)
    cards2 = int(deck2.cards[0].value)
    print(f"Player1 drew {deck1.cards[0]}")
    print(f"Player2 drew {deck2.cards[0]}")
    while cards1 == cards2:
        Player.draw_card(deck1.cards)
        Player.draw_card(deck2.cards)
        cards1 = int(deck1.cards[0].value)
        cards2 = int(deck2.cards[0].value)
        

    if cards1 > cards2:
        print("player1 wins round!")
        Player.draw_card(deck1.cards)
        Player.draw_card(deck2.cards)
    elif cards1 < cards2:

        Player.draw_card(deck1.cards)
        Player.draw_card(deck2.cards)
        print("Player2 wins round!")
    print(f"Player1 has {len(deck1.cards)} cards!")
    print(f"Player2 has {len(deck2.cards)} cards!")
    input("Press Enter to Keep playing!")



if len(deck1.cards) == 0:
    print("Player 2 has collected all of the cards.\nPlayer 2 wins the game!")
elif len(deck2.cards) == 0:
    print("Player 1 has collected all of the cards.\nPlayer 1 wins the game!")