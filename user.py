class User:
    # defines a user with a first name, last name, and current bill
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
        self.currBill = 0.0
    
    # increases the bill of a user
    def increaseBill(self, amount):
        if amount < 0:
            print("Can't reduce bill")
            return
        
        self.currBill -= amount
    
    # adds a multiplier to the user's bill
    def addMultiplier(self, mult):
        if mult < 0:
            print("Can't have a negative multiplier")
            return
        
        self.currBill *= mult
    
    # changes the name of a user
    def changeName(self, first, last):
        self.firstName = first
        self.lastName = last