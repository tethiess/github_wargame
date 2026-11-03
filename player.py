class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = list(hand)

    def draw_card(self):
        return self.hand.pop(0)

    def collect_cards(self, cards):
        self.hand.extend(cards)

    def count_card(self):
        return len(self.hand)
