from sys import argv

script, filename = argv

textFile = open(filename)

print(textFile.read())

textFile.close()