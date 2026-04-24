# Please enter name: Vira Ustymenko
# Date: 23rd April 2026
# Desc: Question 16 A

print("******************")
print("* Conversions *")
print("******************")
print("1) From teaspoons to ml")
print("2) From tablespoons to ml")
print("3) From cups to ml")
print("4) From ml to teaspoons")
print("5) From ml to tablespoons")
print("6) From ml to cups")
conversion = int(input("Please enter the conversion (number from 1 to 5) and press ENTER:"))
if conversion == 1:
    teaspoons = float(input("Please enter number of teaspoons: "))
    ml = teaspoons * 5
    print("The ml is:", ml)
elif conversion == 2:
    tablespoons = float(input("Please enter number of tablespoons: "))
    ml = tablespoons * 15
    print("The ml is:", ml)
elif conversion == 3:
    cups = float(input("Please enter number of cups: "))
    ml = cups * 237
    print("The ml is:", ml)
elif conversion == 4:
    ml = float(input("Please enter number of ml: "))
    teaspoons = ml/5
    print("The number of teaspoons is:", teaspoons)
elif conversion == 5:
    ml = float(input("Please enter number of ml: "))
    tablespoons = ml/15
    print("The number of tablespoons is:", tablespoons)
elif conversion == 6:
    ml = float(input("Please enter number of ml: "))
    cups = ml/237
    print("The number of cups is:", cups)
