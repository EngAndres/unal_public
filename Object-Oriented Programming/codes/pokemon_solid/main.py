"""This module has the definition of the GUI of the videogame,
in a pretty simple way using P5 package.

Author: Carlos Andres Sierra <casierrav@unal.edu.co>
"""

from p5 import *
import random

from pokemons import *

# game elements
pokemons_list = []
gyms_list = []
clinics_list = []

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
world = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)] # for(i = 0; i < GRID_SIZE; i++)

# player -> index 0 - row      index 1 - column
player_location = [0, 0] # row 0, column 0
world[0][0] = 1

# player move
def key_pressed(event):
    global player_location

    # before move
    world[ player_location[0] ][ player_location[1] ] = 0

    if key == "UP":
        player_location[0] = max(player_location[0] - 1, 0)
    elif key == "DOWN":
        player_location[0] = min(player_location[0] + 1, GRID_SIZE - 1)
    elif key == "LEFT":
        player_location[1] = max(player_location[1] - 1, 0)
    elif key == "RIGHT":
        player_location[1] = min(player_location[1] + 1, GRID_SIZE - 1)

    # after move - new position
    world[ player_location[0] ][ player_location[1] ] = 1
    

def add_wild_pokemon(x: int, y: int):
    type_pokemon = random.randint(0, 3)
    if type_pokemon == 0:
        pokemon = ElectricPokemon()
    elif type_pokemon == 1:
        pokemon = RockPokemon()
    elif type_pokemon == 2:
        pokemon = WaterPokemon()
    else:
        pokemon = FirePokemon()

    pokemons_list.append((y, x, pokemon))    

def random_wild_pokemon():
    tries = 2   
    for i in range(tries): # for(int i = 0; i < tries; i++)
        x = random.randint(0, GRID_SIZE - 1)
        y = random.randint(0, GRID_SIZE - 1)

        if world[y][x] == 0:
            world[y][x] = 5
            add_wild_pokemon(x, y)


# ===================================================== #

def draw_cell(x, y, rule_space):
    px = x * CELL_SIZE
    py = y * CELL_SIZE

    if rule_space == 1: # player
        fill(10)
        rect((px, py), CELL_SIZE, CELL_SIZE)
    elif rule_space == 5: # wild pokemon
        fill(225, 100, 10) # orange
        rect((px, py), CELL_SIZE, CELL_SIZE)
        fill(255)
        text('P', px + (CELL_SIZE/2), py + (CELL_SIZE / 2))

def setup():
    title("Pokemon UNAL - OOP")
    size_world = CELL_SIZE * GRID_SIZE
    size(size_world, size_world)

def draw():
    background(200)

    # FPS = 60 - FramePerSecond
    # add wild pokemons based on time
    minutes_new_pokemon = 3
    new_wild_pokemon = 60 * (60 * minutes_new_pokemon)
    if frame_count % new_wild_pokemon == 0:
        random_wild_pokemon()

    # draw the grid
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            draw_cell(x, y, world[y][x])

    


run()
