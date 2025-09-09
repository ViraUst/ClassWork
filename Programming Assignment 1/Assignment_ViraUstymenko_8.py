#Author: Vira Ustymenko
#Date: 01 September 2025
#Description: Program requests a random num. of days and outputs how many hours, minuntes, and seconds are in the given number of days.

days = float(input("Enter a random number of days: "))
hours = days *  24
minutes = hours * 60
seconds = minutes * 60
print("There is", hours, "hours,", minutes, "minutes, and", seconds, "seconds in", days, "days.")
