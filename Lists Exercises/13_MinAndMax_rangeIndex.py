#Author: Vira Ustymenko
#Date: 20th January 2026
#Description: Displays the maximum and minimum values from the specified range of indexes of a list

lizzie = [4,2,1,10,88,453,10007,2,0,6,5,9]
print("The list is: ", lizzie)
rangS = int(input("Enter starting index of the range: "))
rangE = int(input("Enter ending index of the range: "))

Bob = lizzie[rangS:rangE]
print("The minimum value of the range: ", min(Bob))
print("The maximum value of the range: ", max(Bob))