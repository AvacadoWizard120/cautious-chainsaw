from deck_builder import Card, Deck

deck = Deck()

# This is not indicitive of the final product at all.
# I'm just throwing out examples of how we can create new Cards.
shovels = Card("Shovels", "Utility", 15)
troops = Card("Troops", "Units", 20)
artillery = Card("Artillery", "Utility", 8)
restock = Card("Restock", "Utility", 10) # Maybe replace this with ressuply, or have a seperate ressuply card.


# We could call this at any time during gameplay and we can even define how many to add back to the deck,
# like say each month (in game time) more cards are added to the deck or something like that. 
# (Maybe reshuffle event)
deck.add_card(shovels)
deck.add_card(troops)
deck.add_card(artillery)
deck.add_card(restock)

print(deck)

print("Remaining Cards: " + str(deck.get_remaining_cards()))
print("Troop cards in deck: " + str(deck.get_card_count("Troops")))
print("Restock cards in deck: " + str(deck.get_card_count("Restock")))

# I'm thinking maybe we have a dictionary system that allows players to create 'Units' or 'Squads'
# I don't know what to call them, but essentially we have cards with different types of Units and you can use
# those cards to create a Squad or wtv we end up calling it, and then the player can use the squad to try and
# take a trench or make them hold a trench segment and depending on the types of units in the squad, the chances
# of victory in battle will increase/decrease.