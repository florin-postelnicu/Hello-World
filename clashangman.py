

import pickle

class Player:
    def __init__(self, name , battles , victories):
        self.name = name
        self.battles = battles
        self.victories = victories

    def greetings(self):

        history = Player.get_warrior_infos(self)

        #  Check if the name is in the history.names
        # Use get_warrior_infos()

        if self.name in history.keys():
            self.battles = history[self.name][0]
            self.victories = history[self.name][1]
            Player.print_stats(self)
            # self.get_warrior_infos()
        else :

            # No call the Setters
            Player.set_warrior_infos(self)
            history[self.name] = (0,0)
            f1 = open('historydict,p', 'wb')
            pickle.dump(history, f1)
            f1.close()
            Player.print_stats(self)
            print("Sorry valiant warrior, but we don't believe in Fairy Tales, \n"
                  " however,  \n we want you to prove yourself and get into"
                  " our history book. Good Luck!")
        print("History book : \n", history)

    # Define Getters

    def get_warrior_infos(self):
        # Read the file "historydict", and return the dictionary history
        self.name = input("Enter your name warrior! \n")
        print(self.name)
        f1 = open('historydict,p', 'rb')
        history = pickle.load(f1)
        f1.close()
        return history

    # Define Setters For newbies
    def set_warrior_infos(self):
        print("What's your story {}  warrior? \n".format(self.name))
        self.battles = int(input("Enter your skirmishes big warrior \n"))
        self.victories = int(input("Enter the number of annihilated enemies \n"))

    def print_stats(self):
        print("Warrior ", self.name)
        print("Lots of battles ", self.battles)
        print("Lots of winning scars ", self.victories)
    def all_warriors(self):
        pass



Player.greetings(Player)
# player1 = Player("Moody", 35, 12)
# Player.print_stats(player1)
# p2 = Player
# Player.set_warrior_infos(p2)
# Player.print_stats(p2)


