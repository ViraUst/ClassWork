#Author: Vira Ustymenko
#Date: 4th November 2025
#Description: Outputs the biggest word from an entered string

wo = input("Enter a string of text: ")
count = 0
wo = wo + ' '
a = ''
howMany = wo.count(' ') + 1
lyenth = len(wo)
longest = ''
c =''

for b in wo:
    if b != ' ':
        a = a+b
        count = count  + 1
    else:
        if len(a) >= len(longest):
            longest = a
        a = ''
print(longest)