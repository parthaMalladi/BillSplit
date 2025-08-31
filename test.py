import pytesseract
from PIL import Image
from receipt import Receipt

img = Image.open("receipt.jpg")
text = pytesseract.image_to_string(img)

lines = text.split("\n")
items = []
for line in lines:
    if len(line) < 1 or '$' not in line:
        continue
    
    items.append([line, 0.0])


for i in range(len(items)):
    pos = items[i][0].find('$')
    
    if pos != -1:
        temp = items[i][0]
        items[i][0] = temp[:pos].strip()
        items[i][1] = float(temp[pos+1:].strip())

myReceipt = Receipt()
# myReceipt.addAll(items)

while True:
    text = input("Enter Command (type 'cmd' for list of commands or 'exit' to quit): ")
    info = text.split()
    
    if info[0] == 'exit':
        break
    elif info[0] == 'cmd':
        myReceipt.commands()
    elif info[0] == "view":
        print(myReceipt)
    elif info[0] == "+user":
        myReceipt.addUser(info[1], info[2])
    elif info[0] == "+item":
        priceIndex = -1
        itemName = ""
        
        for i, word in enumerate(info):
            if i == 0:
                continue
            if '$' in word:
                priceIndex = i
                break
            itemName += (word + " ")
            
        itemName = itemName[:len(itemName) - 1]
        
        if priceIndex == -1:
            myReceipt.addItem(itemName)
        else:
            price = info[priceIndex][1:]
            myReceipt.addItem(itemName, price)             
    elif info[0] == "-item":
        spaceIndex = text.find(' ')
        itemName = text[spaceIndex + 1:]
        myReceipt.removeItem(itemName)
    elif info[0] == "assign":
        itemName = ""
        itemIndex = -1
        
        for i, word in enumerate(info):
            if i == 0:
                continue
            
            itemName += (word + " ")
            
            if '!' in word:
                itemIndex = i
                break
        
        itemName = itemName[:len(itemName) - 2]
        names = []
        
        for i in range(itemIndex + 1, len(info), 2):
            first = info[i]
            last = info[i+1]
            names.append(first + " " + last)
        
        myReceipt.assign(itemName, names)
    elif info[0] == "totals":
        bills = None
        
        if len(info) >= 2:
            bills = myReceipt.getTotals(info[1])
        else:
            bills = myReceipt.getTotals()
            
        for k, v in bills.items():
            print(f"{k} owes ${v:.2f}")