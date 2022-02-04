from dinos import Dinos
import random

class Herd:

    def __init__(self):
        self.dinos = []
        self.create_herd()
        

    def create_herd(self):
 

        dino_one = Dinos('Toothy')
        self.dinos.append(dino_one)

        dino_two = Dinos('Rex')
        self.dinos.append(dino_two)

        dino_three = Dinos('Klaw')
        self.dinos.append(dino_three)
    
        # self.dinos = [] 

        # print(self.dinos)


    def dino_turn(self):
        dino_fighter = self.dinos[1]
        print(dino_fighter) 

    def dino_status_check(self, dino):
        if dino.health <= 0:
            print(f'{dino.name} was eliminated form the battle.')
            self.dinos.remove(dino)
