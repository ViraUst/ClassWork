#Author: Vira Ustymenko
#Date: 21st October 2025
#Description: all occurences of the given word's first character are changed to '$',
# except for the first character itself

TheWord = input("Enter a word: ")
the_first_chara = TheWord[0]
var = '$'
finalword = TheWord.replace(the_first_chara,var)
finale = the_first_chara+finalword[1:]
print(finale)