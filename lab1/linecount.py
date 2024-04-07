#!/usr/bin/python3

import sys

filename = sys.argv[1]

size = 0

fh = open(filename, "r")
while (True):
    line = fh.readline()
    if not line: break
    size += len(line)

    # Clean the line
    line = line.replace("\n", "")
    line = line.replace("\r", "")
    if line[0] == '#': continue

fh.close()

print("Size=%d" % size)
