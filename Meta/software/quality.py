#coding=utf-8
#!/usr/bin/python3
import pandas as pd
import sys
def quality(chip,lane,index):
    i,j=1,1
    file_r1 = open("/mnt/rawdata/"+chip+"/"+lane+"/"+chip.lower()+"_"+lane+"_"+index+"_1.fq.fqStat.txt","r")
    file_r2 = open("/mnt/rawdata/"+chip+"/"+lane+"/"+chip.lower()+"_"+lane+"_"+index+"_2.fq.fqStat.txt","r")
    for line_r1 in file_r1:
        if i==6:
            base1 = line_r1.split("\t")[1].strip("\n")
            i=i+1
        elif i==11:
            q1 = line_r1.split("\t")[1].strip("\n")
            break
        else:
            i=i+1
    for line_r2 in file_r2:
        if j==6:
            base2 = line_r2.split("\t")[1].strip("\n")
            j=j+1
        elif j==11:
            q2 = line_r2.split("\t")[1].strip("\n")
            break
        else:
            j=j+1
    base=round((float(base1)+float(base2))/1000000000,2)
    G = round((float(q1)+float(q2))/2,2)
    return base,G
pd1 = pd.read_excel(sys.argv[1])
file_out = open(sys.argv[2],"w")
for index,row in pd1.iterrows():
    list_in = list(row)
    if list_in[5] != "WES":
        list_lane = list_in[10].split("&")
        if "lane1" in list_lane:
            data1 = quality(list_in[11],"L01",list_in[3])[0]
            g1 = quality(list_in[11],"L01",list_in[3])[1]
        else:
            data1 = 0
            g1 = 0
        if "lane2" in list_lane:
            data2 = quality(list_in[11],"L02",list_in[3])[0]
            g2 = quality(list_in[11],"L02",list_in[3])[1]
        else:
            data2 = 0
            g2 = 0
        if "lane3" in list_lane:
            data3 = quality(list_in[11],"L03",list_in[3])[0]
            g3 = quality(list_in[11],"L03",list_in[3])[1]
        else:
            data3 = 0
            g3 = 0
        if "lane4" in list_lane:
            data4 = quality(list_in[11],"L04",list_in[3])[0]
            g4 = quality(list_in[11],"L04",list_in[3])[1]
        else:
            data4 = 0
            g4 = 0
        rawdata = data1 + data2 + data3 + data4
        g30 = round((g1 + g2 + g3 + g4)/len(list_lane),2)
        if g30 >= 80 and rawdata >= float(list_in[9])*0.85:
            qua = "合格"
        else:
            qua = "不合格"
        file_out.write(list_in[1]+"\t"+str(rawdata)+"\t"+str(g30)+"\t"+qua+"\n")
