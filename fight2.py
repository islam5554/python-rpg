#start the fight

import random
import time
from player import player
from player import enemie
player_name = input("enter your player name: ")
my_player = player(player_name, 100,True)
boss2 = enemie("modzilla",200,True)
weapons =  {
    "sword":20,
    "gun":30,
    "bandage":20
}
print("you are fighting the second boss modzilla".center(100))
print(f"you have {weapons} to fight him")
#player attack mechanic
while True:  
    while True:
            attack = input("choose you attack weapon: ").lower()
            if attack not in weapons:
                print("invalid input")
                continue
            elif attack == "bandage":
                my_player.health += weapons[3]
                print("your health: " + str(my_player.health))
                print("the boss health: " + str(boss2.health))
                break
            else:
                attack_damage = int(weapons[attack])
                boss2.health -= attack_damage
                print(f"you deal to the boss {attack_damage}")
                print("your health: " + str(my_player.health))
                print("the boss health: " + str(boss2.health))
                break
        #boss attack mechanique


    boss_weapons = {
        "spit": 30,
        "tail attack": 20,
        "smash": 35
    }
    time.sleep(2)
    boss_attack = random.choice(list(boss_weapons))  # Convert keys to list explicitly
    boss_damage = boss_weapons[boss_attack]  # No need for int(), values are already int

    print(f"The attack that boss chose is: {boss_attack}")

    my_player.health -= boss_damage

    print("Your health: " + str(my_player.health))
    print("The boss health: " + str(boss2.health))
    if my_player.health == 0:
        my_player.alive = False
        print("you lose")
        break
    if boss2.health == 0:
        boss2.alive = False
        print("you win")
        break
    else:
        continue