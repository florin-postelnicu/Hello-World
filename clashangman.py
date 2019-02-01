

import pickle

class Player:
    def __init__(self, name , battles , victories):
        self.name = name
        self.battles = battles
        self.victories = victories

    def greetings(self):
        self.name = input("Enter your name warrior! \n")
        print(self.name)
        f1 = open('historydict,p', 'rb')
        history = pickle.load(f1)
        f1.close()

        #  Check if the name is in the history.names
        # Use get_warrior_infos()

        if self.name in history.keys():

            # Yes call the Getters
            self.battles = history[self.name][0]
            self.victories = history[self.name][1]
            Player.print_stats(self)
            # self.get_warrior_infos()
        else :

            # No call the Setters
            Player.set_warrior_infos(self)
            history[self.name] = (self.battles, self.victories)
            f1 = open('historydict,p', 'wb')
            pickle.dump(history, f1)
            f1.close()
            Player.print_stats(self)
        print(history)

    # Define Getters

    def get_warrior_infos(self):
        # Read the file "History", and check if the name of the player it is
        # already in
        pass

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


