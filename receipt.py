from item import Item
from user import User

class Receipt:
    def __init__(self):
        self.items = []
        self.users = {}

    # prints all commands
    def commands(self):
        print("Command List")
        print("---------------DON'T INCLUDE BRACKETS---------------")
        print("To view receipt: view")
        print("To add user: +user [FirstName LastName]")
        print("To add NEW item: +item [Name $Price]")
        print("To increment count of EXISTING item: +item [Name]")
        print("To remove an item: -item [Name]")
        print("To assign an item to users: assign [ItemName!] [FirstName1 LastName1 ... FirstNameX LastNameX]")
        print("To get totals and add a multiplier if necessary: totals [Multiplier]\n")   

    # adds all items gotten from receipt scan
    def addAll(self, list):
        for item, price in list:
            self.addItem(item, price)
    
    # removes item from a list
    def removeItem(self, name):
        itemFound = False
        
        for i, item in enumerate(self.items):
            if item.name == name:
                itemFound = True
                del self.items[i]
                break
        
        if not itemFound:
            print(name + " does not exist to be removed")        
    
    # adds item to list
    def addItem(self, name, price=-1):
        itemFound = False
        price = float(price)
        
        for item in self.items:
            if item.name == name:
                itemFound = True
                item.count += 1
                break
        
        if not itemFound and price <= 0.0:
            print("Can't add an item with 0 or negative price")
            return
        
        if not itemFound:
            temp = Item(name, price)
            self.items.append(temp)
    
    # adds user to list
    def addUser(self, first, last):
        combined = first + " " + last
        
        if combined in self.users:
            print("User " + first + " " + last + " already exists")
        else:
            temp = User(first, last)
            self.users[combined] = temp
    
    # assigns users to an item
    def assign(self, itemName, names):   
        for item in self.items:
            if item.name == itemName:
                for name in names:
                    item.addUser(self.users[name])
    
    # gets how much money each person owes
    def getTotals(self, multi=1):
        mem = {}
        
        for key in self.users:
            mem[key] = 0.0
        
        for item in self.items:
            price = item.getSplit()
            for user in item.users:
                name = user.firstName + " " + user.lastName
                mem[name] += price
        
        for key in mem:
            mem[key] *= float(multi)
        
        return mem
    
    # console output showing items, count, price
    def __str__(self):
        result = "Item List:\n------------------------------------\n"
        for item in self.items:
            result += f"{item.name:40} x{item.count:<3} ${item.price:.2f}\n"
        result += "------------------------------------\n"
        return result     