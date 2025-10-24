#Author: Vira Ustymenko
#Date: 23st October 2025
#Description: asks user to enter a string of numbers, and a step size. Goes through
# the string and adds the first number plus all the numbers at the step size

nums = input("Enter string of numbers: ")
step = int(input("Enter a step size: "))
s = 0
for i in nums[::step]:
    s = int(i) + s
print(s)