from fleet import Fleet
from robos import Robots

class Dinos:

   def __init__(self, name):
      self.name = name 
      self.attack_power = 25
      self.health = 50 
      
      
   def attack(self, robot):
       robot.health -= self.attack_power
       print(f'{self.name} is attacking {robot.name}, with an attack power of {self.attack_power}! {robot.name} has {robot.health} left!')
    
