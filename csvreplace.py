import csv
import os

## i would hope you can just swap the name of the files here to customize a bit 
file1Name = 'DannyTest.csv' ## this file has the english we want to replace 
file2Name = 'DannyTestJap.csv' ## this file has the Japanese we want to save 
full_path = os.path.expanduser('D:/Desktop/TranslationSwap/')

file1 = open(full_path + file1Name, encoding='utf-8')
file2 = open(full_path + file2Name, encoding='utf-8')


## read the csv file2
readerFile2 = csv.reader(file2, delimiter='\t')
Japanese2KoreanDict = {}
for row in readerFile2:
    Japanese2KoreanDict[row[2]] = row[1] ## dictionary is created here 
"""    
{
    'KeyKorean1': 'jap1', 
    'KeyKorean4': 'jap4', 
    'KeyKorean2': 'jap2', 
    'KeyKorean10': 'jap10', 
    'KeyKorean6': 'jap6', 
    'KeyKorean3': 'jap3', 
    'KeyKorean100': 'jap100'
}
"""
## Now we need to loop through file1 (the one we want to replace englsih)
readerFile1 = csv.reader(file1, delimiter='\t')
for row in readerFile1:
    print('This is the row we on ')
    print(row)
    print()
    for key in Japanese2KoreanDict.keys():
        if key == row[2]:
            print ("we got a match")
            print(key + " and " + row[2])
            print(row[1] + ' turns into ' + Japanese2KoreanDict[key])
            break ## break out of loop inn keys for that row to go to next row
            ## row[1] = Japanese2KoreanDict[key]







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