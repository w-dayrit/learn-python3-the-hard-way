tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Study Drills
# 1. Memorize all the escape sequences by putting them on flash cards.

# 2. Use ''' (triple-single-quote) instead. Can you see why you might use that instead of """?
# If string uses " (double-quotes) so they don't have to be escaped

# 3. Combine escape sequences and format strings to create a more complex format
print(f"{tabby_cat}\n\t{persian_cat}\n\t{backslash_cat}")