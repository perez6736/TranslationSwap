import csv
import os

fileName = 'DannyTest.csv'

full_path = os.path.expanduser('D:/Desktop/TranslationSwap/')
print (full_path)

with open(full_path + fileName, encoding='utf-8') as tsvfile:
    readCSV = csv.reader(tsvfile, delimiter='\t')
    for row in readCSV:
        print(row[1])
