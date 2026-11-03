class Player:
    def __int__(self, name, Card):
        self.name = name
        self.hand = Card.cards #we use random cards through cards.file 

    def draw_card(self):
        return self.hand.pop(0)#we draw the top card from our cards

    def collect_cards(self, cards):
        self.hand.extend(cards) #we collect all cards we won to the bottom

    def count_card(self):
        return len(self.hand)
    
