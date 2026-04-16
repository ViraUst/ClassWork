#Question16_A_OL
#Enter your name here: Vira Ustymenko
#Date: 14th April 2026

print("Welcome to the Step Tracker App!")
negative = True

user_name = input("Please enter your name: ")

steps_today = int(input("Enter the number of steps you walked today: ")) #this is where the user enters the number of steps.

if steps_today<0:
    negative = False
    print("The number of steps cannot be negative, ", user_name, ".", sep='')

while negative:
    if steps_today <5000:
        print("Try to be more active today ", user_name, sep='')
    elif steps_today >= 5000 and steps_today <10000:
        print("Good effort ", user_name, "! Almost there.", sep='')
    elif steps_today >=10000:
        print("Well done ", user_name, "! You reached your goal.", sep='')
    break
