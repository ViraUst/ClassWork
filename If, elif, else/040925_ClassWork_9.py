#Author Vira Ustymenko
#Date: 05 September 2025
''' Description: Program displays total water bill charges for a month given the
number of units consumed. Rates: 5 cent a unit for first 100 units; 10 cent a unit
for the next 150 units; 20 cent a unit for the next 150 units '''

unitsConsumed = int(input("Enter the number of units consumed that month: "))
total100 = 5 * 100
difference = 100 - unitsConsumed

if unitsConsumed <= 100:
    total = 5 * unitsConsumed
    print("The total water bill charges: ", total)
    
elif unitsConsumed >100:
    Over100 = unitsConsumed - 100
    next150units = Over100 * 10 + total100
    
    if unitsConsumed <= 250:
        print("The total water bill charges: ", next150units)
        
    elif unitsConsumed > 250:
        next150units = 150 * 10 + total100
        cent20perUnit = unitsConsumed - 250
        over250units = next150units + cent20perUnit * 20
        print("The total water bill charges: ", over250units)