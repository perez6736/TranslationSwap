
"""
with open(full_path + file1Name, encoding='utf-8') as tsvfile:
    readTSV = csv.reader(tsvfile, delimiter='\t')
    for row in readTSV:
        ## we can see all the Korean in the file by printing row[index]
        ## print(row[2])
        ## we need to define the korean in the row 
        file1Kr = row[2]
        file1Eng = row[1]
        ## print (file1Kr)

        ## if file1Kr has a match in the file2Kr
        ## we want to replace index 1 in file1 with the value of index 1 in file2 
        with open(full_path + file2Name, encoding='utf-8') as tsvfile2:
            readTSV2 = csv.reader(tsvfile2, delimiter='\t')
            for row2 in readTSV2:
                print (row2[2])
""" 


"""
reversed the loop 

for row in readerFile1:
    for key in Japanese2KoreanDict.keys():
        print ('This is the key: ' + key)
        print ('This is the row: ' + row[2])
        if key == row[2]:
            print ("we got a match")
            print(key + " and " + row[2])
            print() 
        else:
            print("go to next row")
            print(key + " and " + row[2])
            print() 
""" 