#Author Vira Ustymenko
#Date: 04 September 2025
'''Description: Asks the user their age and displays answers depending on if they
are 18 or ofer, 17, 16, or under 16'''

user_age = int(input("Please enter your age: "))
if user_age >= 18:
    print("You can vote.")
elif user_age == 17:
    print("You can learn to drive.")
elif user_age == 16:
    print("You can buy a lottery ticket.")
else:
    print("You can go Trick-or-Treating.")