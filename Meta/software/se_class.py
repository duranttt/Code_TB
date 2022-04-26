#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    if line.startswith("#"):
        file2.write(line)
    elif line.split("\t")[0].split("|")[-1] == "":
        continue
    elif line.split("\t")[0].split("|")[-1][0] == sys.argv[3]:
        file2.write(line)
    else:
        continue
