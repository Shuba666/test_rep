import random as r

hp = 0
coins = 0
damage = 0

def printParametr():
    print("У тебя {0} hp, {1} coins, {2} damage".format(hp, coins, damage))

def initGame (initHp, initCoins, initDmg):
    global hp
    global coins
    global damage

    hp = initHp
    coins = initCoins
    damage = initDmg

print("Вы просыпайтесь в лесу")


def gameLoop():
    sit = r.randint(0, 10)
    if sit == 0:
        input("вы в лесу")
    elif sit == 1:
        input("вы в аэропорту")
    else:
        input("вы все еще дома, типа может что-то нужно нажать?")

initGame (3, 5, 1)

while True:
    gameLoop()

    if hp <=0:
        if input("Начнем наше приключение с начала (да/нет): ").lower() == "да":
            initGame(3, 5, 1)
        else:
            break
