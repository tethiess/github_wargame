import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        rank_values = {
            "Jack": 11,
            "Queen": 12,
            "King": 13,
            "Ace": 14,
        }
        rank_names = {
            11: "Jack",
            12: "Queen",
            13: "King",
            14: "Ace",
        }
        if isinstance(value, str) and not value.isdigit():
            self.rank = value
            self.value = rank_values[value]
        else:
            self.value = int(value)
            self.rank = rank_names.get(self.value, str(self.value))

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(suit, value) for suit in suits for value in range(2, 15)]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if self.cards:
            return self.cards.pop()
        return None

    def __len__(self):
        return len(self.cards)
