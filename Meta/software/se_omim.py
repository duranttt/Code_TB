#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"r")
file3 = open(sys.argv[3],"w")
dic_pt = {}
for line in file1:
    if line.startswith("#"):
        continue
    else:
        mim_number = line.split("\t")[5]
        phe = line.split("\t")[12]
        list1 = line.split("\t")[6].split(",")
        if len(list1) == 1:
            dic_pt[list1[0]] =mim_number+"  "+ phe
        else:
            n=0
            while n<=len(list1)-1:
                dic_pt[list1[n]] = mim_number+"  "+phe
                n=n+1
for line2 in file2:
    line1 = line2[line2.index("\t")+1:]
    if line1.startswith("#"):
        title = line1.strip("\n")+"\tPhenotypes\n"
        file3.write(title)
    else:
        if line1.split("\t")[2] in dic_pt.keys():
            file3.write(line1.strip("\n")+"\t"+dic_pt[line1.split("\t")[2]]+"\n")
        else:
            file3.write(line1.strip("\n")+"\t.\n")
