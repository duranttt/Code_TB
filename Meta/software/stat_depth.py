#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
species = "no"
len_seq = 0
len_depth = 0
depth = 0
n=1
for line in file1:
    if n==1:
        species = line.split("\t")[0]
        len_seq = 1
        depth = int(line.strip("\n").split("\t")[2])
        if depth == 0:
            len_depth = 0
        else:
            len_depth = 1
    elif species != line.split("\t")[0]:
        if round(depth/len_seq,2) > 1:
            file2.write(species+"\t"+str(round(len_depth/len_seq,2))+"\t"+str(round(depth/len_seq,2))+"\t"+str(len_seq)+"\n")
        species = line.split("\t")[0]
        len_seq = 1
        depth = int(line.strip("\n").split("\t")[2])
        if depth == 0:
            len_depth = 0
        else:
            len_depth = 1
    else:
        len_seq = len_seq + 1
        depth = depth + int(line.strip("\n").split("\t")[2])
        if int(line.strip("\n").split("\t")[2]) == 0:
            continue
        else:
            len_depth = len_depth + 1
    n=n+1
