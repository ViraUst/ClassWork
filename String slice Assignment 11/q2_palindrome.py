#Author: Vira Ustymenko
#Date: 23st October 2025
#Description: checks if a string is a palindrome

word = input('Enter a word: ')
if word == word[::-1]:
    print('Palindrome')
else:
    print('Not a palindrome')