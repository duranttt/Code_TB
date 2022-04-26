#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
n=0
for line in file1:
    if "Viruses" in line:
        n=n+1
    if n==1:
        if int(line.split("\t")[2]) != 0:
            file2.write(line.split("\t")[-2]+"\n")
