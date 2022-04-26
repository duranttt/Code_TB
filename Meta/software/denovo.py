#!/usr/bin/python3
import sys
import subprocess
subprocess.call("mkdir 01.clean;mkdir 05.bwa;mkdir 06.megahit;mkdir 07.blast;mkdir shell_hisat",shell=True)
file1 = open(sys.argv[1],"r")
for line in file1:
    file2 = open("shell_hisat/D_"+line.split("\t")[0]+".sh","w")
    list1 = line.strip("\n").split("\t")
    step_fastp = "#date >> B_{name}.log ; fastp -i {input1} -I {input2} -o {output1} -O {output2} -j {json} -h {html} -w 16 >> B_{name}.log;date >> B_{name}.log\n"
    name = list1[0]
    input1 = list1[1]
    input2 = list1[2]
    output1 = "../01.clean/"+list1[0]+".clean.R1.fq.gz"
    output2 = "../01.clean/"+list1[0]+".clean.R2.fq.gz"
    json = "../01.clean/"+list1[0]+".json"
    html = "../01.clean/"+list1[0]+".html"
    step_bwa = "bwa mem -t 8 /local/db/human/hg38.fa {output1} {output2} | samtools view -bf 4 |samtools view|"
    str1 = "awk \'{OFS=\"\\t\";print \">\"$1\"\\n\"$10}\' "+"- > ../05.bwa/"+list1[0]+".fasta\n"
    step_megahit = "/bio/megahit/megahit/bin/megahit -r ../05.bwa/{name}.fasta -o ../06.megahit/{name}\n"
    step_blast = "blastn -query ../06.megahit/{name}/final.contigs.fa -db /local/db/blast_db/nt -out ../07.blast/{name}.blast -outfmt '6 qseqid qlen sseqid slen qstart qend sstart send qcovs evalue pident length mismatch sstrand bitscore stitle' -num_alignments 1 -max_hsps 1"
    file2.write(step_fastp.format_map(vars())+step_bwa.format_map(vars())+str1+step_megahit.format_map(vars())+step_blast.format_map(vars()))
