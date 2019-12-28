# close: save & close file
# read: read file contents, can assign result to variable
# readline: reads one line of text file
# truncate: empties the file
# write(''): writes string to the file
# seek(0): moves read/write location to beginning of file

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C {^C}.")
print("If you don't want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally, we close it.")
target.close()

# Study Drills
# 1. If you do not understand this, go back through and use the comment trick to get it squared away in your mind. One simple English comment above each line will help you understand or at least let you know what you need to research more.

# 2. Write a script similar to the last exercise that uses read and argv to read the file you just created.
# ex16sd2.py

# 3. There's too much repetition in this file. Use strings, formats and escapes to print out line1, line2, line3 with just one target.write() command instead of six.
    # target.write(f'''
    # {line1}
    # {line2}
    # {line3}
    # ''')

# 4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you explicitly say you want to write a file.
# Default is read

# 5. If you open the file with 'w' mode, then do you really need the target.truncate()? Read the documentation for Python’s open function and see if that’s true.
# no; 'open for writing, truncating the file first' https://docs.python.org/3/library/functions.html#open
