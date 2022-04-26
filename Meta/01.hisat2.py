#!/usr/bin/python3
import sys
import subprocess
subprocess.call("mkdir 01.clean;mkdir 02.hisat;mkdir 03.kraken;mkdir shell_hisat",shell=True)
file1 = open(sys.argv[1],"r")
file3 = open("kraken.sh","w")
file4 = open("braken.sh","w")
for line in file1:
    file2 = open("shell_hisat/B_"+line.split("\t")[0]+".sh","w")
    list1 = line.strip("\n").split("\t")
    step_fastp = "date >> B_{name}.log ; fastp -i {input1} -I {input2} -o {output1} -O {output2} -j {json} -h {html} -w 16 >> B_{name}.log;date >> B_{name}.log"
    name = list1[0]
    input1 = list1[1]
    input2 = list1[2]
    output1 = "../01.clean/"+list1[0]+".clean.R1.fq.gz"
    output2 = "../01.clean/"+list1[0]+".clean.R2.fq.gz"
    json = "../01.clean/"+list1[0]+".json"
    html = "../01.clean/"+list1[0]+".html"
    file2.write(step_fastp.format_map(vars())+"\n")
    step_hisat = "date >> B_{name}.log;hisat2 -x /local/db/human/genome -1 {output1} -2 {output2} --un-gz {unparid_unmap} --un-conc-gz {parid_unmap} -S {sam} --summary-file {summary} --threads 16 >> B_{name}.log;date >> B_{name}.log"
    unparid_unmap = "../02.hisat/"+list1[0]+".unpaired.unmap.gz"
    parid_unmap = "../02.hisat/"+list1[0]+".pairs.unmap.gz"
    sam = "../02.hisat/"+list1[0]+".map.sam"
    summary = "../02.hisat/"+list1[0]+".summary.txt"
    file2.write(step_hisat.format_map(vars())+"\n")
    step_kraken = "date >> time ; /bio/kraken2/kraken2 --threads 32 --db /local/db/kraken/ --threads 60 --output {stat} --unclassified-out {unclass} --report {report} 02.hisat/{name}.pairs.unmap.1.gz --paired 02.hisat/{name}.pairs.unmap.2.gz;date >> time ;sleep 1m"
    stat = "03.kraken/"+name+".stat"
    unclass = "03.kraken/"+name+".unclassified#.fastq"
    report = "03.kraken/"+name+".report"
    file3.write(step_kraken.format_map(vars())+"\n")
    step_braken_g = "/bio/Bracken/bracken -d /local/db/kraken/ -i {report} -o 03.kraken/{name}_g.braken -w 03.kraken/{name}_g.report -r 150 -l G"
    step_braken_s = "/bio/Bracken/bracken -d /local/db/kraken/ -i {report} -o 03.kraken/{name}_s.braken -w 03.kraken/{name}_s.report -r 150 -l S"
    file4.write(step_braken_g.format_map(vars())+"\n")
    file4.write(step_braken_s.format_map(vars())+"\n")
