#!/usr/bin/python
import sys
file_in = open(sys.argv[1],"r")
dic_in = {}
list_class = []
for line in file_in:
    if line.startswith("#"):
        title = line
    else:
        list1 = line.split("\t")[0].split("|")
        length = len(list1)
        n=0
        while n<=length-1:
            if n==0:
                classify = "|"+list1[1]
            elif n==length-1:
                classify = "|".join(list1[0:])
            else:
                classify = "|".join(list1[0:n+1])
            if classify not in list_class:
                list_class.append(classify)
            if classify not in dic_in.keys():
                dic_in[classify] = line.strip("\n").split("\t")[1:]
            else:
                list_after = []
                list_befor = dic_in[classify]
                i = 0
                while i<=len(list_befor)-1:
                    list_after.append(str(float(list_befor[i])+float(line.split("\t")[i+1])))
                    i=i+1
                dic_in[classify] = list_after
            n=n+1
file_out = open(sys.argv[2],"w")
file_out.write("\t".join(title.split("\t")[0:]))
for value in list_class:
    file_out.write(value+"\t"+"\t".join(dic_in[value])+"\n")
