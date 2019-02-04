
import random
from hangman_list import text_w


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


again = 'y'
while again == 'y':

        # Chose a random word from the text_w
    index = random.randint(0, len(text_w))
    word = text_w[index]

    secret_word = list(word)
    # print(secret_word)
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
    again = input('Enter y to play again, else n \n')


print('Thank you for playing the Hangman! See you!')
exit()



