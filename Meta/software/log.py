#!/usr/bin/python
import math
import sys
file1 = open(sys.argv[1],"r")
file_out = open(sys.argv[2],"w")
for line in file1:
    if line.startswith("#"):
        file_out.write(line)
    else:
        list1 = line.strip("\n").split("\t")[1:]
        list_out = []
        for value in list1:
            list_out.append(str(math.log(float(value)+1,10)))
        file_out.write(line.split("\t")[0]+"\t"+"\t".join(list_out)+"\n")
