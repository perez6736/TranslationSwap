import csv
import os

## i would hope you can just swap the name of the files here to customize a bit 
file1Name = 'DannyTest.csv'
file2Name = 'DannyTestJap.csv'
full_path = os.path.expanduser('D:/Desktop/TranslationSwap/')

file1 = open(full_path + file1Name, encoding='utf-8')
file2 = open(full_path + file2Name, encoding='utf-8')


## open file 1 the actual game file 
## loop thorugh each row holding the value for the 1 and 2 index (1 is english and 2 is korean)
## open file 2 
## loop through the rows checking the korean value 
## if korean value equals file1 korean value 
## ## file1 index1 = file2 index1
## ## if no match go to next row 
## repeat above until no more rows in file 1  

## second approach 
## loop through rows in file 2 (korean japanese pair file)
## make a dictionary of korean and japanese pair? 
## loop through the first file and see if the korean their mataches a value of the dictionary 
## swap the english with the japanese pair ffrom the dict 