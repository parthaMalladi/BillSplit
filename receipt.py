from item import Item
from user import User

class Receipt:
    def __init__(self):
        self.items = []
        self.users = []
    
    # adds item to list
    def addItem(self, name, price=-1):
        itemFound = False
        
        for item in self.items:
            if item.name == name:
                itemFound = True
                item.count += 1
                break
        
        if not itemFound and price <= 0:
            print("Can't add an item with 0 or negative price")
            return
        
        if not itemFound:
            temp = Item(name, price)
            self.items.append(temp)
    
    # adds user to list
    def addUser(self, first, last):
        for user in self.users:
            if user.firstName == first and user.lastName == last:
                print("User " + first + " " + last + " already exists")
                return
        
        temp = User(first, last)
        self.users.append(temp)
    
    # assigns users to an item
    def assign(self, itemName, users):
        for item in self.items:
            if item.name == itemName:
                for u in users:
                    item.addUser(u)
    
    # gets how much money each person owes
    def getTotals(self, multi=1):
        mem = {}
        
        for u in self.users:
            mem[u] = 0.0
        
        for item in self.items:
            price = item.getSplit()
            for user in item.users:
                mem[user] += price
        
        for key in mem:
            mem[key] *= multi
        
        return mem