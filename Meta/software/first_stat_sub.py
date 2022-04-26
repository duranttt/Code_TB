#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
dic_sub = {}
for line in file1:
    sid = line.split("\t")[2]
    if sid in dic_sub.keys():
        dic_sub[sid] = dic_sub[sid] + 1
    else:
        dic_sub[sid] = 1
for key in dic_sub.keys():
    file2.write(key+"\t"+str(dic_sub[key])+"\n")
