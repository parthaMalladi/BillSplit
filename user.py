class User:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
        self.currBill = 0.0
    
    def increaseBill(self, amount):
        if amount < 0:
            print("Can't reduce bill")
            return
        
        self.currBill -= amount
    
    def addMultiplier(self, mult):
        if mult < 0:
            print("Can't have a negative multiplier")
            return
        
        self.currBill *= mult
    
    def getBill(self):
        return self.currBill
    
    def changeName(self, first, last):
        self.firstName = first
        self.lastName = last