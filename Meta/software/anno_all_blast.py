#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"r")
file3 = open(sys.argv[3],"w")
file3.write("#Sample\tContig_id\tContig_len\tRef_id\tRef_len\tQ_start\tQ_end\tS_start\tS_end\tE-value\tPident\tStrand\tBitscore\tSeq\tRef_name\tKindom\tTaxo\tHost\tgenome composition\n")
dic_an = {}
for line2 in file2:
    dic_an[line2.split("\t")[0]] = line2.split("\t")[2]+"\t"+line2.split("\t")[3]+"\t"+line2.strip("\n").split("\t")[4]

for line in file1:
    if line.startswith("#"):
        file3.write(line)
    elif "Viruses" in line or "virus" in line:
        if "|" in line.split("\t")[3] and line.split("\t")[3].split("|")[1] in dic_an.keys():
            file3.write(line.strip("\n")+"\t"+dic_an[line.split("\t")[3].split("|")[1]]+"\n")
        elif line.split("\t")[3] in dic_an.keys():
            file3.write(line.strip("\n")+"\t"+dic_an[line.split("\t")[3]]+"\n")
        else:
            file3.write(line.strip("\n")+"\t-\n")
