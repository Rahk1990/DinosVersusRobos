from weapons import Weapons

class Robots:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapons = Weapons('Hammer', 25)

    def attack(self, dinos):
        pass