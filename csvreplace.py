cloneimport csv
import os

full_path = os.path.expanduser('D:\Desktop/ramons thing/English/')
print (full_path)

with open(full_path + "UI.tsv", encoding='utf-8') as tsvfile:
    readCSV = csv.reader(tsvfile, delimiter='\t')
    for row in readCSV:
        print(row[1])
