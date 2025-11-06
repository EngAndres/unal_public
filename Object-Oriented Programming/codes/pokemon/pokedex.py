from character import Pokemon

class Pokedex:

    def __init__(self):
        self.pokemones = []

    def add_pokemon(self, new_pokemon: Pokemon):
        self.pokemones.append(new_pokemon)
