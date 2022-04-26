#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    file_in = open(line.strip("\n"),"r")
    for line1 in file_in:
        if line1.strip("\n").split("\t")[-1] == "Viruses" or "virus" in line1.strip("\n").split("\t")[-1]:
            file2.write(line.split("/")[-1].split(".")[0]+"\t"+line1)
