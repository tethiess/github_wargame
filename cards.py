import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"
        

        

class Deck:
    def __init__(self):
        self.cards = []
        #we need list all suits of a duck
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        #Then we just have to give all those values to those suits
        for suit in suits:
            for value in range(2,15):
                card = Card(suit,value)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)
