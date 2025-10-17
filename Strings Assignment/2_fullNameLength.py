#Author: Vira Ustymenko
#Date: 17th October 2025
#Description: displays length of a joined together name and surname entered bu the
# user

name = input("Name: ")
surname = input("Surname: ")
both = name + ' ' + surname

print(both, """
Length = """,len(both)-1)