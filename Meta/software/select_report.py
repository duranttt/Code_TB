#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
file2.write("#Classification\t"+sys.argv[1].split("/")[-1].split(".")[0][0:-2]+"\n")
for line in file1:
    list_l = line.strip("\n").split("\t")
    if list_l[3] == "D":
        superkindom = "|k__"+list_l[5].strip(" ")
        kindom = p = c = o = f = g = s = ""
    if list_l[3] == "K":
        kindom = "|k__"+list_l[5].strip(" ")
        p = c = o = f = g = s = ""
    if list_l[3] == "P":
        p = "|p__" + list_l[5].strip(" ")
        c = o = f = g = s = ""
    if list_l[3] == "C":
        c = "|c__" + list_l[5].strip(" ")
        o = f = g = s = ""
    if list_l[3] == "O":
        o = "|o__" + list_l[5].strip(" ")
        f = g = s = ""
    if list_l[3] == "F":
        f = "|f__" + list_l[5].strip(" ")
        g = s = ""
    if list_l[3] == "G":
        g = "|g__" + list_l[5].strip(" ")
        s = ""
    if list_l[3] == "S":
        s = "|s__" + list_l[5].strip(" ")
        file2.write(superkindom+kindom+p+c+o+f+g+s+"\t"+str(list_l[1])+"\n")
