#!/usr/bin/python
import sys
file1=open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    if line.split("\t")[-1].strip("\n") == "Y":
        continue
    else:
        file2.write("<li><a id=\"example2\" href=\"src/pictures/"+line.split("\t")[0]+"_qua.png\" ><img src=\"src/pictures/"+line.split("\t")[0]+"_qua.png\" alt=\""+line.split("\t")[0]+"_qua.png\" title=\""+line.split("\t")[0]+"_qua.png\" /></a></li>\n")
    
