
from florinlib import translate
from storytext import text


mynewdict = {'Dr.':'Doctor', 'Mr.': "Mister", 'fishes': 'fish', 'friend,': 'bro'}
new_text = translate(text, mynewdict).split('.')
for sentence in new_text:
    print(sentence, end='.\n') # the \n (back slash n) makes the cursor jump to the next line