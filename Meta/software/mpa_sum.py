#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"r")
file3 = open(sys.argv[3],"w")
dic_1 = {}
dic_2 = {}
list1 = []
for line in file1:
    if line.startswith("#"):
        header = line
        length = len(line.split("\t"))
    else:
        list1.append(line.split("\t")[0])
        dic_1[line.split("\t")[0]] = line.strip("\n")
file3.write(header)
for line in file2:
    dic_2[line.split("\t")[0]] = line.strip("\n")
    if line.split("\t")[0] not in list1:
        list1.append(line.split("\t")[0])
for key in list1:
    if key in dic_1.keys() and key in dic_2.keys():
        n=1
        str1 = key
        while n<length:
            str1 = str1 +"\t"+str(int(dic_1[key].split("\t")[n])+int(dic_2[key].split("\t")[n]))
            n=n+1
        file3.write(str1+"\n")
    elif key in dic_1.keys() and key not in dic_2.keys():
        file3.write(dic_1[key]+"\n")
    elif key in dic_2.keys() and key not in dic_1.keys():
        file3.write(dic_2[key]+"\n")
