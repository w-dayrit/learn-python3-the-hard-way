from sys import argv
print(argv)
script, occupation, place_of_work, work_department, time_of_occupation = argv
responsibilities = input("Describe what you do: ")

print(f"I am a {occupation} at {place_of_work}. I work in {work_department} and have been there for {time_of_occupation}.")
print(responsibilities);