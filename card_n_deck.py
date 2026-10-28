import random 

class Card: # Represents an essentially blank playing card with a suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck: # Represents a standard deck of 52 playing cards with the possible attributes.
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None #This line deals a card from the deck, or returns None if the deck is empty.
# the above line uses .pop to remove and return the last card from the deck.
    def __len__(self):
        return len(self.cards) #This line returns the number of cards remaining in the deck.