#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open("/mnt/rawdata/dataset/test/names.xls","r")
dic_name = {}
for line in file2:
    dic_name[line.split("\t|\t")[0]] = line.split("\t|\t")[1]
file_node = open("/mnt/noxa/db/download/refseq/taxonomy/nodes.dmp","r")
dic_node = {}
for line in file_node:
    dic_node[line.split("\t|\t")[0]] = line.split("\t|\t")[2]
dic_class = {}
for line in file1:
    if line.startswith("U"):
        continue
    else:
        taxid = line.split("\t")[2]
        taxo = line.strip("\n").split("\t")[-1]
        max_kmer = 0
        for info in taxo.split():
            if info.split(":")[0] == taxid and int(info.split(":")[1]) > max_kmer:
                max_kmer = int(info.split(":")[1])
        if taxid in dic_class.keys() and max_kmer > int(sys.argv[2]):
            dic_class[taxid] = dic_class[taxid] + 1
        elif max_kmer > int(sys.argv[2]):
            dic_class[taxid] = 1
file3 = open(sys.argv[3],"w")
file3.write("#name\treads_number\ttaxid\n")
for key in dic_class.keys():
    if dic_node[key] == "species":
        file3.write(str(dic_name[key])+"\t"+str(dic_class[key])+"\t"+str(key)+"\n")
