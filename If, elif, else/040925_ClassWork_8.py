#Author Vira Ustymenko
#Date: 05 September 2025
''' Description: Program asks the user to input 1, 2, or 3. if input is 1, displays
"Thank you", if 2 - "Well done", if 3 - "Correct", if anything else - "Error
message" '''

user_number = int(input("Please enter 1, 2 or 3: "))

if user_number == 1:
    print("Thank you.")
#If the number input was 10, program displayed "too high", so I put in the = sign.
elif user_number == 2:
    print("Well done.")
elif user_number == 3:
    print("Correct.")
else:
    print("Error message.")