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
if not os.path.exists("./TF-IDF"):
    os.makedirs("./TF-IDF")
#for i in range(0, 154):
one_line = []
tf_idf = []
output_file1 = open("./tf.txt", 'r')
for tf_line in output_file1.readlines():
    threshold+=1
    check_tf_line = tf_line.split(",")
    output_file2 = open("./IDF.txt", 'r')
    idf_line = output_file2.readline()
    output_file2.close()
    check_idf_line = idf_line.split(",")
    for j in range(0, terms):
        tf_idf.append(j+1)
        tf_idf[j] = float(check_tf_line[j]) * float(check_idf_line[j]) 
        one_line+=str(tf_idf[j])
        one_line+=','
    file_name="./TF-IDF/" + str(threshold) + "_tf-idf" + ".csv"
    output_file3 = open(file_name, 'w')   
    output_file3.writelines(one_line)
    one_line = []
    print threshold
    if threshold > 153:
        break
output_file1.close()
