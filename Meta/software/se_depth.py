#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line1 in file1:
    if line1.startswith("#"):
        file2.write(line1)
    elif line1.split("\t")[3] != ".":
        file2.write(line1)
    else:
        continue
