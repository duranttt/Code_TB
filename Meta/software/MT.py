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
    map_bam = "../02.bwa/"+name+".map.bam"
    out_vcf = "../03.gatk/"+name+".vcf"
    anno_vcf = "../04.result/"+name+".anno.vcf"
    step_fastp = "fastp -i {input1} -I {input2} -o {output1} -O {output2} -j {out_json} -h {out_html} -w 8\n"
    step_fastqc = "fastqc -f fastq {output1} -t 4;fastqc -f fastq {output2} -t 4\n"
    step_bwa = "bwa mem -R '@RG\\tID:NA\\tLB:NA\\tPL:BGI\\tPU:NA\\tSM:{name}' -t 8 /local/db/bwa/xlt.fasta {output1} {output2}|samtools view -Sb|samtools sort -O BAM -o {out_bam}\n"
    step_map = "samtools view -bF 4 {out_bam} > {map_bam}\n"
    step_rmdup = "/bio/gatk/gatk MarkDuplicates -I {map_bam} -O {rmdup_bam}  -M ../02.bwa/{name}.dup_metrics.txt --REMOVE_DUPLICATES true --java-options \"-Djava.io.tmpdir=../02.bwa/{name} -Xmx8g\"\n"
    step_index = "samtools index {rmdup_bam}\n"
    step_gatk = "/bio/gatk/gatk HaplotypeCaller -R /local/db/bwa/xlt.fasta -I {rmdup_bam} -O {out_vcf}\n"
    step_lofreq = "/bio/lofreq/bin/lofreq call {rmdup_bam} -f /local/db/bwa/xlt.fasta --call-indels -o ../03.gatk/{name}.ref.lofreq.vcf\n"
    step_anno = "python /bio/script/anno_m.py {out_vcf} {anno_vcf}"
    file2.write(step_fastp.format_map(vars())+step_fastqc.format_map(vars())+step_bwa.format_map(vars())+step_map.format_map(vars())+step_rmdup.format_map(vars())+step_index.format_map(vars())+step_gatk.format_map(vars())+step_lofreq.format_map(vars())+step_anno.format_map(vars()))
    n=n+1
