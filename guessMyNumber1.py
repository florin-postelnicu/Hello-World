'''
Documentation
'''

import random

again = 'y'

while again == 'y':
    secret = random.randint(1, 99)

    guess = 0
    tries = 0
    print("Can you guess my number?")
    print("My number is an integer between 1 and 99")

    while guess != secret and tries < 6 :
        print("What is your guess?")
        guess = int(input())
        if guess < secret :
            print("Too Low")
        elif guess > secret :
            print("Too high")

        tries = tries + 1

    if guess == secret:
        print("You got it man! Bravoooo!")
    else :
        print("No more guesses! Try again")
        print("The secret number was : ", secret)
    print(" Do you want to play a game  y/n ?")
    again = input(" Enter your choice \n")

print("Game Over")
exit()
