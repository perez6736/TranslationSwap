import csv
import os

## i would hope you can just swap the name of the files here to customize a bit 
file1Name = '/DannyTestJap.csv' ## this file has the japanese korean and we want to replace the japanese
file2Name = '/DannyTest.csv' ## this file has the english we want to use to replace the japanese. 
full_path = os.getcwd() ## dont hard code directory

file11 = open(full_path + file1Name, encoding='utf-8')
file2 = open(full_path + file2Name, encoding='utf-8')

## read the csv file2
readerFile2 = csv.reader(file2, delimiter='\t')
Japanese2KoreanDict = {}
for row in readerFile2:
    Japanese2KoreanDict[row[2]] = row[1] ## dictionary is created here 

######################################################

## Now we need to loop through file1 (the one we want to replace englsih)
with open(full_path + file1Name,mode='r+', encoding='utf-8', newline='') as file1:
    readerFile1 = csv.reader(file1, delimiter='\t')
    newRows = [] ## this will have the new row 
    for i, row in enumerate(readerFile1):
        print('This is the row we on ')
        print(row)
        print()
        newRows.append(row) ## add the row here 
        print (newRows)
        for key in Japanese2KoreanDict.keys(): ## fix this 
            if key == row[2]:
                print ("we got a match")
                print(key + " and " + row[2])
                print(row[1] + ' turns into ' + Japanese2KoreanDict[key])

                ##todo - fix this line so that it replaces it correctly - nested array 
                newrowsIndex = newRows[i] 
                newrowsIndex[1] = Japanese2KoreanDict[key]
                break ## break out of loop inn keys for that row to go to next row
    print(newRows)

    file1.seek(0)  # seek to the file begining
    file1.truncate()  # truncate the rest of the content
    writer = csv.writer(file1)  # create a CSV writer
    writer.writerows(newRows)  # write our modified rows



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