
import random
# from storytext import text


def gallows(penal):

    if penal == 0:
        draw = '--------I\n' \
               '        I\n' \
               '        I\n' \
               ' 0      I\n' \
               '        I\n' \
               '        I\n' \
               '        I\n' \
               '        /\ \n ' \
               '      /  \ \n '

        return  draw

    if penal == 1:
        draw = '--------I\n' \
               '        I\n' \
               '        I\n' \
               '  1     I\n' \
               '        I\n' \
               '        I\n' \
               '        I\n' \
               '        /\ \n ' \
               '      /  \ \n '

        return draw

    if penal == 2:
        draw = '--------I\n' \
               '        I\n' \
               '        I\n' \
               '  2     I\n' \
               '        I\n' \
               '        I\n' \
               '        I\n' \
               '        /\ \n ' \
               '      /  \ \n '

        return draw

    if penal == 3:
        draw = '--------I\n' \
               '        I\n' \
               '        I\n' \
               '  3     I\n' \
               '        I\n' \
               '        I\n' \
               '        I\n' \
               '        /\ \n ' \
               '      /  \ \n '

        return draw

    if penal == 4:
        draw = '--------I\n' \
               '        I\n' \
               '        I\n' \
               '  4     I\n' \
               '        I\n' \
               '        I\n' \
               '        I\n' \
               '        /\ \n ' \
               '      /  \ \n '

        return draw

    if penal == 5:
        draw = '--------I\n' \
               '        I\n' \
               '        I\n' \
               '  5     I\n' \
               '        I\n' \
               '        I\n' \
               '        I\n' \
               '        /\ \n ' \
               '      /  \ \n '

        return draw

    if penal == 6:
        draw = '--------I\n' \
               '        I\n' \
               '        I\n' \
               '  6     I\n' \
               '        I\n' \
               '        I\n' \
               '        I\n' \
               '        /\ \n ' \
               '      /  \ \n '

        return draw

    if penal == 7:
        draw = '--------I\n' \
               '        I\n' \
               '        I\n' \
               '  7     I\n' \
               '        I\n' \
               '        I\n' \
               '        I\n' \
               '        /\ \n ' \
               '      /  \ \n '

        return draw

# word = text[random.randint(len(text))]


word = 'hangman'
secret_word = list(word)
guess_word = ['*' for i in range(len(secret_word))]

penalty = 0
list_letters = []

while "*" in guess_word and penalty < 7:
    guess = input('Enter your guess letter')

    if guess not in secret_word or guess in list_letters:
        penalty += 1

    else:
        for i in range(len(secret_word)):
            if guess == secret_word[i]:
                guess_word[i] = secret_word[i]
    list_letters.append(guess)
    print('penalty = ', penalty)
    print(list_letters)
    print(guess_word)
    print(gallows(penalty))
print('End Game')
exit()
