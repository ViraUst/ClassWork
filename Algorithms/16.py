#Athor: Vira Ustymenko
#Date: 18.09.25
#Description: Prints a given number of odd numbers

n = int(input("Enter a whole positive number: "))
for i in range(n+1):
    if i%2==0:
        pass
    elif i == n or i == n-1:
        print(i)
    else:
        print(i, end=',')
#to make it look cleaner th elif statement prints a comma only after previous to the
# last numbers
