from user import User

class Item:
    def __init__(self, name, price, count=1):
        self.name = name
        self.price = price
        self.count = count
        self.users = []
    
    # returns the amount owed by each user for the item
    def getSplit(self):
        return self.price // len(self.users)  
    
    # adds a user to an item
    def addUser(self, user):
        if user in self.users:
            print("User already assigned to " + self.name)
            return
        
        self.users.append(user)