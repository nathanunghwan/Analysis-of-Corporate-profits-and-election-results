import os
import csv

csv_path =os.path.join("Resources","election_data.csv")

with open (csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_reader)
    print(f'CSV Header: {csv_header}')
    a = dict((i[0] , i[2]) for i in csv_reader)
    b= [ (v, k) for k,v in a.items()]
    c= list(dict(b))
    print(c)