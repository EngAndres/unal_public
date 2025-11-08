from pokemon_electric import PokemonElectric
from pokemon_fire import PokemonFire

pikachu = PokemonElectric("Pikachu")
charmander = PokemonFire("Charmander")

charmander.defense(pikachu.attack())
print(f"Charmander Health: {charmander.health_}")

pikachu.defense(charmander.attack())
charmander.defense(pikachu.attack())
print(f"Pikachu Health:  {pikachu.health_}")
print(f"Charmander Health: {charmander.health_}")

charmander.defense(pikachu.special_attack())
print(f"Charmander Health: {charmander.health_}")   