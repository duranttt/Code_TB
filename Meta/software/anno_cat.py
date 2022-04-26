#!/usr/bin/python
import sys
file_db = open(sys.argv[1],"r")
file_mul = open(sys.argv[2],"r")
file3 = open(sys.argv[3],"w")
dic_db = {}
for line_db in file_db:
    if line_db.startswith("#"):
        title_db = ""
        list_title_db = line_db.strip("\n").split("\t")
        n=4
        while n<=len(list_title_db)-1:
            title_db = title_db+"\t"+list_title_db[n]
            n=n+1
    else:
        list_db = line_db.strip("\n").split("\t")
        key_db = list_db[0]+"_"+list_db[1]+"_"+list_db[2]+"_"+list_db[3]
        value_db = line_db.strip(list_db[0]+"\t"+list_db[1]+"\t"+list_db[2]+"\t"+list_db[3])
        dic_db[key_db] = value_db

for line_mul in file_mul:
    if line_mul.startswith("#"):
        title_mul = "#Chr"
        list_title_mul = line_mul.strip("\n").strip("\t").split("\t")
        n=1
        while n<= len(list_title_mul)-1:
            title_mul = title_mul + "\t" + list_title_mul[n]
            n=n+1
        file3.write(title_mul+title_db+"\n")
    elif len(line_mul.split("\t")) >= 5:
        list_mul = line_mul.strip("\n").split("\t")
        key_mul = list_mul[0]+"_"+list_mul[1]+"_"+list_mul[3]+"_"+list_mul[4]
        if key_mul in dic_db.keys():
            file3.write(line_mul.strip("\n")+dic_db[key_mul].strip("\t"))
        else:
            file3.write(line_mul.strip("\n")+".\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\n")
