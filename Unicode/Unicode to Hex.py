#Author: Vira Ustymenko
#Date: 27th November 2025
#Description: Program converts Unicode to Hexadecimal

#uni = '111000101000001010101100' = should give 20AC
uni = input('Enter unicode: ')
if len(uni)==8:
    gi = uni[1:]
elif len(uni)==16:
    fur = uni[3:8]
    gi = fir + uni[10:]
elif len(uni)==24:
    fur = uni[4:8]
    gi = fur + uni[10:16] + uni[18:]
elif len(uni)==32:
    fur = uni[5:8]
    gi = fur + uni[10:16] + uni[18:24] + uni[26:]
    
lenth = len(gi)//4
count = 0

start = 0
end = 4
hexa = ''

for i in range(lenth):
    endgoal = 0
    power = 3
    quarter = gi[start:end]
    for b in quarter:
        calc = int(b) * (2**power)
        power = power-1
        endgoal = endgoal+calc
    if endgoal == 10:
        endgoal = 'A'
    elif endgoal == 11:
        endgoal = 'B'
    elif endgoal == 12:
        endgoal = 'C'
    elif endgoal == 13:
        endgoal = 'D'
    elif endgoal == 14:
        endgoal = 'E'
    elif endgoal == 15:
        endgoal = 'F'
    hexa = hexa + str(endgoal)
    start = start + 4
    end = end+4
    
print("U+",hexa)