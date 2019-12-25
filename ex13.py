from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Study Drills
# 1. Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.
# "ValueError: not enough values to unpack (expected 4, got 3)"

# 2. Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.
# ex13num2a.py
# ex13num2b.py

# 3. Combine input with argv to make a script that gets more input from a user. Don’t overthink it. Just use argv to get something, and input to get something else from the user.
# ex13num2b.py

# 4. Remember that modules give you features. Modules. Modules. Remember this because we'll need it later.