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
        print("Command List")
        print("---------------------------------------------------------------------")
        print("To view receipt: view")
        print("To add user: +user [FirstName, LastName]")
        print("To add NEW item: +item [Name, Price]")
        print("To increment count of EXISTING item: +item [Name]")
        print("To remove an item: -item [Name]")
        print("To assign an item to users: assign [ItemName] [FirstName1 LastName1, ..., FirstNameX LastNameX]")
        print("To get totals and add a multiplier if necessary: totals [Multiplier]\n")
    elif info[0] == "view":
        print(myReceipt)
    elif info[0] == "+user":
        myReceipt.addUser(info[1], info[2])     
    elif info[0] == "+item":
        if len(info) > 2:
            myReceipt.addItem(info[1], info[2])
        else:
            myReceipt.addItem(info[1])
    elif info[0] == "-item":
        myReceipt.removeItem(info[1])
    elif info[0] == "assign":
        names = info[2:]
        myReceipt.assign(info[1], names)
    elif info[0] == "totals":
        bills = None
        
        if len(info) > 1:
            bills = myReceipt.getTotals(info[1])
        else:
            bills = myReceipt.getTotals()
            
        for k,v in bills.items():
            print(k + " owes $" + v)