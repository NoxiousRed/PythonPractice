primaryList = []

def multOfAList(primaryList):
    total = 1
    totalInList = int(input('How many numbers? : '))
    for i in range(totalInList):
        numbers = int(input('Enter a number: '))
        primaryList.append(numbers)
    for i in primaryList:
        total*=i
    print('\nProduct of the numbers given: ' + str(total))  
    
    
multOfAList(primaryList)    