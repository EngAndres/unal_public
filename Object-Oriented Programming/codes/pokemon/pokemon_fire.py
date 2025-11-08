from character import Pokemon

class PokemonFire(Pokemon):
    
    def defense(self, damage: int, type_pokemon: str):
        if type_pokemon == "electric":
            self.health_ -= damage
        elif type_pokemon == "water":
            self.health_ -= (damage * 1.3)
        elif type_pokemon == "rock":
            self.health_ -= (damage * 0.8)
        else:
            print("Error in pokemon type")
            