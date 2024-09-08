class Player():
    def __init__(self, hp : int, damage : int):
        self.hp = self.initHp = hp
        self.agility = 20
        self.dmg = damage
        self.defence = self.defenceGain = 0
        self.curDest = "Gernard"
        self.prevDest = None
        self.gear = ["", 0]
        self.coins = 600
        self.drunkness = 0
        self.quest = ""
        self.questOBJ = None
    
    def changeGear(self, name : str, stat : int):
        self.dmg -= self.gear[1]

        self.gear = [name, stat]
        self.dmg += self.gear[1]

    def gainDefence(self, baseGain : int):
        baseGain *= (self.defenceGain * 0.01) if self.defenceGain > 0 else 1
        self.defence += baseGain

    def takeDamage(self, damage : int):
        carryOver = abs(self.defence - damage)
        self.defence = self.defence - damage if self.defence - damage >= 0 else 0

        if self.hp - (damage + carryOver) < 0:
            self.hp = 0
        else:
            self.hp -= (damage + carryOver)