#Author: Vira Ustymenko
#Date: 17th November 2025
#Description: program adds binary numbers

number1 = input("Enter a binary number: ")
number2 = input("Enter the second binary number: ")
end = -1
var = 0
sa =''
for i in number1:
    units = int(i) + int(number2[end]) + var
    var = 0
    if int(units) >= 2:
        fin = int(units) - 2
        var = 1
    sa = str(fin) + sa
    end = end-1
if var == 1:
    print('1'+sa)
else:
    print(sa)