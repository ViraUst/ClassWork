#Athor: Vira Ustymenko
#Date: 18.09.25
#Description: Checks if input year is a leap year or not, outputs result

Year = int(input("Year: "))
if Year%4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
