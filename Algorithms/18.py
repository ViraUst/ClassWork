#Author: Vira Ustymenko
#Date: 19th September 2025
#Description: Calculates and prints the average number from 5 given numbers
count = 0
for number in range(1,6):
    num = float(input("Enter a number: "))
    count = count + num
avg = count/5
print("The average number = ", avg)
    

'''num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))
avg = (num1 + num2 + num3 + num4 + num5)/5
print("An average number = ", avg)'''