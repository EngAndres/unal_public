""""""

from abc import ABC, abstractmethod

class Pokemon(ABC):
    """"""

    # class attribute
    _health = 100

    def __init__(self, attack_damage: int, base_defense: int):
        self._attack_damage = attack_damage
        self._defense_base = base_defense

    def is_defeated(self) -> bool:
        """"""
        minimum_health = 5
        return self.__health < minimum_health
        
    def evolute(self):
        """"""
        print("This pokemon cannot evolute.")

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defense(self, type_adversary: str, attack_value: int):
        pass

    @abstractmethod
    def health_recovery(self):
        pass
