#Author Vira Ustymenko
#Date: 04 September 2025
'''Description: Asks the user for a number and displays: "Too low" if the num. is
lower than 10, if it's between 10 and 20  - "Correct", and otherwise - "Too high"'''

user_number = float(input("Please enter a number: "))

if user_number < 10:
    print("Too low.")
#If the number input was 10, program displayed "too high", so I put in the = sign.
elif user_number >= 10 and user_number <= 20:
    print("Correct.")
else:

    print("Too high.")
