#!/usr/bin/python
#-*- coding:UTF-8 -*-
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
file2.write("#Sample\tRawReads(M)\tRawBase(G)\tRawData_Q20\tRawData_Q30\tRawData_GC\tCleanReads(M)\tCleanReads(G)\tCleanData_Q20\tCleanData_Q30\tCleanData_GC\n")
for line1 in file1:
    if line1.strip("\n").split("\t")[-1] == "Y":
        continue
    else:
        file_json = open("01.clean/"+line1.split("\t")[0]+".json","r")
        n=1
        for line_json in file_json:
            if n==4:
                reads = str(round(float(line_json.split(":")[1].split(",")[0])/1000000,2))
            elif n==5:
                base = str(round(float(line_json.split(":")[1].split(",")[0])/1000000000,2))
            elif n==8:
                q20 = str(round(float(line_json.split(":")[1].split(",")[0])*100,2))
            elif n==9:
                q30 = str(round(float(line_json.split(":")[1].split(",")[0])*100,2))
            elif n==12:
                qc = str(round(float(line_json.split(":")[1].split(",")[0])*100,2))
            elif n==15:
                c_reads = str(round(float(line_json.split(":")[1].split(",")[0])/1000000,2))
            elif n==16:
                c_base = str(round(float(line_json.split(":")[1].split(",")[0])/1000000000,2))
            elif n==19:
                c_q20 = str(round(float(line_json.split(":")[1].split(",")[0])*100,2))
            elif n==20:
                c_q30 = str(round(float(line_json.split(":")[1].split(",")[0])*100,2))
            elif n==23:
                c_qc = str(round(float(line_json.split(":")[1].split(",")[0])*100,2))
            n=n+1
        if float(q30)<80 or float(base)<21.25:
            file2.write(line1.split("\t")[0]+"\t"+base+"\t"+q30+"\t"+"不合格"+"\n")
        else:
            file2.write(line1.split("\t")[0]+"\t"+base+"\t"+q30+"\t"+"合格"+"\n")
#        file2.write(line1.split("\t")[0]+"\t"+reads+"\t"+base+"\t"+q20+"\t"+q30+"\t"+qc.strip("\n")+"\t"+c_reads+"\t"+c_base+"\t"+c_q20+"\t"+c_q30+"\t"+c_qc+"\n")
