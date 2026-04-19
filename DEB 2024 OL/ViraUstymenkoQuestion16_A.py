# Question 16(a)
# Name and School: Vira Ustymenko, Athlone Community College
# Date: 16th April 2026

print("Household budget calculator")
num_adults = int(input("Number of adults in household: "))
num_child = int(input("Number of children in household: "))
infl = float(input("Inflation rate (e.g. 0.05 for 5% inflation): "))

food_budget = 300
cost_food_adults = 50
cost_food_child = 35

child_allowance = 140
num_extra_ca = num_child-3
extra_a = 20

child_atotal = child_allowance*num_child+num_extra_ca*extra_a
print("Children’s allowance total: €", child_atotal, sep='')
tot_cost_food = cost_food_adults*num_adults+cost_food_child*num_child
print("Total household food cost: €",tot_cost_food, sep='')
inflation_food = round(tot_cost_food*(1+infl),2)
print("Total household food cost with inflation: €", inflation_food, sep='')

perc = round(inflation_food/child_atotal*100,2)
print("Percentage spend on food: ", perc, "%", sep='')

left = food_budget - inflation_food + child_atotal

print("Budget remaining after food spend: €", left)