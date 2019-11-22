#import required modules
import random


#Color Coding Class
class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#Person class
class Person:
    #init function to initialize Person Class
    def __init__(self, name, hp, mp, atk, magic, items):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 50
        self.atku = atk + 50
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Item"]
        self.experience = 0

    #Experience Implementation
    def get_experience(self):
        return self.experience

    def increase_experience(self,n):
        self.experience += n
        return self.experience

    def decrease_experience(self,n):
        self.experience -= n
        if self.experience < 0:
            self.experience = 0
        return self.experience

    #Damage Generator Function
    def damage_gen (self):
        return random.randrange(self.atkl, self.atku)

    #Implement generated damage to Person's HP
    def take_damage(self, dmg):
        self.hp -= dmg
        #Avoid getting negative HP
        if self.hp < 0:
            self.hp = 0
        return self.hp

    #Heal Function
    def heal(self, dmg):
        self.hp += dmg
        #Avoid getting HP greater than Max HP
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    #Get HP where ever is needed in main
    def get_hp(self):
        return self.hp

    #Get Maximum HP where ever is needed in main
    def get_max_hp(self):
        return self.maxhp

    #Get Magic Power where ever is needed in main
    def get_mp(self):
        return self.mp

    #Get Maximum Magic Power where ever is needed in main
    def get_max_mp(self):
        return self.maxmp

    #Reduce former magic power whenever player choose to use magic
    def reduce_mp(self, cost):
        self.mp -= cost

    #Function which will run in the beginning of the game so that player can make decision between available options
    def choose_action(self):
        #Choose between attack, magic ,and item
        i = 1
        print("\n" + BColors.BOLD + self.name + BColors.ENDC)
        print(BColors.OKBLUE + BColors.BOLD + "ACTIONS:" + BColors.ENDC)
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1


    # Function which will run when magic is chose so that player can make decision between available magic's options
    def choose_magic(self):
        i = 1
        print("\n" + BColors.OKBLUE + BColors.BOLD + "MAGICS:" + BColors.ENDC)
        for spell in self.magic:
            print("    " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    # Function which will run when item is chose so that player can make decision between available item's options
    def choose_item(self):
        i=1
        print("\n" + BColors.OKGREEN + BColors.BOLD + "ITEMS:" + BColors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item.name + ":", item.description + " (x" + str(item.quantity) + ")")
            i += 1

    # Function to choose Enemy Target
    def choose_target(self, enemies):
        i=1
        print("\n" + BColors.FAIL + BColors.BOLD + "Enemy Targets:" + BColors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("    " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("Choose a target: ")) - 1
        return choice

    # Function to print Players Status
    def show_stat(self):
        block = "█"
        space = " "
        num_hp = int(self.get_hp()/self.maxhp*25)
        num_mp = int(self.get_mp()/self.maxmp*15)
        snhp = 4 - len(str(self.get_hp()))
        snmp = 3 - len(str(self.get_mp()))
        print("                         _________________________                               _______________")
        print(BColors.BOLD + BColors.HEADER + self.name + ":" + "        " + str(self.get_hp()) + "/"
              + str(self.maxhp) + str(space*snhp) + " |" + BColors.OKGREEN + str(block*num_hp)
              + str(space*(25 - num_hp)) + BColors.ENDC + BColors.BOLD + BColors.HEADER
              + "                      " + str(self.get_mp())+ "/" + str(self.maxmp)
              + str(space*snmp) + " |" + BColors.OKBLUE + str(block*num_mp) + str(space*(15 - num_mp)) + BColors.ENDC)

    # Function to print Enemy Status
    def get_enemy_stat(self):
        block = "█"
        space = " "
        num_hp = int(self.get_hp() / self.maxhp *71)
        snhp = 5 - len(str(self.get_hp()))
        print("                         _______________________________________________________________________")
        print(BColors.BOLD + BColors.HEADER + self.name + ":" + "       " + str(self.get_hp()) + "/"
              + str(self.maxhp) + str(space * snhp) + " |" + BColors.FAIL + str(block * num_hp)
              + str(space * (71 - num_hp)) + BColors.ENDC)