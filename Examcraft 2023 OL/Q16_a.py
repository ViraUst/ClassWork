#Author: Vira Ustymenko
#Date: 13th March 2026

#Question 16(a)
option = input("Would you like to (a)dd, (s)ubtract, (m)ultiply or (d)ivide? ")
num1 = float(input("Please enter your first number: "))
num2 = float(input("Please enter your second number: "))
if option == "a":
    numR = num1 + num2
    print(num1, "+",num2,"=", round(numR,2))
if option == "s":
    numR = num1 - num2
    print(num1, "-",num2,"=",round(numR,2))
if option == "m":
    numR = num1 * num2
    print(num1, "*",num2,"=",round(numR,2))
if option == "d":
    numR = num1 / num2
    print(num1, "/",num2,"=",round(numR,2))
