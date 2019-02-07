

'''
class example
'''


class CashRegister:

    def __init__(self):
        self.items = 0
        self.price = 0

    def update_register(self, price):
        self.items += 1
        self.price += price

    def display_record(self):
        return print('total price = ', self.price, 'Number of items = ', self.items)

    def clear_register(self):
        self.items = 0
        self.price = 0


def main():

    reg1 = CashRegister()
    reg1.update_register(29.25)
    reg1.update_register(12.75)
    reg1.display_record()





if __name__ == '__main__':
    main()