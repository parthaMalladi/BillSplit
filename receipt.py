from user import User

class Receipt:
    # constructor takes in a list of pairs: [item name, price]
    # creates two maps, one with (item name, price) and one with (item name, count)
    def __init__(self, items):
        self.prices = {}
        self.count = {}
        self.users = []
        
        for item, price in items:
            self.prices[item] = price
            
            if item not in self.count:
                self.count[item] = 0
            
            self.count[item] += 1
    
    # adds an item to the receipt, replaces if item already exists
    def addItem(self, item, price, count):
        self.prices[item] = price
        self.count[item] = count
    
    # removes count of an item
    # if count drops below 0, removes item from the receipt
    def removeItem(self, item, count):
        if item not in self.count:
            print("Item " + item + " does not exist")
            return
        
        self.count[item] -= count
        if self.count[item] <= 0:
            self.count.pop(item, None)
            self.prices.pop(item, None)
    
    # adds a user to the receipt
    def addUser(self, first, last):
        temp = User(first, last)
        self.users.append(temp)
    
    # removes user from receipt
    def removeUser(self, first, last):
        userFound = False
        
        for i, user in enumerate(self.users):
            if user.firstName == first and user.lastName == last:
                userFound = True
                self.users.pop(i)
        
        if not userFound:
            print("User with the name " + first + " " + last + " does not exist")

    # prints all items on the receipts include name, count, price
    def __str__(self):
        result = "Item List:\n------------------------------------\n"
        for name, price in self.prices.items():
            count = self.count[name]
            result += f"{name:40} x{count:<3} ${price:.2f}\n"
        result += "------------------------------------\n"
        return result