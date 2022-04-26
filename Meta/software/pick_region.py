#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
list_pi = ["exonic","exonic;splicing","UTR5;UTR3","intronic","splicing","ncRNA_intronic","UTR3","UTR5"]
for line in file1:
    if line.split(",")[10] in list_pi:
        file2.write(line)
    elif "#Chr" in line:
        file2.write(line)

