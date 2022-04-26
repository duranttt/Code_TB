#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
value = sys.argv[2]
file2 = open(sys.argv[3],"w")
for line in file1:
    if line.startswith(">"):
        file2.write(line.split(" ")[0]+"/"+value+"\n")
    else:
        file2.write(line)
