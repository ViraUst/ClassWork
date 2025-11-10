#Author: Vira Ustymenko
#Date: 3rd November 2025
#Description: Program converts a given number into equivalent Roman number
#(store its value as a string)

#I = '1'
#V = '5'
#X = '1'
#L = '5'
#C = '1'
#D = '5'
#M = '1'

roman = 'IVXLCDM'
count = 0
end = 3
R = ''
final = ''
n = input("Enter a number to be converted from 1 to 4000: ")
for i in range(len(n)):
    current = roman[count:end]
    n = int(n)
    fir = n%10
    if fir >= 1 and fir<4:
        R = current[0]*fir
    elif fir == 4:
        R = current[0]+current[1]
    elif fir >=5 and fir<9:
        R = current[1] + current[0]*(fir-5)
    elif fir == 9:
        R = current[0]+current[2]
    else:
        pass
    n = n/10
    count = count+2
    end = end +2
    final = R+final
    
print(final)