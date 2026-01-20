#Author: Vira Ustymenko
#Date: 15th January 2026
#Description: Asks the user to enter a list of strings. Creates a new list that consists of those
#strings with their first characters removed.

print("Enter a list of strings, to finish enter done1")
done1 = False
Od = []
Ev = []
while not done1:
    strips = input("Enter an element: ")
    if strips != 'done1':
        Od.append(strips)
        Ev.append(strips[1:])
    else:
        done1 = True
print("Original list =",Od)
print("Modified list =",Ev)