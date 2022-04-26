#!/usr/bin/python3
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
file2.write("class_data=[\n")
for line in file1:
    sample = line.split("\t")[0]
    file_in = open("03.kraken/"+sample+"_s.report","r")
    euk,bac,arc,vir = 0,0,0,0
    for line_in in file_in:
        if line_in.strip("\n").split("\t")[-1].strip(" ")=="root":
            root = line_in.strip("\n").split("\t")[1]
        elif line_in.strip("\n").split("\t")[-1].strip(" ")=="Eukaryota":
            euk = line_in.strip("\n").split("\t")[1]
        elif line_in.strip("\n").split("\t")[-1].strip(" ")=="Bacteria":
            bac = line_in.strip("\n").split("\t")[1]
        elif line_in.strip("\n").split("\t")[-1].strip(" ")=="Archaea":
            arc = line_in.strip("\n").split("\t")[1]
        elif line_in.strip("\n").split("\t")[-1].strip(" ")=="Viruses":
            vir = line_in.strip("\n").split("\t")[1]
        else:
            continue
        euk_rate = round(float(euk)/float(root)*100,2)
        bac_rate = round(float(bac)/float(root)*100,2)
        arc_rate = round(float(arc)/float(root)*100,2)
        vir_rate = round(float(vir)/float(root)*100,2)
    file2.write("{\"SampleID\":\""+sample+"\",\n"+"\"Root\":\""+str(root)+"\",\n"+"\"Eukaryota\":\""+str(euk)+"\",\n"+"\"Euk_rate(%)\":\""+str(euk_rate)+"\",\n"+"\"Bacteria\":\""+str(bac)+"\",\n"+"\"Bac_rate(%)\":\""+str(bac_rate)+"\",\n"+"\"Archaea\":\""+str(arc)+"\",\n"+"\"Arc_rate(%)\":\""+str(arc_rate)+"\",\n"+"\"Viruses\":\""+str(vir)+"\",\n"+"\"Vir_rate(%)\":\""+str(vir_rate)+"\"\n},\n")
file2.write("]\n")
file2.write("\n")
