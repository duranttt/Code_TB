#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open("/bio/annovar/humandb/hg38_dbnsfp33a.txt","r")
file3 = open(sys.argv[2],"w")
file3.write("#CHR\tPOS\tREF\tALT\tQUAL\tFILTER\tAlt_rate\tDP\tSIFT_score\tSIFT_pred\tPoly_HDIV_score\tPoly_HDIV_pred\tPoly_HVAR_score\tPoly_HVAR_pred\tLRT_score\tLRT_pred\tMutationTaster_score\tMutationTaster_pred\tMutationAssessor_score\tMutationAssessor_pred\tFATHMM_score\tFATHMM_pred\tM-CAP_score\tM-CAP_pred\tCADD_raw\tCADD_phred\tGERP++_RS\tGERP++_RS_rankscore\tphyloP100way_vertebrate\tphyloP100way_vertebrate_rankscore\tphyloP20way_mammalian\tphyloP20way_mammalian_rankscore\tSiPhy_29way_logOdds\tSiPhy_29way_logOdds_rankscore\tInterpro_domain\n")
dic_need = {}
for line in file1:
    if line.startswith("#"):
        continue
    else:
        list_n = line.split("\t")
        key_need = list_n[0]+"_"+list_n[1]+"_"+list_n[3]+"_"+list_n[4]
        for anno in line.split("\t")[7].split(";"):
            if anno.startswith("AF"):
                AF = anno[3:]
            elif anno.startswith("DP"):
                DP = anno[3:]
        value_need = list_n[0]+"\t"+list_n[1]+"\t"+list_n[3]+"\t"+list_n[4]+"\t"+list_n[5]+"\t"+list_n[6]+"\t"+AF+"\t"+DP
        dic_need[key_need] = value_need
for line2 in file2:
    if line2.startswith("#"):
        continue
    else:
        list1 = line2.split("\t")
        name = "chr"+list1[0]+"_"+list1[1]+"_"+list1[3]+"_"+list1[4]
        velue = ""
        n=0
        while n<=len(list1):
            if n==5 or n==7 or n==8 or n==10 or n==11 or n==13 or n==14 or n==16 or n==17 or n==19 or n==20 or n==22 or n==23 or n==25 or n==37 or n==39 or n==40 or n==42 or n==56 or n==57 or n==58 or n==59 or n==60 or n==61 or n==66 or n==67 or n==68:
                velue = velue+"\t"+list1[n]
            n=n+1
        if name in dic_need.keys():
            file3.write(dic_need[name]+velue+"\n")
