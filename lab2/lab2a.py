#!/usr/bin/python3

import sys

# Check if the filename argument is provided
if (len(sys.argv) < 2):
    print("Filename missing")
    sys.exit(0)

filename = sys.argv[1]

fh = open(filename, "r")


sortedList = []

for line in fh:
    if not line: break
    if (line[0] == '#'): continue
    if (line[0].isspace()): continue

    # Clean the line
    line = line.replace("\n", "")

    # Split the line using pipe delimiter
    parts = line.split("|")
    pid = parts[0]
    name = parts[1]
    age = parts[2]
    job = parts[3]
    wage = parts[4]

    # Recombine the age and name into a line
    combinedLine = age + " " + name
        
    # Put new lines into a list
    sortedList.append(combinedLine)

# Close the file
fh.close()

# Sort list by age
sortedList.sort()

# Use a for loop to look at each line, split the age and name, and sort it
for line in sortedList:
    # Split the line into age and name
    age,name = line.split(maxsplit=1)
    # Display names in age order
    print(f"Age: {age}, Name: {name}")



