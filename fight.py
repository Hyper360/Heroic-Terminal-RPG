import random
import os
from player import Player

ENEMIES = ["Orc", "Goblin", "Boar", "Giant Spider", "Skeleton"]

def clearTerm():
    os.system('cls' if os.name == 'nt' else 'clear')

def fight(player : Player):
    enemyHP = random.randrange(100, 200, 5)
    enemyDMG = random.randrange(5, 20)
    enemyName = random.choice(ENEMIES)
    fighting = True

    print(f"{enemyName} Approaches!")

    def attack():
        print("Attack (A), Critical (C) or Guard (G)?")
        i = input("Input A, C or G\n> ")

        clearTerm()
        match i.capitalize():
            case "A":
                return 1
            case "C":
                return 2
            case "G":
                return 3
            case _:
                return attack()
    
    def defend():
        print("Dodge (D) or Take The Hit (H)?\n(Warning: Failure to dodge will result in a penalty)")
        i = input("Input D or H\n> ")

        clearTerm()
        match i.capitalize():
            case "D":
                if random.randrange(0, 101) < 20:
                    return 1
                else:
                    return 2
            case "H":
                return 3
            case _:
                return defend()
            
    
    def checkWinner():
        if enemyHP <= 0:
            player.hp = player.initHp
            if player.questOBJ != None:
                if player.questOBJ.progressQuest() == 1:
                    player.coins += player.questOBJ.reward
                    player.quest = ""
                    player.questOBJ = None
            return 1
        elif player.hp <= 0:
            return 2
        else:
            return 0


    def printStats():
        print(f"Player: \nHP = {player.hp}/{player.initHp}\nDMG = {player.dmg}\nDefence = {player.defence}\nAgility = {player.agility}")
        print(f"{enemyName}: \nHP = {enemyHP}\nDMG = {enemyDMG}")

    
    while fighting:
        c = checkWinner()
        if c != 0:
            return c
        a = attack()
        if a == 1:
            enemyHP -= random.randrange(int(player.dmg * 0.95), int(player.dmg * 1.95)) if random.randrange(0, 101) > (player.drunkness * 2) else 0
        elif a == 2:
            if random.randrange(0, 101) < 15:
                enemyHP -= random.randrange(int(player.dmg * 0.95), int(player.dmg * 1.95)) * 1.5 if random.randrange(0, 101) > (player.drunkness * 2) else 0
            else:
                player.takeDamage(random.randrange(int(player.dmg * 0.95), int(player.dmg * 1.95)) // 2)
        elif a == 3:
            player.gainDefence(random.randrange(int(player.hp * 0.05), int(player.hp * 0.10)))

        printStats()

        c = checkWinner()
        if c != 0:
            return c
        d = defend()
        if d == 1:
            pass
        elif d == 2:
            player.takeDamage(random.randrange(int(enemyDMG * 0.95), int(enemyDMG * 1.95)) * 1.5)
        elif d == 3:
            player.takeDamage(random.randrange(int(enemyDMG * 0.95), int(enemyDMG * 1.95)))

        printStats()