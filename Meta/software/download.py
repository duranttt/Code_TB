#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    n = line.split("\t")[0].strip("\n")
    file2.write("/mnt/work/dudongdong/anaconda3/bin/efetch -db nuccore -format fasta -id "+n+"> "+sys.argv[3]+"/"+n+".fasta\n")
