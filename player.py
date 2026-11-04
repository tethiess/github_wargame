from cards import Card, Deck

class Player:
    def __init__(self, player_num, hand):
        self.player_num = player_num
        self.hand = hand if hand is not None else []  # Initialize the player's hand, defaulting to an empty list if no hand is provided.

    def draw(self, deck):
        card = deck.deal()
        if card:
            self.hand.append(card)
            return card
        
    def __repr__(self):
        drawn = ", ".join(str(card) for card in self.hand) 
        return f"Player {self.player_num} drew the {Card}"