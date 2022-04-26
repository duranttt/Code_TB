#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    sample = line.split("\t")[0]
    file2.write("python3 /mnt/software/script/kreport2mpa.py -r 03.kraken/"+sample+"_s.report -o result/"+sample+".mpa --display-header\n")

