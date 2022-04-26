#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
for line in file1:
    if line.strip("\n").split("\t")[-1] == "Y":
        continue
    else:
        file_out = open("03.kraken/"+line.split("\t")[0]+"_virus_taxid.list","w")
        file_in = open(sys.argv[2],"r")
        list_spe = []
        for line_in in file_in:
            if line_in.startswith("#"):
                list_sample = line_in.strip("\n").split("\t")
                position = list_sample.index(line.split("\t")[0])
            else:
                if line_in.startswith("|k__Viruses"):
                    list_out = line_in.strip("\n").split("\t")
                    if int(list_out[position]) != 0:
                        list_spe.append(line_in.split("\t")[0].split("|")[-2][3:].replace("_"," "))
        list_taxid = []
        file_taxid = open("/mnt/noxa/db/ranked/Vir_taxid.dmp","r")
        for line_tax in file_taxid:
            if line_tax.strip("\n").split("|")[-2][3:] in list_spe:
                taxid = line_tax.split("\t")[1]
                if taxid not in list_taxid:
                    list_taxid.append(taxid)
        file_taxid.close()
        for value in list_taxid:
            file_out.write(value+"\n")
        file_in.close()
