# sets a value to variable 'types_of_people'
types_of_people = 10
# set f-string with variable 'types_of_people' to variable 'x'
x = f"There are {types_of_people} types of people."

# set string to variable 'binary'
binary = "binary"
# set string to variable 'do_not'
do_not = "don't"
# set f-string with variables 'binary' and 'do_not' to variable 'y'
y = f"Those who know {binary} and those who {do_not}."

# print variable 'x'
print(x)
# print variable 'y'
print(y)

# print f-string with variable 'x'
print(f"I said: {x}")
# print f-string with variable 'y'
print(f"I also said: '{y}'")

# set false boolean to variable 'hilarious'
hilarious = False
# set string to variable 'joke_evaluation'
joke_evaluation = "Isn't that joke so funny?! {}"

# insert variable 'hilarious' in brackets in variable 'joke_evaluation' with format() and print
print(joke_evaluation.format(hilarious))

# set string to variable 'w'
w = "This is the left side of ..."
# set string to variable 'e'
e = "a string with a right side."

# print concatenated variables 'e' and 'w'
print(w + e)

# Study Drills
# 1. Go through this program and write a comment above each line explaining it.

# 2. Find all the places where a string is put inside a string. There are four places.
# Lines 4, 11, 19, 21

# 3. Are you sure there are only four places? How do you know? Maybe I like lying.
# There aren't-line 29

# 4. Explain why adding the two strings w and e and + makes a longer string.
# plus operator concatenates two strings