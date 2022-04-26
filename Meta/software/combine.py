#!/usr/bin/python
import sys
import subprocess
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
list_sample = []
y=""
for line in file1:
    if line.strip("\n").split("\t")[-1] == "Y":
        y = line.split("\t")[0]
    else:
        list_sample.append("result/"+line.split("\t")[0]+".mpa")
str1 = " ".join(list_sample)
if y == "":
    str1 = str1
else:
    str1 = str1 + " result/"+y+".mpa"
file2.write("python3 /mnt/software/script/combine_mpa.py -i "+str1+" -o result/result.mpa")
