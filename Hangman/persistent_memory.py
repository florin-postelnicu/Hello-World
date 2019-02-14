'''
-- Create a a file to save on the memeory(history)
-- Write on the file for Persistent Memory
-- Read from the file with Persistent Memory

'''

import pickle


def rate_of_winning(dict, player):
    rate = dict[player][1]/dict[player][0]
    return print("The rate of winning for  ", player, ' is ', round(rate, 2))


# Key = Name of player, Value is a tuple( # games played, # victories)
# history = { 'Archy': (12, 4), 'Betty': (10, 6)}

# file_p5 = open('myhistorypickle,p', 'wb')
# pickle.dump(history, file_p5)
# file_p5.close()


# Readt to file

file_p5 = open('myhistorypickle,p', 'rb')
history = pickle.load(file_p5)
file_p5.close()

print(history)
# history['Clarissa'] = (90, 85)
# print(history)
#
# # update the mydictionarypickle
#
# file_p5 = open('myhistorypickle,p', 'wb')
# pickle.dump(history, file_p5)
# file_p5.close()