""""""

from abstract_pokemon import Pokemon

class FirePokemon(Pokemon):
    """"""

    def attack(self) -> int:
        """"""
        return (int)(self._attack_damage * self._health)

    def defense(self, type_adversary: str, attack_value: int):
        """
        
        Args:
            type_adversary (str):
            attack_value (int):
        """
        if type_adversary == "water":
            attack_value *= 1.5

        if attack_value > self._defense_base:
            self._health -= (int)(attack_value)
            self._health = 0 if self._health < 0 else self._health

    def health_recovery(self):
        self._health += (int)(self._defense_base * 0.1)
        if self._health > 100:
            self._health = 100
