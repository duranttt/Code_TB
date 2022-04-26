#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    if line.startswith("#"):
        list_sample = line.split("\t")[1:]
        file2.write("#Kindom\tKindom\tPhylum\tClass\tOrder\tFamily\tGenus\tSpecies\t"+"\t".join(list_sample))
    else:
        list_number = line.split("\t")[1:]
        list_toxa = line.split("\t")[0].split("|")
        k=k1=p=c=o=f=g=s=""
        for name in list_toxa:
            if name.startswith("k__"):
                if name[3:] == "Viruses" or name[3:] == "Eukaryota" or name[3:] == "Archaea" or name[3:] == "Bacteria":
                    k = name[3:]
                else:
                    k1 = name[3:]
            elif name.startswith("p__"):
                p = name[3:].replace("_"," ")
            elif name.startswith("c__"):
                c = name[3:].replace("_"," ")
            elif name.startswith("o__"):
                o = name[3:].replace("_"," ")
            elif name.startswith("f__"):
                f = name[3:].replace("_"," ")
            elif name.startswith("g__"):
                g = name[3:].replace("_"," ")
            elif name.startswith("s__"):
                s = name[3:].replace("_"," ")
        file2.write(k+"\t"+k1+"\t"+p+"\t"+c+"\t"+o+"\t"+f+"\t"+g+"\t"+s+"\t"+"\t".join(list_number))
