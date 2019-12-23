# number of cars
cars = 100
# car space
space_in_a_car= 4.0
# number of drivers
drivers = 30
# number of passengers
passengers = 90
# number of cars left
cars_not_driven = cars - drivers
# number of cars out
cars_driven = drivers
# how much space for carpool
carpool_capacity = cars_driven * space_in_a_car
# passenger average
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

# Study Drills
# variable 'car_pool_capacity' in line 8 does not match the name 'carpool_capacity' in line 7

# 1. I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
# Not necessary, spaces are whole numbers.
# Variable carpool_capacity would be a whole number

# 2. Remember that 4.0 is a floating point number. It’s just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.

# 3. Write comments above each of the variable assignments.

# 4. Make sure you know what = is called (equals) and that its purpose is to give data (numbers, strings, etc.) names (cars_driven, passengers).

# 5. Remember that _ is an underscore character.

# 6. Try running python3.6 from the Terminal as a calculator like you did before, and use variable names to do your calculations. Popular variable names include i, x, and j.