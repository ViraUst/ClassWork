# Question 16(a)
# Name and School: Vira Ustymenko, Athlone Community College
# Date: 16th Aptil 2026

P = float(input("Enter the principal investment amount: \u20ac"))
I = float(input("Enter the annual interest rate (e.g. 0.05 for 5% interest): "))

for t in range(1,11):
    value = P*(1+I)**t
    print("Year",t,"- Investment value: \u20ac", round(value,2))