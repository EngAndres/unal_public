from character import Pokemon
class Gym:

    def __init__(self, pokemon: Pokemon):
        self.pokemon_leader = pokemon

    def new_leader(self, pokemon_new_leader):
        self.pokemon_leader = pokemon_new_leader

    def fight(self):
        return "This i a battle between two oponents."