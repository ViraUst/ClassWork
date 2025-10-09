#Author: Vira Ustymenko
#Date: 08 October 2025 - 08 October 2025
#Desc: prints every integer between 1 and n divisible by m. Reports if
# the printed numbers are even or odd.

n = int(input("Enter an integer end of range number: "))
m = int(input("Enter the number results will be a multiple of: "))
for i in range(1,n):
    if i%m==0:
        print(i)
        if i%2==0:
            print("Even")
        else:
            print("Odd")
    else:
        pass
