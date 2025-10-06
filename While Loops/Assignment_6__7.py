#Author: Vira Ustymenko
#Date: 03 October 2025
#Description: Program takes numbers until thier sum is more than 50

may = 0
while may==0:
    n = float(input("Please enter a number between 10 and 20 inclusive: "))
    if n>=10 and n<=20:
        may = 1
    elif n<10:
        print('''
Too low.
''')
    elif n>20:
        print('''
Too high.
''')
print("Thank you.")

#triple quotes for some space between the lines in orded to make the text more
#readable