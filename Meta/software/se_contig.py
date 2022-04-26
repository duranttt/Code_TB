#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    if line.startswith("#"):
        continue
    else:
        sample = line.split("\t")[0]
        contig_num = line.split("\t")[1]
        file_in = open("05.megahit/"+sample+"/"+sample+".contigs.fa","r")
        wl = "F"
        for line_in in file_in:
            if line_in.startswith(">"):
                if line_in.split()[0][1:] == contig_num:
                    wl = "T"
                else:
                    wl = "F"
            else:
                wl = wl + "S"
            if wl == "TS":
                file2.write(">"+sample+"_"+contig_num+"\n"+line_in)
        file_in.close()
