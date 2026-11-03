class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = list(hand)

    

    def collect_cards(self, cards):
        self.hand.extend(cards)

    def count_card(self):
        return len(self.hand)
    
    def draw_card(hand):
        return hand.pop(0)
        