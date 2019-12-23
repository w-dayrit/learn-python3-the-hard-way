name = 'Zed A.Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# Study Drills
# 1. Change all the variables so there is no my_  in front of each one. 
# Make sure you change the name everywhere, not just where you used = to set them.

# 2. Try to write some variables that convert the inches and pounds to centimeters and kilograms.
# Do not just type in the measurements. Work out the math in Python.

inches = 2
centimeters_per_inch = 2.54
print(f"{inches} inch(es) equals {inches * centimeters_per_inch} centimeters.")

pounds = 2
kilograms_per_pound = 0.453592
print(f"{pounds} pound(s) equals {pounds * kilograms_per_pound} kilograms.")

