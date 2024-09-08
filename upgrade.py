from player import Player

def upgrade(player : Player):
    print("What do you want to upgrade?\nHealth += 5%\nAgility += 5%\nDefence Gain += 5%")
    i = str(input("H, A or D?\n> "))

    match i.capitalize():
        case "H":
            player.initHp *= 1.05
            player.initHp = round(player.initHp, 2)
            player.hp = player.initHp
        case "A":
            player.agility *= 1.05
            player.initHp = round(player.agility, 2)
        case "D":
            player.defenceGain *= 1.05
            player.initHp = round(player.defenceGain, 2)
