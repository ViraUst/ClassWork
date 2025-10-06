#Author: Vira Ustymenko
#Date: 02 October 2025
#Description: Program takes an integer number and outputs all the even numbers from
# 0 to the number


Input = int(input("Enter an integer number: "))
count = -1
while count<=Input-1:
    count = count + 1
    if count%2==0 and count!=Input and count!=Input-1:
        print(count, end=',')
    elif count%2==0:
        print(count)
    else:
        pass


#Aternative using a for loop
'''Input = int(input("Enter an integer number: "))
for i in range(Input+1):
    if i%2==0 and i!=Input and i!=Input-1:
        print(i, end=',')
    elif i%2==0:
        print(i)
    else:
        pass'''