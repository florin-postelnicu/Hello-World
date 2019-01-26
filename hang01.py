
word = 'hangman'
secret_word = list(word)
guess_word = []
for i in range(len(secret_word)):
    guess_word.append('*')


penalty = 0
list_letters = []


while "*" in guess_word and penalty < 7:
    guess = input('Enter your guess letter')

    if guess not in secret_word:
        penalty += 1

    if guess  in list_letters:
        penalty += 1

    else:
        for i in range(len(secret_word)):
            if guess == secret_word[i]:
                guess_word[i] = secret_word[i]
    list_letters.append(guess)
    print('penalty = ', penalty)
    print(list_letters)
    print(guess_word)
print('End Game')
exit()
