#!/usr/bin/python3

import sys

# Check if the filename argument is provided
if (len(sys.argv) < 2):
    print("Filename missing")
    sys.exit(0)

filename = sys.argv[1]

fh = open(filename, "r")

professions = {}

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
    rate = float(parts[4])

    if job in professions:
        professions[job]['count'] += 1
        professions[job]['total_wages'] += rate
    else:
        professions[job] = {'count': 1, 'total_wages': rate}

# Close the file
fh.close()

# Calculate the average rate for each profession
for profession, data in sorted(professions.items()):
    average_rate = data['total_wages'] / data['count']
    print(f"Profession: {profession}\t${average_rate:.2f}")
