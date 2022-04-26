#!/usr/bin/python
import sys
import subprocess
file_1= open(sys.argv[1]+".clean.R1.fq","r")
file_2 = open(sys.argv[1]+".clean.R2.fq","r")
file_primer = open("/mnt/software/script/primer.txt","r")
file_1out = open(sys.argv[1]+".rmprimer.R1.fq","w")
file_2out = open(sys.argv[1]+".rmprimer.R2.fq","w")
list_primer_1 = []
list_primer_2 = []
for line in file_primer:
    if line.startswith("#"):
        continue
    else:
        list_primer_1.append(line.split("\t")[5])
        list_primer_2.append(line.split("\t")[6])
n=1
for line in file_1:
    if n%4==1:
        file_1out.write(line)
    elif n%4==2:
        l=1
        for primer in list_primer_1:
            if line.startswith(primer):
                l = len(primer)
                break
            else:
                continue
        file_1out.write(line[l-1:])
    elif n%4==3:
        file_1out.write("+\n")
    else:
        file_1out.write(line[l-1:])
    n=n+1
file_1out.close()
file_1.close()
n=1
for line in file_2:
    if n%4==1:
        file_2out.write(line)
    elif n%4==2:
        l=1
        for primer in list_primer_2:
            if line.startswith(primer):
                l = len(primer)
                break
            else:
                continue
        file_2out.write(line[l-1:])
    elif n%4==3:
        file_2out.write("+\n")
    else:
        file_2out.write(line[l-1:])
    n=n+1
file_2out.close()
file_2.close()
