'''
To start for the first time the Hangman game 
one needs to create a starting 'memory' file  historydict,
that should have at least one entry:
history = {'Anonymous':(0,0)}
These lines should be added to the beggining of the program 
containing the class Player (clashangman):
f1 = open('historydict,p', 'wb')
pickle.dump(history, f1)
f1.close()

f1 = open('historydict,p', 'rb')
history = picle.load(f1)
f1.close()

After the first run, thes lines could be erased, since the 'memory'
has been created.
'''

import random
from hangman_list import text_w
from clashangman import Player


def gallows(penal):
    if penal == 0 :
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 1:
        gal = "---------I \n" \
              "  I      I \n" \
              " O      I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal ==2 :
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   2    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"

    if penal == 3:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   3    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 4:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   4    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 5:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   5    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 6:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   6    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    if penal == 7:
        gal = "---------I \n" \
              "         I \n" \
              "         I \n" \
              "         I \n" \
              "   7    I \n" \
              "         I \n" \
              "        / \  \n" \
              "       /   \  \n" \
              "      ====  \n"
    return gal
player1 = Player
player1.greetings(player1)
again = 'y'
while again == 'y':

    # Chose a random word from the text_w

    index = random.randint(0, len(text_w))
    word = text_w[index]

    secret_word = list(word)
    print(secret_word)
    new_word = ['*' for i in range(len(secret_word))]
    print(new_word)
    penalty = 0
    letters_used = []
    while '*' in new_word and penalty < 7:

        guess = input ('Enter a letter  \n')
        if guess not in secret_word or guess in letters_used:
            penalty += 1
        else:
            for i in range(len(secret_word)):
                if guess == secret_word[i]:
                    new_word[i] = secret_word[i]
        letters_used.append(guess)
        print(letters_used)
        print('penalty ', penalty) # Here will be placed the gallows call
        print(gallows(penalty))
        print(new_word)

    print('The End')
    if penalty < 7:
        wiky = True
    else:
        wiky = False
    Player.update_warrior(player1, wiky)
    again = input('Enter y if you want to play another game, else enter n \n')

print("Good by, See you again!")
exit()



