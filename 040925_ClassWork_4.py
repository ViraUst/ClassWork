#Author Vira Ustymenko
#Date: 04 September 2025
#Description: Program asks the user for their favourite colour, if they enter red,
#Red, orRED desplays "I like red too", otherwise "I dont like the colour, i prefer red"

user_colour = (input("Please enter your favourite colour: "))
if user_colour == "red" or user_colour == "Red" or user_colour == "RED":
    print("I like red too.")
else:
    print("I don't like the colour", user_colour, ", I prefer red.")