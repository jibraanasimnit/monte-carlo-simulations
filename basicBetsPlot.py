import random
import matplotlib.pyplot  as plt
def RollDice():
    roll = random.randint(1, 100)
    if roll == 100:
        # print('roll was 100. you lose, what are the odds! play again')
        return False
    elif roll <= 50:
        # print('you lose roll was :', roll)
        return False
    elif 100 > roll > 50:
        # print('you win! hurray')
        return True



def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    wX = []
    vY = []
    curr_wager = 1
    while curr_wager <= wager_count:
        if RollDice():
            value += wager
            wX.append(curr_wager)
            vY.append(value)
        else:
            value -= wager
            wX.append(curr_wager)
            vY.append(value)
        curr_wager += 1
    plt.plot(wX,vY)
    
x = 0
while x < 100:
    simple_bettor(10000, 1000, 10000)
    x +=1 
    plt.ylabel('account value')
    plt.xlabel('wager count')
    plt.show
    
