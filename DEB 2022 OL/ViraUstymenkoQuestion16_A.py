# Question 16(a) 
# Name and School: Vira Ustymenko, Athlone Community College
# Date: 21st April 2026
import random
SupVacc = ["A","B","C"]
answer = 1

while answer!='END':
    s_name = input("Enter your surname: ")
    f_name = input("Enter your first name: ")
    age = int(input("Enter your age: "))
    eir = input("Enter your Eircode: ")
    yesno = input('''Do you agree to participate in a vaccine trial?
Type 'Yes' or 'No' ''')
    #K78 E625
    #K66 E644
    print("Hello", f_name, s_name, "you are", age, "years old, and your Eircode is", eir)

    if int(eir[-1])%2==0:
        sign = "Eastwood"
    else:
        sign = "Northfield"
    print("You must attend", sign, "for your vaccine")    

    if yesno == 'No':
        if age<50 and age>11:
            vaccine = "MRNA"
        elif age>=50:
            vaccine = "ADENO"
        print(f_name, ", you will receive the ",vaccine," vaccine", sep='')
    else:
        v = random.choice(SupVacc)
        print("You are now enrolled in the trial to receive the Super vaccine",v)
    answer = input("If you have finished entering people's details type 'END', otherwise press ENTER: ")