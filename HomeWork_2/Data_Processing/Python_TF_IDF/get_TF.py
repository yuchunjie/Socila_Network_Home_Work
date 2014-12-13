import sys
import math
import os
import re

count = 0;
file_name="";

items = open("./Final_summary_freq_Before_Post_IDF_wKey.txt", "r")
lines = len(items.readlines())
items.close()
output_file1 = open("./term_times_all.txt", 'w')
output_file2 = open("./tf.txt", 'w')
for dirPath, dirNames, fileNames in os.walk("./Before_Post_IDF_Individual_freq_wKey"):
    for f in fileNames:
        file_name=os.path.join(dirPath, f)
        file_read = open(file_name, 'r')
        count+=1
        data_list = []
        total_count = 1
        for i in range(0,lines):
            data_list.append(i+1)
            data_list[i]=0
        #print count, len(data_list)
        for line in file_read.readlines():
            #print line
            read_a_line=re.match('(.*)[ \t](.*)[ \t](.*)[ \r]',line)
            #print read_a_line.group(3)
            try:
                if int(read_a_line.group(1)) < lines:
                    data_list[int(read_a_line.group(1))-1] = read_a_line.group(3)
                    total_count+=int(read_a_line.group(3))
            except ValueError:
                print('???')
        one_line1 = []
        one_line2 = []
        for i in range(0,lines):
            one_line1+=str(data_list[i])
            one_line1+=','
            #if total_count < 2:
            #    print total_count
            tf=0.001
            tf=float(data_list[i])/total_count
            #if tf > 0:
            #    print tf
            one_line2+=str(tf)
            one_line2+=','
        one_line1+='\n'
        one_line2+='\n'
        output_file1.writelines(one_line1)
        output_file2.writelines(one_line2)
        file_read.close()
output_file1.close()
output_file2.close()
