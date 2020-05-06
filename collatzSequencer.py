print ('WELCOME TO THE COLLATZ SEQUENCER: ALWAYS NUMBER 1')
print ('ENTER YOUR NUMBER AND PREPARE TO GET SEQUENCED')
numberToSequence = input()  

def tryCollatz(numberToSequence):
    collatzCalled = False
    while(collatzCalled == False):
        try:    
            numberToSequence = int(numberToSequence)
            collatz(numberToSequence)
            collatzCalled = True
        except:
            print ('Error: Value input must be an INTEGER')
            numberToSequence = input()

def collatz(numberToSequence):
    while numberToSequence != 1:
        if numberToSequence % 2 == 0:
            numberToSequence = numberToSequence // 2
            print (numberToSequence)
        elif numberToSequence % 2 == 1:
            numberToSequence = 3 * numberToSequence + 1
            print (numberToSequence)
    
    
tryCollatz(numberToSequence)



    