
import pickle


class Player:
    def __init__(self, name , battles , victories):
        self.name = name
        self.battles = battles
        self.victories = victories

    def greetings(self):
        # self.get_warrior_infos()
        self.name = input("Enter your name warrior! \n")
        print(self.name)
        history = Player.get_warrior_infos(self)

        #  Check if the name is in the history.names
        # Use get_warrior_infos()

        if self.name in history.keys():
            self.battles = history[self.name][0]
            self.victories = history[self.name][1]

        else:

            # No, call the Setters
            Player.set_warrior_infos(self)
            history[self.name] = (0,0)
            f1 = open('historydict,p', 'wb')
            pickle.dump(history, f1)
            f1.close()

            print("Sorry valiant warrior, but we don't believe in Fairy Tales, \n"
                  " however,  \n we want you to prove yourself and get into"
                  " our history book. Good Luck!")
            Player.update_warrior(self, vic=None)
        Player.print_stats(self)
        Player.print_all_warriors(self)

    # Define Getters 

    @staticmethod
    def get_warrior_infos(self):
        # Read the file "historydict", and return the dictionary history
        f1 = open('historydict,p', 'rb')
        history = pickle.load(f1)
        f1.close()
        return history

    # Define Setters For newbies
    def set_warrior_infos(self):
        print("What's your story {}  warrior? \n".format(self.name))
        self.battles =0
        int(input("Enter your skirmishes big warrior \n"))
        self.victories =0
        int(input("Enter the number of annihilated enemies \n"))

    def print_stats(self):
        print("Warrior ", self.name)
        print("Lots of battles ", self.battles)
        print("Lots of winning scars ", self.victories)

    def update_warrior(self, vic):
        history = Player.get_warrior_infos(self)
        if self.name in history.keys() and vic is not None:

            # Update victories
            if vic :
                self.victories += 1
                # Update battles
                self.battles += 1
            else:
                self.victories += 0
                # Update battles
                self.battles += 1

        history[self.name] = (self.battles, self.victories)
        f1 = open('historydict,p', 'wb')
        pickle.dump(history, f1)
        f1.close()
        Player.print_stats(self)

    def print_all_warriors(self):
        history = Player.get_warrior_infos(self)
        print("History book : \n", history)
