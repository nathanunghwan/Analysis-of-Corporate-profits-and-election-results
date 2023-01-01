import os
import csv

csv_path = os.path.join("Resources","election_data.csv")
print(csv_path)
with open(csv_path,encoding='utf-8') as csv_file:
    csv_reader= csv.reader(csv_file, delimiter=',')
    print(csv_reader)