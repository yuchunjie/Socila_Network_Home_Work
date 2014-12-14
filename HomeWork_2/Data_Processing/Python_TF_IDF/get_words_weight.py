import sys
import math
import os
import re

threshold = 0;
#CNT_len = 0;
#one_line1 = []
items = open("./Final_summary_freq_Before_Post_IDF_wKey.txt", "r")
terms = len(items.readlines())
items.close()
file_name=""
weight = []
output_file2 = open("./IDF.txt", 'r')
for line in output_file2.readlines():
    check_idf_line = line.split(",")
output_file2.close()
for i in range(0, terms):
    word_weight = 0
    for j in range(0, 154):
        threshold=j+1
        file_name="./TF-IDF/" + str(threshold) + "_tf-idf" + ".csv"
        output_file1 = open(file_name, 'r')   
        for line in output_file1.readlines():
            check_line = line.split(",")
        output_file1.close()
        try:
            word_weight+=float(check_line[i+1])*float(check_idf_line[i+1])
        except ValueError:
            print('???')
    word_weight=float(word_weight)/float(154)
    print i+1, word_weight
    weight+=str(word_weight)
    weight+=','
output_file3 = open("./words_weight.txt", 'w')
output_file3.writelines(weight)
output_file3.close()
