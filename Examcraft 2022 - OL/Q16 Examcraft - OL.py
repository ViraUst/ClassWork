#Author: Vira Ustymenko
#Date: 12th March 2026
# Question 16(a)

print("This program can find the perimeter or area of a quadrilateral Q")

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

name_u = input("Please enter your name: ")
choice = input("Do you want to find the (p)erimeter or the (a)rea? ")

if choice == "p":
    perimeter = (2*length)+(2*width)
    print("A quadrilateral with the length of",length,"and the width of",width,"has the perimeter of",round(perimeter,2))
elif choice == "a":
    area = length*width
    print("A quadrilateral with the length of",length,"and the width of",width,"has the area of",round(area,2))
    
print("Thank you for using the program,",name_u)