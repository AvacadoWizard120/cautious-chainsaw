from deck_builder import Card, Deck
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 50
MARGIN = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

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
    [0, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 1]
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



# Function to draw a trench
def draw_trench(trench, x, y):
    color = (0, 0, 0)  # Black color
    size = trench_data[trench]['size']
    for i in range(size):
        pygame.draw.rect(screen, color, (x + i * TILE_SIZE, y + i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

# Function to draw the game level
def draw_game_level():
    for row in range(len(game_level)):
        for col in range(len(game_level[row])):
            if game_level[row][col] in trench_data:
                draw_trench(game_level[row][col], col * TILE_SIZE, row * TILE_SIZE)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the game level
    draw_game_level()

    # Update the display
    pygame.display.flip()