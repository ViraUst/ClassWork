#Question16_B_OL
#Enter your name here: Vira Ustymenko
#Date: 14th April 2026

print("Welcome to my weekly step tracker!")
b = True
DaysOfW = ['Please enter the steps you did on Monday: ','Please enter the steps you did on Tuesday: ',\
           'Please enter the steps you did on Wednesday: ','Please enter the steps you did on Thursday: ',\
           'Please enter the steps you did on Friday: ','Please enter the steps you did on Saturday: ',\
           'Please enter the steps you did on Sunday: ']
o = 0
total = []
Sum = 0

for i in range(7):
    StepNum = int(input(DaysOfW[o]))
    total.append(StepNum)
    Sum += StepNum
    o += 1
print("The list of steps is: ",total)
print("The total steps taken this week was: ", Sum)
average = Sum/7
print("The average number of steps is: ", round(average,2))
print("The largest number of steps you took this week was: ", max(total))
print("The smallest number of steps you took this week was: ",min(total))