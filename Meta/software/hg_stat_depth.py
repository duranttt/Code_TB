#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open("/home/user/CCDS.20180614.txt","r")
file3 = open(sys.argv[2],"w")
dic_cds = {}
list_chr = ["chr1","chr2","chr3","chr4","chr5","chr6","chr7","chr8","chr9","chr10","chr11","chr12","chr13","chr14","chr15","chr16","chr17","chr18","chr19","chr20","chr21","chr22","chrX","chrY"]
for ch in list_chr:
    dic_cds[ch] = {}
for line in file2:
    if line.startswith("#") or line.split("\t")[5] == "Withdrawn":
        continue
    elif line.split("\t")[9]=="-":
        continue
    else:
        chrom = "chr"+line.split("\t")[0]
        list_loc = line.split("\t")[9][1:-1].split(",")
        for tup in list_loc:
            left = int(tup.split("-")[0])
            right = int(tup.split("-")[1])
            if left in dic_cds[chrom].keys() and dic_cds[chrom][left] >= right:
                continue
            else:
                dic_cds[chrom][left] = right
n=0
sum_depth = 0
first_chr = ""
for line_d in file1:
    chrom = line_d.split("\t")[0]
    if chrom not in list_chr:
        continue
    if chrom != first_chr:
        first_chr = chrom
        list_left = []
        for key in dic_cds[chrom].keys():
            list_left.append(key)
        list_left.sort()
        i=0
    pos = int(line_d.split("\t")[1])
    depth = int(line_d.strip("\n").split("\t")[2])
    if depth < 10:
        continue
    else:
        if pos-1 < list_left[i]:
            continue
        elif list_left[i]<=pos-1<=dic_cds[chrom][list_left[i]]:
            n=n+1
            sum_depth = sum_depth+depth
        else:
            if i+1<= len(list_left)-1:
                i=i+1
            else:
                continue
file3.write(sys.argv[1].split(".")[0]+"\t"+str(n/33401146)+"\t"+str(sum_depth/33401146)+"\n")
                
