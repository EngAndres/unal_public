"""This module has the definition of the GUI of the videogame,
in a pretty simple way using P5 package.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""
from p5 import *
import random

# constants
GRID_SIZE = 20
CELL_SIZE = 30

# rules - space
# 0 - nothing
# 1 - player
# 2 - small clinic
# 3 - big clinic
# 4 - gym
# 5 - wild pokemon

# initilize game world -> 0,0,0,...,0 20 times
world = [[0 for i in range(GRID_SIZE)]] # for(i = 0; i < GRID_SIZE; i++)

# player -> index 0 - row      index 1 - column
player_location = [0, 0] # row 0, column 0

# player move
def key_pressed(event):
    global player_location

    if key == "UP":
        player_location[0] = max(player_location[0] - 1, 0)
    elif key == "DOWN":
        player_location[0] = min(player_location[0] + 1, GRID_SIZE - 1)
    elif key == "LEFT":
        player_location[1] = max(player_location[1] - 1, 0)
    elif key == "RIGHT":
        player_location[1] = min(player_location[1] + 1, GRID_SIZE - 1)

