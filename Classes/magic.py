#import required modules
import random

#Spell Class for magic users
class Spell:
    #init function to initialize Spell Class
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    #Spell damage generator function
    def damage_gen(self):
        mgl = self.dmg - 100
        mgu = self.dmg + 100
        return random.randrange(mgl, mgu)