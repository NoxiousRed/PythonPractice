import sys
primaryList = ['tofu']

def commaCode(primaryList): 
    if len(primaryList)>1:
        for i in range(len(primaryList) - 2):
                print(primaryList[i], end=', ')
        print(primaryList[len(primaryList) - 2] + ' and ' + primaryList[len(primaryList) - 1]) 
    elif len(primaryList)==1:
        print(primaryList)
    else:
        print('Error')
        sys.exit()
            
commaCode(primaryList)