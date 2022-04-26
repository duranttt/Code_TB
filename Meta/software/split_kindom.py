#!/usr/bin/python
import sys
file_in = open(sys.argv[1],"r")
file_vir = open(sys.argv[1].split(".")[0]+"_vir.mpa","w")
file_arc = open(sys.argv[1].split(".")[0]+"_arc.mpa","w")
file_euk = open(sys.argv[1].split(".")[0]+"_euk.mpa","w")
file_bac = open(sys.argv[1].split(".")[0]+"_bac.mpa","w")
list_vir = []
list_bac = []
list_euk = []
list_arc = []
for line in file_in:
    if line.startswith("#"):
        i=1
        while i <= len(line.split("\t"))-2:
            list_vir.append(0)
            list_euk.append(0)
            list_arc.append(0)
            list_bac.append(0)
            i=i+1
    else:
        if line.startswith("|k__Bac"):
            i=0
            while i<=len(list_bac)-1:
                list_bac[i] = list_bac[i]+float(line.split("\t")[i+1])
                i=i+1
        elif line.startswith("|k__Arc"):
            i=0
            while i<=len(list_arc)-1:
                list_arc[i] = list_arc[i]+float(line.split("\t")[i+1])
                i=i+1
        elif line.startswith("|k__Euk"):
            i=0
            while i<=len(list_euk)-1:
                list_euk[i] = list_euk[i]+float(line.split("\t")[i+1])
                i=i+1
        else:
            i=0
            while i<=len(list_vir)-1:
                list_vir[i] = list_vir[i]+float(line.split("\t")[i+1])
                i=i+1
file_in.close()
list_pi_arc = []
list_pi_bac = []
list_pi_euk = []
list_pi_vir = []
n_bac = 0
n_arc = 0
n_vir = 0
n_euk = 0
file_in = open(sys.argv[1],"r")
for line in file_in:
    if line.startswith("#"):
        list_sample = line.split("\t")[0:-1]
        list_out = []
        for value in list_sample:
            list_out.append(value)
        file_vir.write("\t".join(list_out)+"\n")
        file_arc.write("\t".join(list_out)+"\n")
        file_bac.write("\t".join(list_out)+"\n")
        file_euk.write("\t".join(list_out)+"\n")
        i=1
        while i <= len(line.split("\t"))-2:
            list_pi_vir.append(0)
            list_pi_euk.append(0)
            list_pi_arc.append(0)
            list_pi_bac.append(0)
            i=i+1
    elif line.startswith("|k__Bac"):
        n_bac = n_bac+1 
        if n_bac >=30:
            continue
        else:
            i=0
            file_bac.write("s__"+line.split("\t")[0].split("|")[-1][3:].replace("_"," ")+"\t"+"\t".join(line.split("\t")[1:-1])+"\n")
            while i<=len(list_pi_bac)-1:
                list_pi_bac[i] = list_pi_bac[i]+float(line.split("\t")[i+1])
                i=i+1
    elif line.startswith("|k__Euk"):
        n_euk = n_euk+1
        if n_euk >=30:
            continue
        else:
            i=0
            file_euk.write("s__"+line.split("\t")[0].split("|")[-1][3:].replace("_"," ")+"\t"+"\t".join(line.split("\t")[1:-1])+"\n")
            while i<=len(list_pi_euk)-1:
                list_pi_euk[i] = list_pi_euk[i]+float(line.split("\t")[i+1])
                i=i+1
    elif line.startswith("|k__Arc"):
        n_arc = n_arc+1
        if n_arc >=30:
            continue
        else:
            i=0       
            file_arc.write("s__"+line.split("\t")[0].split("|")[-1][3:].replace("_"," ")+"\t"+"\t".join(line.split("\t")[1:-1])+"\n")
            while i<=len(list_pi_arc)-1:
                list_pi_arc[i] = list_pi_arc[i]+float(line.split("\t")[i+1])
                i=i+1
    elif line.startswith("|k__Vir"):
        n_vir = n_vir+1
        if n_vir >=30:
            continue
        else:
            i=0      
            file_vir.write("s__"+line.split("\t")[0].split("|")[-1][3:].replace("_"," ")+"\t"+"\t".join(line.split("\t")[1:-1])+"\n")
            while i<=len(list_pi_vir)-1:
                list_pi_vir[i] = list_pi_vir[i]+float(line.split("\t")[i+1])
                i=i+1
m=0
str_bac = "others"
str_arc = "others"
str_euk = "others"
str_vir = "others"
while m<=len(list_bac)-1:
    str_bac = str_bac + "\t"+str(list_bac[m]-list_pi_bac[m])
    str_arc = str_arc + "\t"+str(list_arc[m]-list_pi_arc[m])
    str_euk = str_euk + "\t"+str(list_euk[m]-list_pi_euk[m])
    str_vir = str_vir + "\t"+str(list_vir[m]-list_pi_vir[m])
    m=m+1
file_bac.write(str_bac)
file_vir.write(str_vir)
file_euk.write(str_euk)
file_arc.write(str_arc)
