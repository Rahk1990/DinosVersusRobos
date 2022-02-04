# add logic to dino attack() it should look very similar to robot attack()
# test this attack method just like we did in robo_turn()
# make logic for dino options 
# once you have dino options working, add it to robo turn and make an input 
    #so user can select what dino they want the robot to attack
# now go setup dino turn just like we did robot turn.
from fleet import Fleet
from herd import Herd

class Battlefield:

    def __init__(self):
        print('Game initializing')
        self.fleet = Fleet()
        print('Fleet Created!')
        self.herd = Herd()
        print('Herd Created!')
        
    

    def run_game(self):
        self.welcome()
        print('Game Start')

        self.battle()
        self.display_winners()
        print('Game Over')
       

        
    
    def welcome(self):
        print('Welcome to Game!')
    
    
    def battle(self): # good place for a while loop
        print(f'Today we have Robos vs Dinos. Let get ready to battle!')
        # battle = True
        while len(self.fleet.robots) > 0 and len(self.herd.dinos) > 0:
            self.robo_turn()
            if len(self.fleet.robots) < 0:
                return('Robos are Victorious!')
            # else
                #pass
        # self.fleet.fleet_status_check()

    def create_herd(self):
        self.herd.create_herd()
        

    def robo_turn(self):
        print("Pick a robot to fight with.")
        self.show_robo_options()
        robot_user_choice = int(input())
        print(f'Your Robo is {robot_user_choice}')
        
        print('Now its time to pick a Dino...')
        self.show_dino_options()
        dino_user_choice = int(input())
        self.fleet.robots[robot_user_choice].attack(self.herd.dinos[dino_user_choice])

        self.herd.dino_status_check(self.herd.dinos[dino_user_choice])

    
        

    def dino_turn(self):   # random.randint(0, len(self.her.dinos)-1)
        # print('Now pick the dino you want to attack.')
        self.show_dino_options()
        dino_user_choice = int(input())
        print(f'Your Dino is {dino_user_choice}')

        print("Pick a robot to fight with.")
        self.show_robo_options()
        robot_user_choice = int(input())
       
        print(f'Your Robo is {robot_user_choice}')    
        self.herd.dinos[dino_user_choice].attack(self.fleet.robots[robot_user_choice])
        
        self.fleet.fleet_status_check(self.fleet.robots[robot_user_choice])
        
        # self.show_dino_options()
        # setup an input for dino choice and replace the 0 below 
        
    def show_dino_options(self):
        count = 0 
        for dinos in self.herd.dinos:
            print(f'Press {count} to select {dinos.name}')
            count += 1

    def show_robo_options(self):
        count = 0
        for robot in self.fleet.robots:
            print(f'Press {count} to select {robot.name}')
            count += 1
        pass

    def display_winners(self):
        if (len(self.fleet.robots)) < (len(self.herd.dinos)):
            print('Robos Win!')
        elif (len(self.herd.dinos)) < (len(self.fleet.robots)): 
            print('Dinos Win!')