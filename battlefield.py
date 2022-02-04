from fleet import Fleet
from herd import Herd

class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
        
    

    def run_game(self):
        self.welcome()
        print('Game Start')
    
    def welcome(self):
        print('Welcome to Game!')
    
    
    def battle(self):
        print(f'Today we have Robos vs Dinos. Let get ready to battle!')
    
        

    def create_herd(self):
        self.herd.create_herd()
        

    def dino_turn(self):    
        self.herd.create_herd()

    # def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass