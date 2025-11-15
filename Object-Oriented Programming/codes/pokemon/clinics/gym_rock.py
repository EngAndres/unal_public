from gym import Gym

class GymRock(Gym):
    def __init__(self, pokemon):
        super().__init__(pokemon)

    def fight(self):
        return "I  would bet you."