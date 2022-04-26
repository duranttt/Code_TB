#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file_out = open(sys.argv[1].split("_")[0]+".out.fasta","w")
for line in file1:
    if line.split("\t")[-1].strip("\n") == "Archaea":
        file_out.write(">"+line.split("\t")[0]+"\n"+line.split("\t")[9]+"\n")
    elif line.split("\t")[-1].strip("\n") == "Eukaryota":
        file_out.write(">"+line.split("\t")[0]+"\n"+line.split("\t")[9]+"\n")
    elif line.split("\t")[-1].strip("\n") == "Bacteria":
        file_out.write(">"+line.split("\t")[0]+"\n"+line.split("\t")[9]+"\n")
    elif line.split("\t")[-1].strip("\n") == "Viruses":
        file_out.write(">"+line.split("\t")[0]+"\n"+line.split("\t")[9]+"\n")

