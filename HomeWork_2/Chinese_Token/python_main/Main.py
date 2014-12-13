import sys
import math
from subprocess import call
call(["del_datfiles.bat"]) 
# Open this file.
f = open(".\READMEc.txt", "r")
count = 0;
CNT_len = 0;
file_name="";
# Loop over each line in the file.
for line in f.readlines():
    count +=1;
    #file_name='%010d' %(count)+".dat";
    file_name= ".\SplitedFiles" + '\%d' %(count)+".cj_";
    file = open(file_name, 'w');
    file.writelines(line) # Write a sequence of strings to a file
    file.close();
    print "Write File %s Done" %(file_name);

f.close();
print "count = %010d, CNT_len=%d" %(count, CNT_len)
print "Step-1 : Initial Files"
call(["mv_datfiles.bat"]) # move split files form .\SplitedFiles to ..\CKIPClient\test\in
print "Step-2 : Run CKIPClient.exe"
call(["token.bat"]) 	  # run CKIPClient.exe as test.bat
print "Step-3 : Move the output of CKIPClient.exe"
call(["get_token_out.bat"]) # move ..\CKIPClient\test\in .\token_out and ..\CountWordFreq\in
print "Step-4 : Run CountWordFreq.exe with all token files"
for i in range(1, count+1, 1):
  call(["cal_freq.bat", str(i)])
print "Step-5 : Move the output of CountWordFreq.exe"
call(["get_freq_out.bat"]) 
print "Step-6 : To summary output of CountWoreFreq"
call(["cal_freq_summary.bat"]) 