#!/usr/bin/python3
import sys
file1=open(sys.argv[1],"r")
file2=open(sys.argv[2],"w")
file2.write("Sample\tCHROM\tPOS\tREF\tALT\tDP\tAF\tSB\tIMPACT\tEFFECT\tGENE\tBase\tAminoAcid\n")
for line in file1:
    file3 = open("04.ref_variation/"+line.split("\t")[0]+".anno","r")
    for line1 in file3:
        if line1.startswith("#"):
            continue
        else:
            list1 = line1.split("\t")
            list2 = line1.split("\t")[7].split(";")
            list3 = list2[4].split(",")
            sample = line.split("\t")[0]
            seqid = list1[0]
            pos = list1[1]
            ref = list1[3]
            alt = list1[4]
            dp = list2[0].split("=")[-1]
            af = list2[1].split("=")[-1]
            sb = list2[2].split("=")[-1]
            dp4 = list2[3].split("=")[-1]
            for info in list3:
                list4 = info.split("|")
                if list4[-1].startswith("WARNING"):
                    continue
                elif len(list4)<=10:
                    continue
                elif float(af) >0.5:
                    impact = list4[2]
                    effect = list4[1]
                    gene = list4[3]
                    if gene.startswith("CHR"):
                        gene = "None"
                    base = list4[9]
                    aminoacid = list4[10]
                    str1 = sample+"\t"+seqid+"\t"+pos+"\t"+ref+"\t"+alt+"\t"+dp+"\t"+af+"\t"+sb+"\t"+impact+"\t"+effect+"\t"+gene+"\t"+base+"\t"+aminoacid+"\n"
                    if base[2] == "-" or base[2] == "*":
                        continue
                    else:
                        file2.write(str1)
                        break
