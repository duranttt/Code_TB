# Code_TB
Using a pathogenic microorganism DNA capture-based NGS technique for pathogenic microorganism DNA enrichment sequencing, followed by machine learning to establish pathogenic microorganism diagnostic thresholds that leaded to a pathogenic microorganism diagnostic model. 

## QC
 >fastp -i {input1} -I {input2} -o {output1} -O {output2} -j {json} -h {html} -w 16

## remove host reads
 >hisat2 -x /local/db/human/genome -1 {output1} -2 {output2} --un-gz {unparid_unmap} --un-conc-gz {parid_unmap} -S {sam} --summary-file {summary} --threads 16

## classification
 >kraken2 --threads 32 --db /local/db/kraken/ --threads 60 --output {stat} --unclassified-out {unclass} --report {report} 02.hisat/{name}.pairs.unmap.1.gz --paired 02.hisat/{name}.pairs.unmap.2.gz

## stat and correct
>bracken -d /local/db/kraken/ -i {report} -o 03.kraken/{name}_g.braken -w 03.kraken/{name}_g.report -r 150 -l G

>bracken -d /local/db/kraken/ -i {report} -o 03.kraken/{name}_s.braken -w 03.kraken/{name}_s.report -r 150 -l S

## blast
>blastn -query ../05.megahit/{sample}/{sample}.contigs.fa -db /mnt/noxa/db/blast_db/nt -out ../05.megahit/{sample}_blast.result -outfmt "6 qseqid qlen sseqid slen qstart qend sstart send evalue pident sstrand bitscore qseq stitle" -num_alignments 1 -max_hsps 1 -num_threads 32

## stat and plot
>Rscript software/pheamap.R result/result_genus_rpm_log_vir.mpa vir.png

>Rscript software/pheamap.R result/result_genus_rpm_log_arc.mpa arc.png

>Rscript software/pheamap.R result/result_genus_rpm_log_bac.mpa bac.png

>Rscript software/pheamap.R result/result_genus_rpm_log_euk.mpa euk.png

>Rscript software/percent_species.R result/result_plot.txt

##DecisionTree
>R - party - ctree

#ROC
>R - pROC - ggplot2 - 


This study was supported by the Natural Science Fund of China (82072328), Capital’s Funds for Health Improvement and Research (CFH2020-4-2163), Beijing Municipal Administration of Hospitals’ Ascent Plan (DFL20181602), Beijing Hospitals Authority Youth Programme (QML20201601), and Tongzhou “Yun He” Talent Project (YHLD2019001 and YHLD2018030).
