#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    load = line.strip("\n")
    name = line.strip("\n").split("/")[-1]
    step_blast = "nohup blastn -query {load} -db /local/db/{database} -out {out}/{name}.blast -num_threads 16 -outfmt '6 qseqid qlen sseqid slen qstart qend sstart send evalue pident nident mismatch bitscore qcovs stitle' -num_alignments 1 -max_hsps 1 &\n"
    database = sys.argv[3]
    out = sys.argv[4]
    file2.write(step_blast.format_map(vars()))
