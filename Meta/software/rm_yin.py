#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    if line.startswith("#"):
        list_1 = line.split("\t")
        list_sample = list_1[0:-1]
        length = len(list_1)
        file2.write("\t".join(list_sample)+"\n")
    else:
        list_number = line.strip("\n").split("\t")
        n=1
        add = 0
        while n<length-1:
            if float(list_number[n])/2500<float(list_number[length-1]):
                list_number[n]=0
                add = add + list_number[n]
            else:
                add = add + float(list_number[n])
            n=n+1
        if add == 0:
            continue
        else:
            i=0
            while i<=length-2:
                if i==length-2:
                    file2.write(str(list_number[i])+"\n")
                else:
                    file2.write(str(list_number[i])+"\t")
                i=i+1
