import random
import pickle
from player import Player
from fight import fight, clearTerm
from upgrade import upgrade

class Dungeon:
    # r = random.randrange(1, 4)
    GRID = pickle.load(open(f"dungeons/d{3}", "rb"))
    # print(r)

    def __init__(self, player : Player):
        self.player = player
        self.playerPos = None

        for r in range(len(self.GRID)):
            for c in range(len(self.GRID[r])):
                if self.GRID[r][c] == "P":
                    self.playerPos = [c, r]
        if not self.playerPos:
            print("An error has occured")
            quit()
    
        self.active = True
        with open("text/messages.txt", "r") as f:
            self.messages = f.readlines()
            f.close()

    def checkMove(self):
        self.GRID[self.playerPos[1]][self.playerPos[0]] = "P"
        for r in self.GRID:
            for c in r:
                print(" " + c + " ", end="")
            print("\n")
        print("Where do you want to move? UP, DOWN, LEFT, or RIGHT?")

        i = input("U, D, L or R?\n> ")

        clearTerm()
        match i.capitalize():
            case "U":
                if self.GRID[self.playerPos[1] - 1][self.playerPos[0]] == " ":
                    self.GRID[self.playerPos[1]][self.playerPos[0]] = " "
                    self.playerPos[1] -= 1
                elif self.GRID[self.playerPos[1] - 1][self.playerPos[0]] == "E":
                    return 1
                else:
                    return self.checkMove()
            case "D":
                if self.GRID[self.playerPos[1] + 1][self.playerPos[0]] == " ":
                    self.GRID[self.playerPos[1]][self.playerPos[0]] = " "
                    self.playerPos[1] += 1
                elif self.GRID[self.playerPos[1] + 1][self.playerPos[0]] == "E":
                    return 1
                else:
                    return self.checkMove()
            case "L":
                if self.GRID[self.playerPos[1]][self.playerPos[0] - 1] == " ":
                    self.GRID[self.playerPos[1]][self.playerPos[0]] = " "
                    self.playerPos[0] -= 1
                elif self.GRID[self.playerPos[1]][self.playerPos[0] - 1] == "E":
                    return 1
                else:
                    return self.checkMove()
            case "R":
                if self.GRID[self.playerPos[1]][self.playerPos[0] + 1] == " ":
                    self.GRID[self.playerPos[1]][self.playerPos[0]] = " "
                    self.playerPos[0] += 1
                elif self.GRID[self.playerPos[1]][self.playerPos[0] + 1] == "E":
                    return 1
                else:
                    return self.checkMove()
            case _:
                return self.checkMove()
            
    def run(self):
        if self.checkMove() == 1:
            self.active = False

        if random.randrange(0, 10) < 2:
            if fight(self.player) == 1:
                clearTerm()
                print("YOU WIN!")
                coins = random.randrange(10, 36)
                print(f"You get {coins} coins!")
                self.player.coins += coins
                upgrade(self.player)
                clearTerm()
            else:
                clearTerm()
                print("You Died...")
                quit()
        else:
            print(random.choice(self.messages))

        self.run() if self.active == True else 0

d = Dungeon(Player(10, 10))