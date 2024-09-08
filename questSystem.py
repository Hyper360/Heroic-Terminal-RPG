from fight import clearTerm

class ChurchQuest():
    NAME = "Church Quest"
    def __init__(self):
        self.kills = 0
        self.target = 1
        self.active = False
        self.reward = 400

    def questInfo(self):
        print('''*You enter a grand looking church in the center of town*\n
*A man in a long robe greets you at the door to the church*\n
Welcome brother to our humble abode, where we worship the ever-powerful God Aurelius. Would you like to join our body of people?\n
*After a long pause, the man continues*\n
Ahh, I see. Well can you least help our cause? Our everlasting God has bestowed monsters amoung us to create struggle on earth\n
This struggle makes us stronger, and I sense a deep power within you. If you can kill 10 monsters, the church will be grateful.''')

    def checkQuest(self):
        return self.kills

    def progressQuest(self):
        if self.active == True:
            self.kills += 1
        
        print(f"Quest Progression: {self.checkQuest()}")
        if self.kills == self.target:
            print(f"You have completed this quest. You have recieved {self.reward} coins as a reward.")
            return 1

        return 0
    
    def resetQuest(self):
        self.kills = 0