import sys
import math
import os
import re

count = 0;
#CNT_len = 0;
one_line1 = []

items = open("./Final_summary_freq_Before_Post_IDF_wKey.txt", "r")
terms = len(items.readlines())
items.close()
#output_file1 = open("./tf-idf.txt", 'w')
output_file1 = open("./term_times_all.txt", 'r')
lines = len(output_file1.readlines())
for line in output_file1.readlines():
    print line
output_file1.close()
print lines
print terms
output_file2 = open("./IDF.txt", 'w')
count=0
check_line = []
for i in range(0,terms):
    count=0
    check_line = []
    output_file1 = open("./term_times_all.txt", 'r')
    for line in output_file1.readlines():
        check_line = line.split(",")
        have_value=int(check_line[i])
        #print i, check_line[i]
        if have_value > 0:
            count+=1
    output_file1.close()
    idf=float(lines)/float(1+count)
    idf=math.log(idf)
    print i, idf
    one_line1+=str(idf)
    one_line1+=','
output_file2.writelines(one_line1)
output_file2.close()
