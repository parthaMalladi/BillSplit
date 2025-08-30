class Receipt:
    def __init__(self, items):
        self.prices = {}
        self.count = {}
        self.bill = {}
        
        for item, price in items:
            self.prices[item] = price
            
            if item not in self.count:
                self.count[item] = 0
            
            self.count[item] += 1
    
    def addItem(self, item, price, count):
        self.prices[item] = price
        self.count[item] = count
    
    def removeItem(self, item, count):
        if item not in self.count:
            print("Item " + item + " does not exist")
            return
        
        self.count[item] -= count
        if self.count[item] == 0:
            self.count.pop(item, None)
            self.prices.pop(item, None)
    
    def splitItem(self, item, div):
        if item not in self.prices:
            return -1
        
        return (self.prices[item] * self.count[item]) // div

    def __str__(self):
        result = "Item List:\n------------------------------------\n"
        for name, price in self.prices.items():
            count = self.count[name]
            result += f"{name:40} x{count:<3} ${price:.2f}\n"
        result += "------------------------------------\n"
        return result