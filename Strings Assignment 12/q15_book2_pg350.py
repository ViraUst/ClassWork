#Author: Vira Ustymenko
#Date: 10th November 2025
#Description: Program takes input line of text then creates a new line of text where each word of
# input is revesed

theL = input("Enter a line of text: ")
theL = theL + ' '
reverse = ''
linux = ''
for i in theL:
    if i != ' ':
        reverse = reverse + i
    else:
        linux = reverse[::-1]
        print(linux, end=' ')
        reverse = ''