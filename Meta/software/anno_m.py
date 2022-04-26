#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    if line.startswith("#"):
        continue
    else:
        if float(line.split("\t")[7].split(";")[1][3:]) >= 0.3:
            key = line.split("\t")[1]+"_"+line.split("\t")[3]+"_"+line.split("\t")[4]
            file_rs = open("/home/user/MT_rs.txt","r")
            for line_rs in file_rs:
                if line_rs.split("\t")[1]+"_"+line_rs.split("\t")[3]+"_"+line_rs.split("\t")[4] == key:
                    rs = line_rs.strip("\n").split("\t")[-1]
                    break
                else:
                    rs = "."
            file_rs.close()
            file_dis = open("/home/user/disease.txt","r")
            for line_dis in file_dis:
                if "-" in line_dis.split("\t")[3] and line_dis.split("\t")[2]+"_"+line_dis.split("\t")[3].split("-")[0]+"_"+line_dis.split("\t")[3].split("-")[1] == key:
                    disease = line_dis.split("\t")[6]
                    allele = line_dis.split("\t")[1]
                    dis_aa = line_dis.split("\t")[4]
                    homo = line_dis.split("\t")[5].split("/")[0]
                    het = line_dis.split("\t")[5].split("/")[1]
                    status = line_dis.split("\t")[7]
                    refs = line_dis.split("\t")[10].strip("\n")
                    break
                else:
                    disease = "."
                    allele = "."
                    dis_aa = "."
                    homo = "."
                    het = "."
                    status = "."
                    refs = "."
            file_dis.close()
            file_som = open("/home/user/somatic.txt","r")
            for line_som in file_som:
                if "-" in line_som.split("\t")[2] and line_som.split("\t")[0]+"_"+line_som.split("\t")[2].split("-")[0]+"_"+line_som.split("\t")[2].split("-")[1] == key:
                    som_locus = line_som.split("\t")[1]
                    som_aa = line_som.split("\t")[3]
                    som_hom = line_som.split("\t")[4]
                    som_het = line_som.split("\t")[5]
                    som_cell = line_som.split("\t")[6]
                    som_note = line_som.split("\t")[7]
                    break
                else:
                    som_locus = "."
                    som_aa = "."
                    som_hom = "."
                    som_het = "."
                    som_cell = "."
                    som_note = "."
            file_som.close()
            file_gene = open("/home/user/genbank_haplogroup_count.csv","r")
            for line_gene in file_gene:
                if line_gene.split(",")[0]+"_"+line_gene.split(",")[1]+"_"+line_gene.split(",")[2] == key:
                    codon_number = line_gene.split(",")[8]
                    codon_change = line_gene.split(",")[7]
                    locus = line_gene.split(",")[10]
                    break
                else:
                    codon_number = "."
                    codon_change = "."
                    locus = "."
            file_gene.close()
            file_dise = open("/home/user/disease.vcf","r")
            for line_out in file_dise:
                if line_out.startswith("#"):
                    continue
                else:
                    n=0
                    list_alt = line_out.split("\t")[3].split(",")
                    while n<=len(list_alt)-1:
                        if line_out.split("\t")[0]+"_"+line_out.split("\t")[2]+"_"+list_alt[n] == key:
                            list_out = line_out.strip("\n").split("\t")[-1].split(";")
                            AF = "."
                            for value in list_out:
                                if value.startswith("AF"):
                                    AF=value[3:].split(",")[n]
                                if value.startswith("aachange"):
                                    dis_aa = value.split("=")[1]
                                if value.startswith("hom"):
                                    homo = value.split("=")[1].split(",")[n]
                                if value.startswith("het"):
                                    het = value.split("=")[1].split(",")[n]
                                if value.startswith("Disease="):
                                    disease = value.split("=")[1].split(",")[n]
                                if value.startswith("DiseaseStatus"):
                                    status = value.split("=")[1].split(",")[n]
                        else:
                            AF = "."
                        n=n+1
            file_dise.close()
            file_score = open("/home/user/mitotip_scores.txt","r")
            for line_score in file_score:
                if line_score.startswith("Pos"):
                    continue
                else:
                    if line_score.split("\t")[0]+"_"+line_score.split("\t")[1]+"_"+line_score.split("\t")[2] == key:
                        MitoTIP = line_score.split("\t")[3]
                        Quartile = line_score.split("\t")[4]
                    else:
                        MitoTIP = "."
                        Quartile = "."
            file_score.close()
            file2.write("chrM"+"\t"+line.split("\t")[1]+"\t"+line.split("\t")[3]+"\t"+line.split("\t")[4]+"\t"+rs+"\t"+line.split("\t")[7].split(";")[0][3:]+"\t"+line.split("\t")[7].split(";")[1][3:]+"\t"+locus+"\t"+AF+"\t"+disease+"\t"+allele+"\t"+MitoTIP+"\t"+Quartile+"\t"+line.split("\t")[3]+"-"+line.split("\t")[4]+"\t"+dis_aa+"\t"+homo+"\t"+het+"\t"+status+"\t"+refs+"\t"+som_locus+"\t"+som_aa+"\t"+som_hom+"\t"+som_het+"\t"+som_cell+"\t"+som_note+"\t"+codon_number+"\t"+codon_change+"\n")
