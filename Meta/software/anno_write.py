#!/usr/bin/python
import sys
import pandas as pd
pd1 = pd.read_csv(sys.argv[1],sep="\t")
list_af = list(pd1.iloc[:,53])
list_alt_type = []
for value in list_af:
    if value == "1.00":
        list_alt_type.append("HOM")
    elif value == "0.500":
        list_alt_type.append("HET")
    else:
        list_alt_type.append(".")
pd1['Alt_type'] = list_alt_type
list_ref = list(pd1.iloc[:,3])
list_alt = list(pd1.iloc[:,4])
list_snp = []
n = 0
while n <= len(list_ref)-1:
    va = list_ref[n]+list_alt[n]
    if len(va) == 2:
        list_snp.append('snp')
    else:
        list_snp.append('indel')
    n = n + 1
pd1['SNP'] = list_snp
pd2 = pd1[["#Chr","Start","Gene.refGene","Depth","Ref","Alt","SNP","Alt_type","Alt_rate","Func.refGene","CLNALLELEID","CLNDN","CLNDISDB","CLNREVSTAT","CLNSIG","GeneDetail.refGene","ExonicFunc.refGene","AAChange.refGene","cytoBand","snp151","SIFT_score","SIFT_pred","Poly_HVAR_score","Poly_HVAR_pred","MutationTaster_score","MutationTaster_pred","FATHMM_score","FATHMM_pred","Poly_HDIV_score","Poly_HDIV_pred","LRT_score","LRT_pred","MutationAssessor_score","MutationAssessor_pred","M-CAP_score","M-CAP_pred","CADD_raw","CADD_phred","AFR.sites.2015_08","ALL.sites.2015_08","AMR.sites.2015_08","EAS.sites.2015_08","EUR.sites.2015_08","SAS.sites.2015_08","ExAC_ALL","ExAC_AFR","ExAC_AMR","ExAC_EAS","ExAC_FIN","ExAC_NFE","ExAC_OTH","ExAC_SAS","esp6500siv2_aa","esp6500siv2_all","esp6500siv2_ea","AF","AF_raw","AF_male","AF_female","AF_afr","AF_ami","AF_amr","AF_asj","AF_eas","AF_fin","AF_nfe","AF_oth","AF_sas","SiPhy_29way_logOdds","phyloP100way_vertebrate"]]
pd2 = pd2.rename(columns={"AFR.sites.2015_08":'1000_AFR',"ALL.sites.2015_08":'1000_ALL',"AMR.sites.2015_08":'1000_AMR',"EAS.sites.2015_08":'1000_EAS',"EUR.sites.2015_08":'1000_EUR',"SAS.sites.2015_08":'1000_SAS'})
pd3 = pd2
pd3.loc[pd3['SIFT_pred'] == "T",'SIFT_pred'] = "tolerated"
pd3.loc[pd3['SIFT_pred'] == "D",'SIFT_pred'] = "deleterious"
pd3.loc[pd3['Poly_HVAR_pred'] == "B",'Poly_HVAR_pred'] = "Benign"
pd3.loc[pd3['Poly_HVAR_pred'] == "P",'Poly_HVAR_pred'] = "Possibly damaging"
pd3.loc[pd3['Poly_HVAR_pred'] == "D",'Poly_HVAR_pred'] = "Probably damaging"
pd3.loc[pd3['Poly_HDIV_pred'] == "D",'Poly_HDIV_pred'] = "Probably damaging"
pd3.loc[pd3['Poly_HDIV_pred'] == "P",'Poly_HDIV_pred'] = "Possibly damaging"
pd3.loc[pd3['Poly_HDIV_pred'] == "B",'Poly_HDIV_pred'] = "Benign"
pd3.loc[pd3['MutationTaster_pred'] == "A",'MutationTaster_pred'] = "Disease_causing_automatic"
pd3.loc[pd3['MutationTaster_pred'] == "D",'MutationTaster_pred'] = "Disease_causing"
pd3.loc[pd3['MutationTaster_pred'] == "N",'MutationTaster_pred'] = "Polymorphism"
pd3.loc[pd3['MutationTaster_pred'] == "P",'MutationTaster_pred'] = "Polymorphism_automatic"
pd3.loc[pd3['FATHMM_pred'] == "D",'FATHMM_pred'] = "Deleterious"
pd3.loc[pd3['FATHMM_pred'] == "T",'FATHMM_pred'] = "Tolerated"
pd3.loc[pd3['LRT_pred'] == "D",'LRT_pred'] = "Deleterious"
pd3.loc[pd3['LRT_pred'] == "N",'LRT_pred'] = "Neutral"
pd3.loc[pd3['LRT_pred'] == "U",'LRT_pred'] = "Unknown"
pd3.loc[pd3['MutationAssessor_pred'] == "H",'MutationAssessor_pred'] = "High"
pd3.loc[pd3['MutationAssessor_pred'] == "M",'MutationAssessor_pred'] = "Medium"
pd3.loc[pd3['MutationAssessor_pred'] == "L",'MutationAssessor_pred'] = "Low"
pd3.loc[pd3['MutationAssessor_pred'] == "N",'MutationAssessor_pred'] = "Neutral"
pd3 = pd3[["#Chr","Start","Gene.refGene","Depth","Ref","Alt","SNP","Alt_type","Alt_rate","Func.refGene","CLNALLELEID","CLNDN","CLNDISDB","CLNREVSTAT","CLNSIG","GeneDetail.refGene","ExonicFunc.refGene","AAChange.refGene","cytoBand","snp151","SIFT_score","SIFT_pred","Poly_HVAR_score","Poly_HVAR_pred","MutationTaster_score","MutationTaster_pred","FATHMM_score","FATHMM_pred","Poly_HDIV_score","Poly_HDIV_pred","LRT_score","LRT_pred","MutationAssessor_score","MutationAssessor_pred","M-CAP_score","M-CAP_pred","CADD_raw","CADD_phred","1000_AFR","1000_ALL","1000_AMR","1000_EAS","1000_EUR","1000_SAS","ExAC_ALL","ExAC_AFR","ExAC_AMR","ExAC_EAS","ExAC_FIN","ExAC_NFE","ExAC_OTH","ExAC_SAS","esp6500siv2_aa","esp6500siv2_all","esp6500siv2_ea","AF","AF_raw","AF_male","AF_female","AF_afr","AF_ami","AF_amr","AF_asj","AF_eas","AF_fin","AF_nfe","AF_oth","AF_sas","SiPhy_29way_logOdds","phyloP100way_vertebrate"]]
pd3.to_csv(sys.argv[2])
