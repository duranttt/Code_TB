#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
dic_all = {}
for line1 in file1:
    file2 = open(line1.strip("\n"),"r")
    for line2 in file2:
        if line2.split("\t")[0] not in dic_all.keys():
            dic_all[line2.split("\t")[0]]=[line2.split("\t")[1],line2.split("\t")[2]]
    file2.close()
file1.close()
file_list = open(sys.argv[1],"r")
for line_list in file_list:
    file_1 = open(line_list.strip("\n"),"r")
    dic_add = {}
    for line_1 in file_1:
        dic_add[line_1.split("\t")[0]] = line_1.split("\t")[-1].strip("\n")
    for key in dic_all.keys():
        if key in dic_add.keys() and key != "name":
            dic_all[key].append(dic_add[key])
        elif key == "name":
            dic_all[key].append(line_list.strip("\n"))
        else:
            dic_all[key].append("0")
file_out = open(sys.argv[2],"w")
for key in dic_all.keys():
    list_out = dic_all[key]
    n = 0
    str_out = key
    while n <= len(list_out)-1:
        str_out = str_out +"\t"+list_out[n] 
        n = n+1
    file_out.write(str_out+"\n")
