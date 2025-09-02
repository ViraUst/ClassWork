#Author: Vira Ustymenko
#Date: 02 September 2025
#Description: Program accepts marks in 5 subjects and outputs the average

SubjOne = int(input("Enter the first grade: "))
SubjTwo = int(input("Enter the second grade: "))
SubjThree = int(input("Enter the third grade: "))
SubjFour = int(input("Enter the fourth grade: "))
SubjFive = int(input("Enter the fifth grade: "))
Average = (SubjOne + SubjTwo + SubjThree + SubjFour + SubjFive)/5
print("Average grade is: ", Average)