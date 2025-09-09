#Author: Vira Ustymenko
#Date: 01 September 2025
#Description: Program requests the total price of the bill, then requests the number of diners and displays how much each should pay
total = float(input("Enter the total price of your bill: "))
number_diners = int(input("Enter the number of diners: "))
each = total / number_diners
print("Each diner must pay", each)
