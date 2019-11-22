#Import required classes
from Classes.game import BColors, Person
from Classes.magic import Spell
from Classes.inventory import Item
#import required modules
import random

#Create Black Magic To Attach
fire = Spell("Fire", 15, 300, "black")
thunder = Spell("Thunder", 25, 500, "black")
blizzard = Spell("Blizzard", 45, 800, "black")
meteor = Spell("Meteor", 70, 1200, "black")
quake = Spell("Quake", 110, 2000, "black")

#Create White Magic To Heal
cure = Spell("Cure", 50, 600, "white")
cura = Spell("Cura", 100, 1500, "white")

#Creat Players' Items
potion = Item ("Potion", "potion", "Heals 50 HP", 50, 15)
hipotion = Item ("Hi Potion", "potion", "Heals 100 HP", 100, 5)
superpotion = Item ("Super Potion", "potion", "Heals 500 HP", 100, 5)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999, 5)
megaelixir = Item("Mega Elixir", "elixir", "Fully restores party's HP/MP", 9999, 2)
grenade = Item("Grenade", "attack", "Deals 500 damage", 900, 5)

#Instantiate Players
player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion, hipotion, superpotion, elixir, megaelixir, grenade]
player1 = Person("Aegon",3260, 332, 430, player_spells,player_items)
player2 = Person("Ario ",4160, 408, 550, player_spells,player_items)
player3 = Person("Tony ",3089, 474, 370, player_spells,player_items)
#Instantiate Enemies and their properties
#Note that Items are not usable for Enemies and they only use magic
firestorm = Spell("Fire Storm", 80, 900, "black")
meteorstorm = Spell("Meteor Storm", 100, 1800, "black")
ultimateelixir = Spell("Ultimate Storm", 50, 2000, "white")
enemy_spells = [firestorm, meteorstorm, ultimateelixir]
enemy1 = Person("Imp  ", 2500, 400, 560, enemy_spells, [])
enemy2 = Person("Robot",15000, 800, 315, enemy_spells,[])
enemy3 = Person("Imp  ", 2500, 400, 560, enemy_spells, [])
#Set players
players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
defeated_enemies = []
defeated_players = []

#Set running options
run = True
i = 0


# Define win/loose criteria function for Battle Game
def result():
    global run
    if len(defeated_enemies) == 3:
        print(BColors.OKGREEN + "Congrats! You win!" + BColors.ENDC)
        run = False
    elif len(defeated_players) == 3:
        print(BColors.FAIL + "Your enemies have defeated you!" + BColors.ENDC)
        run = False


#Begin The Battle
print(BColors.FAIL + BColors.BOLD + 'An Enemy has Invaded!' + BColors.ENDC)
while run:
    print("========================")
    print("\n")
    #Column Headers
    print("Name                     Heat Point                                              Magic Power")
    for player in players:
        #Show Players' Status
        player.show_stat()
        print(BColors.UNDERLINE + BColors.OKGREEN  + "\n"
              + "Player {} Experience: {}".format(player.name, player.get_experience()) + BColors.ENDC)
    #Print Enemy Status
    for enemy in enemies:
        enemy.get_enemy_stat()
    for player in players:
        # Choose an Action between Attack, Magic, and Item
        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1
        if index == 0:
            #Attack Option
            #Damage generation and implement damage to enemy HP
            dmg = player.damage_gen()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You have attacked to " + enemies[enemy].name, "for",str(dmg) + " points of damages")
            player.increase_experience(500)
            if enemies[enemy].get_hp() == 0:
                print(BColors.OKGREEN + BColors.BOLD + "Enemy {} has been defeated.".format(enemies[enemy].name)
                      + BColors.ENDC)
                defeated_enemies.append(enemies[enemy])
                enemies.remove(enemies[enemy])
            result()

        elif index == 1:
            #Magic Option and selecting between available magics
            player.choose_magic()
            magic_choice = int(input("Choose magic: ")) - 1
            #Back to Main Menu using 0
            if magic_choice == -1:
                continue
            #Spell Damage Generation
            spell = player.magic[magic_choice]
            magic_dmg = spell.damage_gen()
            #Check whether player have enough magic power cost
            current_mp = player.get_mp()
            if current_mp < spell.cost:
                print(BColors.FAIL + "\nYou do not have enough MP\n", BColors.ENDC)
                continue
            #Reduce cost of magic choice from player's magic power
            player.reduce_mp(spell.cost)
            #Check whether magic's type is attack or heal
            if spell.type == "white":
                #heal player if its type is heal
                player.heal(magic_dmg)
                print(BColors.OKBLUE + "\n" + spell.name + ": heals for", str(magic_dmg), "HP" + BColors.ENDC)
                player.decrease_experience(200)
            elif spell.type == "black":
                #invade enemy if its type is attack
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(BColors.OKBLUE + "\n" + spell.name + ": deals", str(magic_dmg), "points of damages to "
                      + enemies[enemy].name + BColors.ENDC)
                player.increase_experience(350)
                if enemies[enemy].get_hp() == 0:
                    print(BColors.OKGREEN + BColors.BOLD + "Enemy {} has been defeated.".format(enemies[enemy].name)
                          + BColors.ENDC)
                    defeated_enemies.append(enemies[enemy])
                    enemies.remove(enemies[enemy])
                result()

        elif index == 2:
            #Whether player has enough experience
            if player.get_experience() < 800 :
                print("Player {} has not enough experience to use Items".format(player.name))
            else:
                #Item Option and selecting between available items
                player.choose_item()
                item_choice = int(input("Choose Item: ")) - 1
                #Get back to main Menu by writing 0 in terminal
                if item_choice == -1:
                    continue
                #Define selected item
                item = player.items[item_choice]
                if item.quantity == 0:
                    print(BColors.FAIL + "\nYou ran out of", item.name + " item\n" + BColors.ENDC)
                    continue
                # reduce quantity of used item
                item.reduce_quantity()
                #Implement selected item operation
                if item.type == "potion":
                    player.heal(item.prop)
                    print(BColors.OKGREEN + "\n" + item.name + ": heals for", str(item.prop), "HP" + BColors.ENDC)
                    player.decrease_experience(150)
                elif item.type == "elixir":
                    if item.name == "Mega Elixir":
                        for i in players:
                            i.hp = i.maxhp
                            i.mp = i.maxmp
                            print(BColors.OKGREEN + "\n" + item.name +
                                  ": Congrats! HP and MP of all players have fully restored" + BColors.ENDC)
                            player.decrease_experience(400)
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                        print(BColors.OKGREEN + "\n" + item.name + ": Congrats! Your HP and MP have fully restored"\
                              + BColors.ENDC)
                        player.decrease_experience(250)
                elif item.type == "attack":
                    enemy = player.choose_target(enemies)
                    enemies[enemy].take_damage(item.prop)
                    print(BColors.FAIL + "\n" + item.name + ": deals", str(item.prop), "points of damages to "
                          + enemies[enemy].name + BColors.ENDC)
                    player.increase_experience(200)
                    if enemies[enemy].get_hp() == 0:
                        print(BColors.OKGREEN + BColors.BOLD + "Enemy {} has been defeated.".format(enemies[enemy].name)
                              + BColors.ENDC)
                        defeated_enemies.append(enemies[enemy])
                        enemies.remove(enemies[enemy])
                    result()

    #Now it is enemy turn to invade player randomly
    for enemy in enemies:
        if enemy.get_hp() / enemy.get_max_hp() < 0.3:
            magic_choice = 2
            spell = enemy.magic[magic_choice]
            magic_dmg = spell.damage_gen()
            current_mp = enemy.get_mp()
            if current_mp < spell.cost:
                continue
            else:
                enemy.heal(magic_dmg)
        else:
            index = random.randrange(0, 2)
            if index == 0:
                #Attack Option
                enemy_dmg = enemy.damage_gen()
                target = random.randrange(0, len(players))
                players[target].take_damage(enemy_dmg)
                print("Enemy attacks to {} for {} point of damages".format(players[target].name, enemy_dmg))
                if players[target].get_hp() == 0:
                    print(BColors.FAIL + BColors.BOLD + "Enemies have defeated Player {}".format(players[target].name) + BColors.ENDC)
                    defeated_players.append(players[target])
                    players.remove(players[target])
                result()
            else:
                magic_choice = random.randrange(0,2)
                spell = enemy.magic[magic_choice]
                magic_dmg = spell.damage_gen()
                current_mp = enemy.get_mp()
                if current_mp < spell.cost:
                    continue
                else:
                    target = random.randrange(0, len(players))
                    players[target].take_damage(magic_dmg)
                    print("Enemy attacks to {} for {} point of damages".format(players[target].name, magic_dmg))
                    if players[target].get_hp() == 0:
                        print(BColors.FAIL + BColors.BOLD + "Enemies have defeated Player {}".format(
                            players[target].name) + BColors.ENDC)
                        defeated_players.append(players[target])
                        players.remove(players[target])
                    result()