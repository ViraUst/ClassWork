#Author: Vira Ustymenko
#Date: 02 September 2025
#Description: Program computes simple interest and compound interest

principal = float(input("Enter principal amount: "))
rateOfInterest = float(input("Enter rate of interest: "))
time = float(input("Enter time: "))
compoundNumber = float(input("Enter number of times interest is compound per year: "))
simpleInterest = principal * rateOfInterest * time
compoundInterest = principal * (1 + rateOfInterest/compoundNumber)**compoundNumber
print("Simple interest =", simpleInterest, "Compound interest =", compoundNumber)