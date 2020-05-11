primaryList = []

def sumOfAList(primaryList):
    totalInList = int(input('How many numbers? : '))
    for i in range(totalInList):
        numbers = int(input('Enter a number: '))
        primaryList.append(numbers)
    print('\nSum of the numbers given: ' + str(sum(primaryList)))    
    
    
sumOfAList(primaryList)    