import random
import pickle
from dungeon import Dungeon
from fight import clearTerm
from player import Player
from questSystem import ChurchQuest


class Session:
    MAP = {
        "Bridlerry" : ["Colwes"],
        "St. Thamesheath" : ["Colwes"],
        "Colwes" : ["Bridlerry", "St. Thamesheath", "Stonehod"],
        "Stonehod" : ["Colwes", "Houthend", "Peleigh", 'Gernard'],
        "Peleigh" : ["Stonehod"],
        "Houthend" : ["Stonehod"],
        "Gernard" : ["Stonehod", "Hulkingford", "Lenscliffe"],
        "Hulkingford" : ["Gernard", "Tunbright"],
        "Tunbright" : ["Hulkingford", "Wellin"],
        "Wellin" : ["Tunbright", "Lenscliffe"],
        "Lenscliffe" : ["Gernard", "Wellin", "Tothet"],
        "Tothet" : ["Lenscliffe", "Surstead"],
        "Surstead" : ["Tothet"]
    }

    QUESTTOWNS = {
        "St. Thamesheath" : ChurchQuest()
    }

    GEAR = {
        "Dull Sword" : [5, 100],
        "Sharp Sword" : [8, 180],
        "The Razor™" : [12, 250],
    }

    with open("text/barkeepSpeak.txt", "r") as f:
        BKTEXT = f.readlines()
        f.close()

    with open("text/customerSpeak.txt", "r") as f:
        CUSTOMERTEXT = f.readlines()
        f.close()


    def __init__(self, player : Player):
        self.player = player
        
    
    def moveToTowns(self):
        print(f"Your Current destination is {self.player.curDest}\n", "Where do you want to move to?")
        towns = ""
        curDest = self.MAP[self.player.curDest]
        for t in range(len(curDest)):
            if t < len(curDest) - 1:
                towns += curDest[t] + ", "
            else:
                towns += curDest[t] + "?"
        i = input(towns + "\n> ")

        for town in self.MAP[self.player.curDest]:
            if town.lower() == i:
                self.player.curDest = i
                self.player.drunkness -= 1 if self.player.drunkness > 0 else 0
                return
        
        clearTerm()
        return self.moveToTowns()

    def shop(self):
        print(f"What do you want to buy? You have {self.player.coins} coins")

        itemName = {}

        for i, item in enumerate(self.GEAR):
            print(f"{item} - DMG = {self.GEAR[item][0]} - Costs = {self.GEAR[item][1]}")
            itemName[i] = item
        i = input("Enter the number, starting from 0, of the item you wish to have (E to exit)\n> ")

        if i.capitalize() != "E":
            i = int(i)
            if self.player.coins >= self.GEAR[itemName[i]][1]:
                self.player.coins -= self.GEAR[itemName[i]][1]
                self.player.changeGear(self.GEAR[itemName[i]][0], self.GEAR[itemName[i]][1])
                clearTerm()
                print("Item Purchased!")
            else:
                clearTerm()
                print("You can't buy that")
                return self.shop()
        else:
            print("Exited Store")
            return

    def changeQuest(self):
        print("There is a quest in this town. Do you want to claim it?")
        i = input("Y/N\n> ")
        
        match i.capitalize():
            case "Y":
                clearTerm()
                self.player.quest = self.QUESTTOWNS[self.player.curDest].NAME
                self.player.questOBJ = self.QUESTTOWNS[self.player.curDest]
                self.player.questOBJ.questInfo()
            case "N":
                return
            case _:
                clearTerm()
                self.changeQuest()

    def townInteraction(self):
        if self.player.curDest in self.QUESTTOWNS:
            if self.player.quest == self.QUESTTOWNS[self.player.curDest].NAME:
                print(f"Current Quest Progress: {self.player.questOBJ.checkQuest()} kills")
            else:
                self.changeQuest()

        print(f"You are in {self.player.curDest}\nWhat do you want to do here?\nShop, Travel, Save or visit the Bar")
        i = input("S, T, W or B?\n> ")

        clearTerm()
        match i.capitalize():
            case "S":
                self.shop()
            case "T":
                self.moveToTowns()
            case "W":
                pickle.dump(self.player, open("saves/player", "wb"))
                clearTerm()
                print("Saved!\n")

            case "B":
                self.barInteraction()
            case _:
                return self.townInteraction()
    
    def barInteraction(self):
        print(f"You are in the {self.player.curDest} Bar. What do you want to do?\n- Talk to the barkeep\n- Talk to the people within\n- Buy a drink (10 coins, Effects stats negetively)\n- Exit the bar")
        i = input("B, T, D or E?\n> ")

        clearTerm()
        match i.capitalize():
            case "B":
                print("Barkeep: ", random.choice(self.BKTEXT))
                return self.barInteraction()
            case "T":
                print("Customer: ", random.choice(self.CUSTOMERTEXT))
                return self.barInteraction()
            case "D":
                if self.player.coins < 10:
                    return self.barInteraction()
                else:
                    if self.player.drunkness < 5:
                        print("You take a chug (Drink responsibly)")
                        self.player.drunkness += 1
                        return self.barInteraction()
                    else:
                        print("You are too wasted, so the barkeeper kicks you out")
                    
            case "E":
                print("You leave the bar")
            case _:
                return self.barInteraction()

    def dungeonEncounter(self):
        print(f"You have encountered a dungeon enroute to {self.player.curDest}\nDo you want to Enter?")
        i = input("Y/N\n> ")

        match i:
            case "Y":
                d = Dungeon(self.player)
                d.run()
                del d
            case "N":
                print("Wuss..")
                return
            case _:
                self.dungeonEncounter()

    def run(self):
        r = random.randrange(0, 100)
        if  r < 20:
            self.dungeonEncounter()
        else:
            self.townInteraction()
        
        clearTerm()
        self.run()