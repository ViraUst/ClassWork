#Question 16(b)
#Name and School: Vira Ustymenko
#Date: 28th, April 2026

temperatures=[14,23.5,72,56,45.5]
meanstart = sum(temperatures)/len(temperatures)
newtemp = float(input("Enter a temperature: "))
temperatures.append(newtemp)
print("Maximum temperature =", round(max(temperatures),1), "Minimum temperature =", round(min(temperatures),1))
mean = sum(temperatures)/len(temperatures)

print("Mean temperature =", round(mean,1) )
if mean > meanstart:
    print("Mean temperature is increasing")
elif mean < meanstart:
    print("Mean temperature is decreasing")