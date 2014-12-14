import sys
import math
import os
import re

threshold = 0;
items = open("./Final_summary_freq_Before_Post_IDF_wKey.txt", "r")
terms = len(items.readlines())
items.close()
file_name=""
count=0
output_file3 = open("./words_weight.txt", 'r')
weights_line = output_file3.readline()
#for line in output_file3.readlines():
weights_line = weights_line.split(",")
output_file3.close()
result = []
for dirPath, dirNames, fileNames in os.walk("./Before_Post_IDF_Individual_freq_wKey"):
    for f in fileNames:
        file_name=os.path.join(dirPath, f)
        count+=1
        data_list = []
        file_read = open(file_name, 'r')
        lines = len(file_read.readlines())
        file_read.close()
        total_weight = 0.0
        for i in range(0,lines):
            data_list.append(i+1)
            data_list[i]=0
        #print count, len(data_list)
        file_read = open(file_name, 'r')
        for line in file_read.readlines():
            #print line
            read_a_line=re.match('(.*)[ \t](.*)[ \t](.*)[ \r]',line)
            #print read_a_line.group(3)
            #try:
            word = int(read_a_line.group(1))
            if word <= terms:
                total_weight+=float(weights_line[word])
            #except ValueError:
            #    print('???')
        file_read.close()
        print count, total_weight
        result+=str(count)
        result+=','
        result+=str(total_weight)
        result+='\n'
        if count > 153:
            break
output_file1 = open("./old_weight.csv", 'w')
output_file1.writelines(result)
output_file1.close()
