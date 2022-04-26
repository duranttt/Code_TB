#!/usr/bin/python
import sys
file_vir = open(sys.argv[1],"r")
file_arc = open(sys.argv[2],"r")
file_bac = open(sys.argv[3],"r")
file_euk = open(sys.argv[4],"r")
file_out = open(sys.argv[5],"w")
dic_vir = {}
dic_bac = {}
dic_arc = {}
dic_euk = {}
for line in file_vir:
    if line.startswith("#"):
        list1 = line.strip("\n").split("\t")
    else:
        list2 = line.strip("\n").split("\t")
        n=1
        while n<= len(list1)-1:
            dic_vir[list2[0]+"\t"+list1[n]] = list2[n]
            n=n+1
for line in file_arc:
    if line.startswith("#"):
        list1 = line.strip("\n").split("\t")
    else:
        list2 = line.strip("\n").split("\t")
        n=1
        while n<= len(list1)-1:
            dic_arc[list2[0]+"\t"+list1[n]] = list2[n]
            n=n+1
for line in file_bac:
    if line.startswith("#"):
        list1 = line.strip("\n").split("\t")
    else:
        list2 = line.strip("\n").split("\t")
        n=1
        while n<= len(list1)-1:
            dic_bac[list2[0]+"\t"+list1[n]] = list2[n]
            n=n+1
for line in file_euk:
    if line.startswith("#"):
        list1 = line.strip("\n").split("\t")
    else:
        list2 = line.strip("\n").split("\t")
        n=1
        while n<= len(list1)-1:
            dic_euk[list2[0]+"\t"+list1[n]] = list2[n]
            n=n+1
list_vir = list(dic_vir.keys())
list_bac = list(dic_bac.keys())
list_arc = list(dic_arc.keys())
list_euk = list(dic_euk.keys())
file_out.write("vir\tsample_vir\trpm_vir\tarc\tsample_arc\trpm_arc\tbac\tsample_bac\trpm_bac\teuk\tsample_euk\trpm_euk\n")
i=0
while i<= len(list_bac)-1:
    if i >= len(list_vir):
        vir = " "
        sample_vir = " "
        rpm_vir = " "
    else:
        vir = list_vir[i].split("\t")[0]
        sample_vir = list_vir[i].split("\t")[1]
        rpm_vir = dic_vir[list_vir[i]]
    if i >= len(list_arc):
        arc = " "
        sample_arc = " "
        rpm_arc = " "
    else:
        arc = list_arc[i].split("\t")[0]
        sample_arc = list_arc[i].split("\t")[1]
        rpm_arc = dic_arc[list_arc[i]]
    if i >= len(list_euk):
        euk = " "
        sample_euk = " "
        rpm_euk = " "
    else:
        euk = list_euk[i].split("\t")[0]
        sample_euk = list_euk[i].split("\t")[1]
        rpm_euk = dic_euk[list_euk[i]]
    bac = list_bac[i].split("\t")[0]
    sample_bac = list_bac[i].split("\t")[1]
    rpm_bac = dic_bac[list_bac[i]]
    file_out.write(vir+"\t"+sample_vir+"\t"+rpm_vir+"\t"+arc+"\t"+sample_arc+"\t"+rpm_arc+"\t"+bac+"\t"+sample_bac+"\t"+rpm_bac+"\t"+euk+"\t"+sample_euk+"\t"+rpm_euk+"\n")
    i=i+1
