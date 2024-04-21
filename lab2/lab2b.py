#!/usr/bin/python3

import sys

# Check if the filename argument is provided
if (len(sys.argv) < 2):
    print("Filename missing")
    sys.exit(0)

filename = sys.argv[1]

fh = open(filename, "r")

agesList = []

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

    
    agesList.append(age)

# Close the file
fh.close()

agesList.sort()

number_count = {}

for age in agesList:
    if age in number_count:
        number_count[age] += 1
    else:
        number_count[age] = 1

total = 0

for age, count in number_count.items():
    print(f"Age: {age} -> Count: {count}")
    total += count

print(f"Total: {total}")
