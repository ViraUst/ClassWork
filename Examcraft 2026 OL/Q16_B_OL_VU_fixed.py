#Author: Vira Ustymenko
#Date: 15th May 2026
#Description: Question 16(b) OL with feedback changes

print("Welcome to my weekly step tracker!")
b = True
DaysOfW = ['Monday: ','Tuesday: ','Wednesday: ','Thursday: ','Friday: ','Saturday: ','Sunday: ']
total = []
Sum = 0

for i in range(len(DaysOfW)):
    message = "Enter the steps you did on " + DaysOfW[i]
    StepNum = int(input(message))
    total.append(StepNum)
    Sum += StepNum
    
print("The list of steps is: ",total)
print("The total steps taken this week was: ", Sum)
average = Sum/len(DaysOfW)
print("The average number of steps is: ", round(average,2))
print("The largest number of steps you took this week was: ", max(total))
print("The smallest number of steps you took this week was: ",min(total))
