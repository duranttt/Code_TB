#!/usr/bin/python
import sys
import re
file1= open(sys.argv[1],"r")
file2 = open(sys.argv[2],"w")
for line in file1:
    need_str = line.split("\t")[5]
    list_map = re.findall(r"\d+M+",need_str)
    if len(list_map) > 1:
        list_value = []
        for value in list_map:
            list_value.append(int(value[0:-1]))
        map_number = max(list_value)
    elif len(list_map) == 1:
        map_number = int(list_map[0][0:-1])
    else:
        continue
    if map_number >= 60:
        file2.write(line)

