#Author: Vira Ustymenko
#Date: 15th January 2026
#Description: Checks if a number is present in the list or not. If the number is present, prints
#the posititon of the number. Prints an appropriate message if the number is not present in the list

Last = [1,2,4,10,99,25]
print("Set list =",Last)
checkN = int(input("Enter a number to check for: "))
if checkN in Last:
    print("The number", checkN, "is at index", Last.index(checkN))
else:
    print("Number not found in the list.")