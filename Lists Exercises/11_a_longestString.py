#Author: Vira Ustymenko
#Date: 19th January 2026
#Description: (a) Print the length of the longest string in the list of strings str_list
#Precondition : the list will contain at least one element

str_list = []
process = True
print("Enter elements of a list, when done enter stop_")

while process:
    e = input("Enter element: ")
    if e != "stop_":
        str_list.append(e)
    else:
        process = False

long = ''

for i in str_list:
    if len(i)>len(long):
        long = i
        
print("Length of the longest string:",len(long))