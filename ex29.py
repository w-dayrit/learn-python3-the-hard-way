people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")

# Study Drills
# 1. What do you think the if does to the code under it?
# Executes code if condition is met

# 2. Why does the code under the if need to be indented four spaces?
# Designate that it belongs to the if condition

# 3. What happens if it isn’t indented?
# Will just run without checking the if condition

# 4. Can you put other Boolean expressions from Exercise 27 in the if-statement? Try it.
# Yes

# 5. What happens if you change the initial values for people, cats, and dogs?
# Changes outcomes of the conditions
