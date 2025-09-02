#Author: Vira Ustymenko
#Date: 01 September 2025
#Description: Program requests the user's name and age, greets the user and displays their age the next year
user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: "))
user_age_next_y = user_age + 1
print("Hello", user_name,", next year you will be", user_age_next_y, "years old.")
