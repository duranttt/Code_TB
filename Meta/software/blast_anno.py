#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"r")
file3 = open(sys.argv[3],"w")
dic_an = {}
for line2 in file2:
    dic_an[line2.split("\t")[0]] = line2.split("\t")[2]

for line in file1:
    if line.startswith("#"):
        file3.write(line)
    else:
        if "|" in line.split("\t")[3] and line.split("\t")[3].split("|")[1] in dic_an.keys():
            file3.write(line.strip("\n")+"\t"+dic_an[line.split("\t")[3].split("|")[1]])
        elif line.split("\t")[3] in dic_an.keys():
            file3.write(line.strip("\n")+"\t"+dic_an[line.split("\t")[3]])
