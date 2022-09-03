import random


def RollDice():
    roll = random.randint(1, 100)
    if roll == 100:
        print('roll was 100. you lose, what are the odds! play again')
        return False
    elif roll <= 50:
        print('you lose roll was 1-50')
        return False
    elif 100 > roll > 50:
        print('you win! hurray')
        return True


def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager
    
    curr_wager = 0
    while curr_wager < wager_count:
        if RollDice():
            value += wager
        else:
            value -= wager
        curr_wager += 1
        print('funds : ', value)
simple_bettor(10000, 100, 100)
    
