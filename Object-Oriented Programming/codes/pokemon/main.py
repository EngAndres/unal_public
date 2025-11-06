from character import Pokemon

pikachu = Pokemon("Pikachu")
charmander = Pokemon("Charmander")

charmander.defense(pikachu.attack())
print(charmander.health_)

pikachu.defense(charmander.attack())
charmander.defense(pikachu.attack())
print(charmander.health_)

charmander.defense(pikachu.attack())
print(charmander.health_)   