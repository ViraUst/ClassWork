#Author Vira Ustymenko
#Date: 04 September 2025
#Description: Program asks the user for a number between 10 and 20 inclusive, if the number is higher or lower it outputs "incorrect value"

user_number = float(input("Please enter a number between 10 and 20 inclusive: "))
if user_number>=10 and user_number<=20:
    print("Thank you.")
else:

    print("incorrect value entered.")
