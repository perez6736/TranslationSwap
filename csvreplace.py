import csv
import os

print ("working...")
## i would hope you can just swap the name of the files here to customize a bit 
file1Name = '/DannyTestJap.csv' ## this file has the japanese korean and we want to replace the japanese
file2Name = '/DannyTest.csv' ## this file has the english we want to use to replace the japanese. 
full_path = os.getcwd() ## dont hard code directory

## file11 = open(full_path + file1Name, encoding='utf-8')
file2 = open(full_path + file2Name, encoding='utf-8')

## read the csv file2
readerFile2 = csv.reader(file2, delimiter='\t')
Japanese2KoreanDict = {}
for row in readerFile2:
    if len(row) > 1:
        Japanese2KoreanDict[row[2]] = row[1] ## dictionary is created here 
print ("dictionary created. ")

######################################################
print ("translating. please wait. ")
## Now we need to loop through file1 (the one we want to replace englsih)
with open(full_path + file1Name,mode='r+', encoding='utf-8', newline='') as file1:
    readerFile1 = csv.reader(file1, delimiter='\t')
    newRows = [] ## this will have the new row 
    for i, row in enumerate(readerFile1):
        newRows.append(row) ## add the row here 
        if len(row) >=3:
            print (len(row))
            for key in Japanese2KoreanDict.keys():
                if key == row[2]: ## some file dont have a index 2 in the row.... need to skip those 
                    newrowsIndex = newRows[i] 
                    newrowsIndex[1] = Japanese2KoreanDict[key]
                    break ## break out of loop inn keys for that row to go to next row

    file1.seek(0)  # seek to the file begining
    file1.truncate()  # truncate the rest of the content
    writer = csv.writer(file1, delimiter='\t')  # create a CSV writer
    writer.writerows(newRows)  # write our modified rows
    print (i)
    print ("finished.")

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