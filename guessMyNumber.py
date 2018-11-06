import random
secret = random.randint(1,99)

guess = 0
tries = 0
print("Can you guess my  secret number?")
print("It is a number between 1 and 99. You have 6 tries.")

while guess!=secret and tries<6:
    print("What's your guess?")
    guess = int(input())
    if guess< secret:
        print("Too low!")
    elif guess > secret:
        print("Too high")
    tries = tries + 1

if guess == secret:
    print("You got it! Bravo!")
else :
    print("No more guesses! Try again!")
    print('The secret number was ; ', secret)
