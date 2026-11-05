import random
from typing import Union


RANK_VALUES = {
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}
RANK_NAMES = {value: name for name, value in RANK_VALUES.items()}


class Card:
    def __init__(self, suit: str, value: Union[int, str]):
        self.suit = suit
        if isinstance(value, str):
            if value in RANK_VALUES:
                card_value = RANK_VALUES[value]
            else:
                try:
                    card_value = int(value)
                except ValueError as exc:
                    raise ValueError("value must be from 2 to 14 or a face-card name") from exc
        elif isinstance(value, int) and not isinstance(value, bool):
            card_value = value
        else:
            raise TypeError("value must be an integer or rank string")

        if not 2 <= card_value <= 14:
            raise ValueError("value must be from 2 to 14")

        self.value = card_value
        self.rank = RANK_NAMES.get(card_value, str(card_value))

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
