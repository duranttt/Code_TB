#!/usr/bin/python
import sys
import subprocess
subprocess.call("mkdir 01.clean;mkdir 02.bwa;mkdir 03.gatk;mkdir 04.result;mkdir w1.shell.sh",shell=True)
file_sample = open(sys.argv[1],"r")
n=1
for line in file_sample:
    if n<10:
        sh_name = "w0"+str(n)+"."+line.split("\t")[0]+".sh"
    else:
        sh_name = "w"+str(n)+"."+line.split("\t")[0]+".sh"
    file2 = open("w1.shell.sh/"+sh_name,"w")
    list_sample = line.strip("\n").split("\t")
    input1 = list_sample[1]
    input2 = list_sample[2]
    name = list_sample[0]
    output1 = "../01.clean/"+name+".clean.R1.fq.gz"
    output2 = "../01.clean/"+name+".clean.R2.fq.gz"
    out_json = "../01.clean/"+name+".json"
    out_html = "../01.clean/"+name+".html"
    out_bam = "../02.bwa/"+name+".bam"
    rmdup_bam = "../02.bwa/"+name+".rmdup.bam"
    out_vcf = "../03.gatk/"+name+".vcf"
    avinput = "../03.gatk/"+name+".avinput"
    db_vcf = "../03.gatk/"+name+".db.vcf"
    result_name = "../03.gatk/"+name
    cat_result = "../03.gatk/"+name+".result.vcf"
    result = "../03.gatk/"+name+"_anno_down.vcf"
    region_result = "../04.result/"+name+"_region.vcf"
    omim_result = "../04.result/"+name+"_omim.vcf"
    step_fastp = "fastp -i {input1} -I {input2} -o {output1} -O {output2} -j {out_json} -h {out_html} -w 8\n"
    step_fastqc = "fastqc -f fastq {output1} -t 4;fastqc -f fastq {output2} -t 4\n"
    step_bwa = "bwa mem -R '@RG\\tID:NA\\tLB:NA\\tPL:BGI\\tPU:NA\\tSM:{name}' -t 8 /local/db/human/hg38.fa {output1} {output2}|samtools view -Sb|samtools sort -O BAM -o {out_bam}\n"
    step_rmdup = "/bio/gatk/gatk MarkDuplicates -I {out_bam} -O {rmdup_bam}  -M ../02.bwa/{name}.dup_metrics.txt --REMOVE_DUPLICATES true --java-options \"-Djava.io.tmpdir=../02.bwa/{name} -Xmx8g\""
    step_index = "samtools index {rmdup_bam}\n"
    step_gatk = "/bio/gatk/gatk HaplotypeCaller -R /local/db/human/hg38.fa -I {rmdup_bam} -O {out_vcf}\n"
    step_vcf = "python /bio/script/vcf_avinput.py {out_vcf} {avinput}\n"
    step_anno = "python /bio/script/anno_db.py {out_vcf} {db_vcf}\n/bio/annovar/table_annovar.pl {avinput} /bio/annovar/humandb/ -buildver hg38 -out {result_name} -remove -protocol refGene,cytoBand,clinvar_20210123,AFR.sites.2015_08,ALL.sites.2015_08,AMR.sites.2015_08,EAS.sites.2015_08,EUR.sites.2015_08,SAS.sites.2015_08,avsnp150,exac03,dbscsnv11,esp6500siv2_aa,esp6500siv2_all,esp6500siv2_ea,gnomad30_genome,snp151 -operation gx,r,f,f,f,f,f,f,f,f,f,f,f,f,f,f,f -nastring . -csvout -polish\n"
    step_replace = "sed -i \"s#,#\\t#g\" {result_name}.hg38_multianno.csv\n"
    step_cat = "python /bio/script/anno_cat.py {db_vcf} {result_name}.hg38_multianno.csv {cat_result}\n"
    step_write = "python /bio/script/anno_write.py {cat_result} {result}\n"
    step_pick = "python /bio/script/pick_region.py {result} {region_result}\n"
    step_rep = "sed -i \"s#,#\\t#g\" {region_result}\n"
    step_omim = "python /bio/script/se_omim.py /local/db/genemap2.txt {region_result} {omim_result}\n"
    file2.write("echo \"clean start\" `date`>> ./"+sh_name[0:-2]+"time.log\n"+step_fastp.format_map(vars())+step_fastqc.format_map(vars())+"echo \"clean end and bwa start\" `date`>> ./"+sh_name[0:-2]+"time.log\n"+step_bwa.format_map(vars())+step_index.format_map(vars())+"echo \"bwa end and gatk start\" `date`>> ./"+sh_name[0:-2]+"time.log\n"+step_gatk.format_map(vars())+step_vcf.format_map(vars())+step_anno.format_map(vars())+step_replace.format_map(vars())+step_cat.format_map(vars())+step_write.format_map(vars())+step_pick.format_map(vars())+step_rep.format_map(vars())+step_omim.format_map(vars()))
    n=n+1
