#Author Vira Ustymenko
#Date: 04 September 2025
#Description: Program asks the user for 2 numbers, displays the smaller one first, the two numbers are never equal

num_1 = float(input("Please enter the first number: "))
num_2 = float(input("Please enter the second number(different from the first): "))

if (num_1 > num_2):
    print(num_2, num_1)
elif (num_2 > num_1):
    print(num_1, num_2)
else:

    print("Insufficient result")
