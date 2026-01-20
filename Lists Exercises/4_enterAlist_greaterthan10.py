#Author: Vira Ustymenko
#Date: 15th January 2026
#Description: Asks the user to enter a list containing numbers between 1 and 12. Then replaces all
# of the entries in the list that are greater than 10 with 10.

i = True
Elle = []

print("Hello, enter a list of number elements between 1 and 12. Enter i to finish.")

while i:
    item = input("Enter a number element between 1 and 12: ")
    if item.isdigit()== True and int(item) >=1 and int(item) <=12:
        item = int(item)
        Elle.append(item)
    elif item == 'i':
        i = False
    else:
        print("Incorrect value, try again.")

for b in range(len(Elle)):
    if Elle[b] > 10:
        Elle[b]=10
print(Elle)