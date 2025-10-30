class Pokemon:

    def __init__(self, name: str):
        self.name = name
        self.health_ = 100
        self.lives = 3

    def attack(self):
        damage = 15
        return (damage * self.health_) / 100 

    def defense(self, damage: int):
        block = False
        if not block:
            self.health_ -= damage
            if self.health_ < 0:
                self.health_ = 0

    def is_defeat(self):
        return True if self.health == 0 else False
