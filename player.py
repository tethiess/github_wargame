class Player:
    def __init__(self, name, hand=None):
        self.name = name
        self.player_num = name
        self.hand = list(hand) if hand is not None else []

    def draw(self, deck):
        card = deck.deal()
        if card is not None:
            self.hand.append(card)
        return card

    def collect_cards(self, cards):
        self.hand.extend(cards)

    def count_card(self):
        return len(self.hand)

    @staticmethod
    def draw_card(hand):
        if hand:
            return hand.pop(0)
        return None

    def __repr__(self):
        drawn = ", ".join(str(card) for card in self.hand)
        return f"Player {self.name} has {drawn}"
