import random


# Code that creates a list of 100 'heads' or 'tails' values.
def experimentTrial():
    heads=0
    tails=0    
    numberOfStreaks = 0
    for experimentNumber in range(10000):
        for experimentTrial in range(100):
            coinFlip = random.randint(0, 1)
            if coinFlip == 0:
                #print(heads)
                heads = heads + 1
            if(heads==6):
                heads=0
                numberOfStreaks = numberOfStreaks + 1
            elif coinFlip == 1:
                #print(tails)    
                tails = tails + 1
            if(tails==6):
                tails=0
                numberOfStreaks = numberOfStreaks + 1
        return numberOfStreaks          
                  
    

experimentTrial()
    
    
print('Chance of streak: %s%%' % (experimentTrial() / 100))

