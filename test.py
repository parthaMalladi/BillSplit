import pytesseract
from PIL import Image
import re
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
        
curr = Receipt(items)

while True:
    info = input("Enter Command (type 'cmd' for list of commands or 'exit' to quit): ")
    
    if info == 'exit':
        break

    if info == 'cmd':
        print("Command List")
        print("----------------------------")


    print(curr)
    