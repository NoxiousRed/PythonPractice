print ('WELCOME TO THE MAXIMUM MAXIMUM MAXIMIZER FOR MAXIMUM MAXIMIZATION')
print ('ENTER THREE NUMBERS AND PREPARE TO BE MAXIMIZED')

while True:
    try:
        print ('\nENTER YOUR FIRST NUMBER')
        x = input()
        x = int(x)
        print ('\nENTER YOUR SECOND NUMBER')
        y = input()
        y = int(y)
        print ('\nENTER YOUR THIRD NUMBER')
        z = input()
        z = int(z)
        break
    except:
        print ('\nERROR, MAXIMUM MAXIMIZER REQUIRES THREE INTEGERS TO MAXIMIZE')
        continue

def maxOfThree ( x, y, z ):
    print ('\nYOUR MAXIMIZED NUMBER IS:')
    if x > y and x > z:
        print (x)
    if x < z and y < z:
        print (z)
    if x < y  and y > z:
        print (y)


maxOfThree( x, y, z)
    
    


