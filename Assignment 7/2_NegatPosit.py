#Author: Vira Ustymenko
#Date: 6th October 2025
#Description: User enters numbers until they enter 0. The program prints the count
# of the positive and negative numbers entered.(Is assumed that all input is numeric)
countPos = 0
countNegative = 0
numEnt = 25
while numEnt != 0:
    numEnt = float(input("Enter a negative or a positive number, to end enter 0: "))
    if numEnt>0:
        countPos = countPos+1
    elif numEnt<0:
        countNegative = countNegative+1
print("You entered", countPos, "positive numbers and", countNegative, "negative numbers")