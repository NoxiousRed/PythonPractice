print ('Enter your name: ')
name = input()

print ('Enter your age: ')
age = input()
age = int(age)

if name == 'Alice':
    print('Hi Alice!')
elif age < 12:
    print ('You are not Alice kiddo')
elif age > 2000:
    print ('unlike you, Alice is not an undead, immortal vampire')
elif age > 100:
    print ('you are not Alice, Granny')