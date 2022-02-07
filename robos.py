from weapons import Weapons

class Robots:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.weapons = Weapons('Hammer', 25)

    def attack(self, dino):
        dino.health -= self.weapons.attack_power
        print(f'{self.name} is attacking {dino.name} with {self.weapons.name} for {self.weapons.attack_power} damge leaving {dino.name} with {dino.health} health remaining ')
        