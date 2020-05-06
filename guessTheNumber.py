# This is the guess the number game

import random

secretNumber = int(random.randint(1, 20))
maxNumberOfGuesses = 7

print ('I am thinking of a number between 1 and 20')

#ask user to take 6 guesses
for guessesTaken in range(1, maxNumberOfGuesses):
    print ('Take a guess')
    guess = int(input())

    if guess > secretNumber:
        print ('Your guess is too high!')
    elif guess < secretNumber:
        print ('Your guess is too low!')
    else:
        break


if guess == secretNumber:
    print ('Good job! You guessed my number in ' + str(guessesTaken) + ' tries!')
else:
    print('nope, the number I was thinking of was ' + str(secretNumber) + '.')
