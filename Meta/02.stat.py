#!/usr/bin/python
import sys
file1 = open(sys.argv[1],"r")
value = sys.argv[2]
for line1 in file1:
    if line1.strip("\n").split("\t")[-1] == "Y":
        continue
    else:
        sample = line1.split("\t")[0]
        file_out = open("step2/"+sample+".sh","w")
#        file_out.write("#python /mnt/software/mata/se_virus_id.py ../03.kraken/"+sample+".report ../03.kraken/"+sample+".list\n")
#        file_out.write("/mnt/software/mata/se_seqid.py ../03.kraken/"+sample+".stat ../03.kraken/"+sample+"_virus_taxid.list ../03.kraken/"+sample+".txt\n")
#        file_out.write("sed \"s/$/\/1/\" ../03.kraken/"+sample+".txt > ../03.kraken/"+sample+"_virus_1.txt\n")
#        file_out.write("sed \"s/$/\/2/\" ../03.kraken/"+sample+".txt > ../03.kraken/"+sample+"_virus_2.txt\n")
#        file_out.write("/mnt/software/seqtk/seqtk seq -a ../02.hisat/"+sample+".pairs.unmap.1.gz > ../02.hisat/"+sample+".unmap.paris.1.fa ; /mnt/software/seqtk/seqtk seq -a ../02.hisat/"+sample+".pairs.unmap.2.gz > ../02.hisat/"+sample+".unmap.paris.2.fa\n")
#        if value == "BGI":
#            file_out.write("mv ../02.hisat/"+sample+".unmap.paris.1.fa ../02.hisat/"+sample+".unmap.paris.1.fasta\n")
#            file_out.write("mv ../02.hisat/"+sample+".unmap.paris.2.fa ../02.hisat/"+sample+".unmap.paris.2.fasta\n")
#        else:
#            file_out.write("python /mnt/software/script/reads_id_change.py ../02.hisat/"+sample+".unmap.paris.1.fa 1 ../02.hisat/"+sample+".unmap.paris.1.fasta\n")
#            file_out.write("rm ../02.hisat/"+sample+".unmap.paris.1.fa\n")
#            file_out.write("python /mnt/software/script/reads_id_change.py ../02.hisat/"+sample+".unmap.paris.2.fa 2 ../02.hisat/"+sample+".unmap.paris.2.fasta\n")
#            file_out.write("rm ../02.hisat/"+sample+".unmap.paris.2.fa\n")
#        file_out.write("/mnt/software/seqtk/seqtk subseq ../02.hisat/"+sample+".unmap.paris.1.fasta ../03.kraken/"+sample+"_virus_1.txt > ../05.megahit/"+sample+"_virus.1.fa;/mnt/software/seqtk/seqtk subseq ../02.hisat/"+sample+".unmap.paris.2.fasta ../03.kraken/"+sample+"_virus_2.txt > ../05.megahit/"+sample+"_virus.2.fa\n")
        file_out.write("cat ../L0*/05.megahit/"+sample+"_virus.1.fa > ../05.megahit/"+sample+"_virus.1.fa\n")
        file_out.write("cat ../L0*/05.megahit/"+sample+"_virus.2.fa > ../05.megahit/"+sample+"_virus.2.fa\n")
        file_out.write("/mnt/software/megahit/megahit/bin/megahit -1 ../05.megahit/"+sample+"_virus.1.fa -2 ../05.megahit/"+sample+"_virus.1.fa -o ../05.megahit/"+sample+"\n")
        file_out.write("mv ../05.megahit/"+sample+"/final.contigs.fa ../05.megahit/"+sample+"/"+sample+".contigs.fa\n")
        file_out.write("head -5 ../05.megahit/"+sample+"/log |tail -1 > ../05.megahit/"+sample+".log\ntail -2 ../05.megahit/"+sample+"/log | head -1 >> ../05.megahit/"+sample+".log\n")
        file_out.write("export BLASTDB=\"/mnt/noxa/db/blast_db/\" && /mnt/software/ncbi-blast-2.10.1+/bin/blastn -query ../05.megahit/"+sample+"/"+sample+".contigs.fa -db /mnt/noxa/db/blast_db/nt -out ../05.megahit/"+sample+"_blast.result -outfmt \"6 qseqid qlen sseqid slen qstart qend sstart send evalue pident sstrand bitscore qseq stitle\" -num_alignments 1 -max_hsps 1 -num_threads 32\n")
