'''
Resources :

https://www.python-course.eu/python3_loops.php

Swap two variables  using a temporary variable:

given x, y
Create temp = x
Reassign :
x = y ( The value of var x is now the value of y)
y = temp ( The value in var y is temp, which is the former value in x, before reassignment)



'''

import random
x= 1
while x < 10:
    print(x)
    x += 1
x = 1
y = 1
while x < 10:
    while y < 5:
        print ( x,y,' ', end='')
        y = y +1
    print()
    x = x + 1
    y = 1

# Guessing a number



n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("New number: "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you're giving up!")
        break
else:
    print("Congratulation. You made it!")

#
# Fibonacci Numbers using reassigning variables


x = 1
y = 1

cont = 'c'
while cont =='c':
    print("A fibon number: ", x+y)
    temp = x

    x = y
    y = temp + y

    cont = input('if continuu press c, else press any other key')
