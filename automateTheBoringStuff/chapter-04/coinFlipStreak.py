import random

def flipCoin():
    return ["H" if random.randint(0,1)==0 else "T" for i in range(100)]

def hasStreak(coinFlips):
    for i in range(len(coinFlips)-5):
        if( all(coinFlips[i+j] == coinFlips[i] for j in range(1 , 6))):
            return True
    return False

streaks = 0

for _ in range(10000):
    if hasStreak(flipCoin()):
        streaks+=1


print(streaks/100)