
# 项目简介
* Using a pathogenic microorganism DNA capture-based NGS technique for pathogenic microorganism DNA enrichment sequencing, followed by machine learning to establish pathogenic microorganism diagnostic thresholds that leaded to a pathogenic microorganism diagnostic model. 

# Code_TB代码说明
* 利用hisat2去除每个样本的宿主序列，提取unmapped reads，进行kraken2分类以及braken矫正。

* 将临床数据的判定结果用0和1表示阴性和阳性，输入因素为Total、Mycobacterium、 Complex、 Complex_RPM、Ratio，利用R语言的party包绘制决策树并选择显著性因素Ratio（P值小于0.005）作为分类标准，pROC包绘制ROC曲线并计算AUC值，然后根据做种阈值预测每个队列的结果，用预测结果和临床结果质控PR曲线。









This study was supported by the Natural Science Fund of China (82072328), Capital’s Funds for Health Improvement and Research (CFH2020-4-2163), Beijing Municipal Administration of Hospitals’ Ascent Plan (DFL20181602), Beijing Hospitals Authority Youth Programme (QML20201601), and Tongzhou “Yun He” Talent Project (YHLD2019001 and YHLD2018030).

