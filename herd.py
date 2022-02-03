from dinos import Dinos

class Herd:
    def __init__(self):
        
        self.dinos = [] 


    def create_herd(self):
        dino_one = Dinos('Toothy', 20)
        self.dinos.append(dino_one)

        dino_two = Dinos('chompy', 45)
        self.dinos.append(dino_two)

        dino_three = Dinos('Klaw', 50)
        self.dinos.append(dino_three)
   