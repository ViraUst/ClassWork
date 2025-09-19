#Athor: Vira Ustymenko
#Date: 18.09.25
#Description: Calculates simple interest, outputs result

P = float(input("Principal: "))
R = float(input("Rate: "))
T = float(input("Time: "))

Simple_Interest = (P * R * T)/100
print('Simple interest = ', Simple_Interest, end='%')
