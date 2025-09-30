#Author: Vira Ustymenko
#Date: 09th September 2025
#Description: prints the number of even and odd numbers from a series of numbers
#input by the user. The user should enter "q" to indicdate they are finished.


userinput = 0
count_1 = 0
count_2 = 0
while not userinput == "q":
    userinput = input("Enter a positive integer number, to finish enter 'q': ")
    if not userinput == "q":
        userinput = float(userinput)
        if userinput%2 == 0:
            count_1 = count_1 + 1
        else:
            count_2 = count_2 + 1
print("number of odd input numbers = ", count_2)
print("number of even input numbers = ", count_1)