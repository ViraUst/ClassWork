#Author: Vira Ustymenko
#Date: 02 September 2025
#Description: Program asks for user's height in cm and converts it to feet and inches

user_height = float(input("Enter your height: "))
 
inches = user_height / 2.54
feet = inches/12
print("Your height is", inches, "inches, or", feet, "feet.")