#Author: Vira Ustymenko
#Date: 6th October 2025
#Description: A program checks if a number is an Armstrong number (a num. equal to
# the sum of the cube of its digits)
total = 0
TheNum = input("Enter an integer number: ")
for i in TheNum:
    total = total + int(i)**3
TheNum = int(TheNum)
if TheNum == total:
    print("The number", TheNum, "is an Armstrong number")
elif TheNum!=total:
    print("The number", TheNum, "is not an Armstrong number")