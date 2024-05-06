class Card:
    def __init__(self, name, card_type, quantity):
        self.name = name
        self.card_type = card_type
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.card_type}) x{self.quantity}"
    
class Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
    
    def remove_card(self, card):
        self.cards.remove(card)

    def get_remaining_cards(self):
        return sum(card.quantity for card in self.cards)
    
    def get_card_count(self, card_name):
        for card in self.cards:
            if card.name == card_name:
                return card.quantity
        return 0
    
    def __str__(self):
        return f"Deck with {self.get_remaining_cards()} cards:\n" + "\n".join(str(card) for card in self.cards)