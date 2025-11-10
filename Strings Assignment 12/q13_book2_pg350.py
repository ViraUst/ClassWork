#Author: Vira Ustymenko
#Date: 4th November 2025
#Description: Counts number of vowels in a line of text

_theLie = input("Enter a line of text: ")
count = _theLie.count("a")+ _theLie.count("e") + \
        _theLie.count("i") + _theLie.count("o") + \
        _theLie.count("u")
print("Method 1:",count,"vowels.")
count_1 = 0


lis = "aieou"
for i in lis:
    count_1 = _theLie.count(i) + count_1 #quicker way
print("Method 2:",count_1,"vowels.")