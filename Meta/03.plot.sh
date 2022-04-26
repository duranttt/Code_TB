python3 software/se_class.py result/result_kindom.mpa result/result_genus.mpa g
python3 software/krone_out.py result/result_kindom.mpa result/result_rm.mpa
#python3 software/se_virus_report.py sample result/result_rm.mpa
ls *txt > list.txt
cat list.txt |tr "\n" " " > krona.sh
sed -i "s#^#/usr/local/bin/ktImportText #" krona.sh
bash krona.sh
rm *txt
python3 software/rpm.py result/result_rm.mpa result/result_rpm.mpa
python3 software/back_kindom.py result/result_rpm.mpa result/result_rpm_kin.mpa
python3 software/se_class.py result/result_rpm_kin.mpa result/result_genus_rpm.mpa g
#python software/log.py result/result_rpm.mpa result/result_rpm_log.mpa
python3 software/log.py result/result_genus_rpm.mpa result/result_genus_rpm_log.mpa
python3 software/split_kindom.py result/result_rpm.mpa
python3 software/split_kindom_genus.py result/result_genus_rpm_log.mpa
python3 software/change_data_R.py result/result_rpm_vir.mpa result/result_rpm_arc.mpa result/result_rpm_bac.mpa result/result_rpm_euk.mpa result/result_plot.txt
python3 software/change_data_R.py result/result_genus_rpm_log_vir.mpa result/result_genus_rpm_log_arc.mpa result/result_genus_rpm_log_bac.mpa result/result_genus_rpm_log_euk.mpa result/result_genus_plot.txt
Rscript software/pheamap.R result/result_genus_rpm_log_vir.mpa vir.png
Rscript software/pheamap.R result/result_genus_rpm_log_arc.mpa arc.png
Rscript software/pheamap.R result/result_genus_rpm_log_bac.mpa bac.png
Rscript software/pheamap.R result/result_genus_rpm_log_euk.mpa euk.png
Rscript software/percent_species.R result/result_plot.txt
