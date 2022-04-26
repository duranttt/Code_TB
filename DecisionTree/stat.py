print("队列\t十折\t第1因素\t第1阈值\t第1P值\t第2因素\t第2阈值\t第2P值\t第3因素\t第3阈值\t第3P值")
def take_P(file,group,batch):
    list_print = [group,str(batch)]
    mark = ""
    for line in open(file):
        if "<=" in line:
            i = line.strip().split(" ")
            factor_name = i[1]
            factor_value = i[3].strip(";")
            factor_criterion = i[6].strip(",")
            if factor_criterion == "1":
                factor_P = "0.001"
            else:
                factor_P = str(round(1-float(factor_criterion),3))
            list_print.extend([factor_name, factor_value, factor_P])
        if "tree with 2 terminal nodes" in line:
            mark = "2"
        if "tree with 3 terminal nodes" in line:
            mark = "3"
    if mark == "2":
        list_print.extend(["-", "-", "-","-", "-", "-"])
    if mark == "3":
        list_print.extend(["-", "-", "-"])
    print("\t".join(list_print))

for group in ["Plasma_A_I", "TotalS_A_I", "CSF_A_I", "TotalS_Sum", "CSF_Sum", "Plasma_Sum"]:
    for batch in range(10):
        file_stat = "~/Decision_Tree/TB/queue4/" + group + "/" + str(batch) + "/train.db." + group + ".matrix.xls" 
        take_P(file_stat,group,batch)

