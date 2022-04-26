#!/usr/bin/python
import sys
file_in = open(sys.argv[1],"r")
file_out = open(sys.argv[2],"w")
dic_out = {}
file_clean = open(sys.argv[3],"r")
dic_clean = {}
for line in file_clean:
    if line.startswith("#"):
        continue
    else:
        dic_clean[line.split("\t")[0]] = float(line.split("\t")[1])*1000000
for line in file_in:
    if line.startswith("#"):
        list_sample = line.strip("\n").split("\t")[1:]
        list_rawreads = []
        for sample in list_sample:
            list_rawreads.append(dic_clean[sample])
        file_out.write(line.strip("\n")+"\trpm_add\n")
    else:
        list1 = line.strip("\n").split("\t")
        list2 = []
        i=1
        while i<= len(list1)-1:
            rpm = int(list1[i])/list_rawreads[i-1]*1000000
            list2.append(rpm)
            i=i+1
        sum_rpm = 0
        str_out = line.split("\t")[0]
        for rpm in list2:
            sum_rpm = sum_rpm + rpm
            str_out = str_out + "\t" + str(rpm)
        list2.append(sum_rpm)
        dic_out[str_out] = sum_rpm
list_dic = sorted(dic_out.items(),key=lambda kv:(kv[1],kv[0]),reverse=True)
for value in list_dic:
    file_out.write(value[0]+"\t"+str(value[1])+"\n")
