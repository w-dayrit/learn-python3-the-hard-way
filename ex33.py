numbers = []

def buildArrayUsingWhile(arr, limit, increment):
    i = 0
    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

# buildArrayUsingWhile(numbers, 100, 10)

# Study Drills
# 1. Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
# buildArray()

# 2. Use this function to rewrite the script to try different numbers.

# 3. Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how it increments by.

# 4. Rewrite the script again to use this function to see what effect that has.

# 5. Write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?
# Not needed

def buildArrayUsingFor(arr, limit, increment):
    for i in range(0, limit, increment):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

buildArrayUsingFor(numbers, 100, 10)