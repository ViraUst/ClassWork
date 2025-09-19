#Athor: Vira Ustymenko
#Date: 18.09.25
#Description: Categorises depending on given age, prints answer

age = int(input("Enter the age: "))
if age < 13:
    print("Child.")
elif age >= 13 and age < 20:
    print("Teenager.")
else:
    print("Adult.")
