#Author: Vira Ustymenko
#Date: 17th-20th November 2025
#Description: program adds binary numbers

number = input("Enter a binary number: ")
number2 = input("Enter the second binary number: ")

if len(number)>len(number2):
    number2 = '0'*(len(number)-len(number2))+number2
elif len(number2)>len(number):
    number = '0'*(len(number2)-len(number))+number
    #this makes the numbers the same length without changing the value

end = -1
var = 0
sa =''
number1 = number[::-1]
fin = ''
for i in number1:
    units = int(i) + int(number2[end]) + var
    var = 0
    if int(units) >= 2:
        fin = int(units) - 2
        var = 1
        sa = str(fin) + sa
    else:
        sa = str(units) + sa
    end = end-1  
    
if var == 1:
    print('1'+sa)
else:
    print(sa)