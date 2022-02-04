
from robos import Robots

class Fleet:

    def __init__(self):
        self.robots = [] 
        self.create_fleet()
        
    def create_fleet(self):
        robo_one = Robots('Magatron')
        self.robots.append(robo_one) 

        robo_two = Robots('Jimbot')
        self.robots.append(robo_two)
    
        robo_three = Robots('Bolt')
        self.robots.append(robo_three)

    def fleet_status_check(self, robot):
        if robot.health <= 0:
            print(f'{robot.name} was eliminated form the battle.')
            self.robots.remove(robot)
            

