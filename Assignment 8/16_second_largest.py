#Author: Vira Ustymenko
#Date: 09th October 2025
#Description: input N numbers, outputs second largest

que = int(input("How many numbers?: "))
maxim = -1
secMax = -2

for i in range(que):
    Number = float(input("Enter number: "))
    
    if Number> maxim:
        secMax = maxim
        maxim = Number
#moving numbers down
    elif Number>secMax:
        secMax = Number
        
print("Second largest: ", secMax)