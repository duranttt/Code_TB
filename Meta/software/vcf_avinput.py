#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    if line.startswith("#"):
        continue
    else:
        list1 = line.split("\t")
        pos_end = int(list1[1])+len(list1[4])-1
        DP = list1[7].split(";")[4][3:]
        AF = list1[7].split(";")[1][3:]
        file2.write(list1[0]+"\t"+list1[1]+"\t"+str(pos_end)+"\t"+list1[3]+"\t"+list1[4]+"\t"+list1[6]+"\t"+list1[5]+"\t"+DP+"\t"+AF+"\n")
