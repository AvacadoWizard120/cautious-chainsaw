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

# Scratch everything I said in this spot, let's keep things simple for the sake
# of fun.


# Set the initial level at turn 0
game_level = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

unit_data = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0 ,0]
]

# define some symbols so we can display graphics
# the size will be how many units will fit in the trench.
trench_data = {
    1: {'symbol': '|', 'size': 1}, # 1 is single digit number of units [0,9]
    2: {'symbol': '|', 'size': 2}, # 2 is double digit number of units [0,99]
    3: {'symbol': '|', 'size': 3} # [0,999]
}



# You can then iterate over the game_level array and print the appropriate symbol based on the trench_data and unit_data
for row in range(len(game_level)):
    for col in range(len(game_level[row])):
        if game_level[row][col] in trench_data:
            symbol = trench_data[game_level[row][col]]['symbol']
            size = trench_data[game_level[row][col]]['size']
            units = unit_data[row][col]
            print(f'{symbol}{(size - 1) * " "}{units}{symbol}', end='')
        else:
            print(' ' * 5, end='')  # Print 5 spaces for non-trench tiles
    print()  # Print a new line after each row


user_input = input("Press Enter to continue...")
print("You pressed Enter!")