#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"r")
file_out = open(sys.argv[3],"w")
dic_1 = {}
dic_2 = {}
for line1 in file1:
    if line1.startswith("#"):
        title1 = line1.strip("\n")
    else:
        dic_1[line1.split("\t")[0]] = line1.strip("\n").split("\t")[1:]
        len1 = len(line1.split("\t"))-1
for line2 in file2:
    if line2.startswith("#"):
        title2 = "\t".join(line2.strip("\n").split("\t")[1:])
    else:
        dic_2[line2.split("\t")[0]] = line2.strip("\n").split("\t")[1:]
        len2 = len(line2.split("\t"))-1
title = title1 + "\t" + title2 + "\n"
file_out.write(title)
list_all = list(set(dic_1.keys()).union(set(dic_2.keys())))
for spe in list_all:
    if spe in dic_1.keys() and spe in dic_2.keys():
        file_out.write(spe+"\t"+"\t".join(dic_1[spe])+"\t"+"\t".join(dic_2[spe])+"\n")
    elif spe in dic_1.keys() and spe not in dic_2.keys():
        str_out = spe + "\t" + "\t".join(dic_1[spe])
        n=1
        while n<=len2:
            str_out = str_out+"\t0"
            n=n+1
        file_out.write(str_out+"\n")
    elif spe not in dic_1.keys() and spe in dic_2.keys():
        str_out = spe
        n=1
        while n<=len1:
            str_out = str_out+"\t0"
            n=n+1
        file_out.write(str_out+"\t"+"\t".join(dic_2[spe])+"\n")
