import pandas
from numpy import random
import sys,os

df = pandas.read_csv(sys.argv[1],sep="\t")

all_list = [i for i in range(len(df))]
random.shuffle(all_list)
print(all_list)

#生成随机列表
dict_list = {}
for i in range(10):
    #print(int(i/10 * len(df) ))
    #print(int((i+1)/10 * len(df)))
    dict_list[i] = all_list[ int(i/10 * len(df) ) : int((i+1)/10 * len(df)) ]
    #print(dict_list[i])

#生成训练和测试集
print(dict_list)
for i in range(10):
    test_list = dict_list[i]
    train_list = [i for i in all_list if i not in test_list]

    df_train = df.loc[train_list]
    df_test = df.loc[test_list]

    os.system("mkdir -p " + str(i))
    df_train.to_csv( str(i) + "/train.db." + sys.argv[2] + ".xls", sep="\t", index=0)
    df_test.to_csv( str(i) + "/test.db." + sys.argv[2] + ".xls", sep="\t", index=0)

