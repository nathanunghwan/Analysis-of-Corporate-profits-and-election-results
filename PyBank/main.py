import os
import csv

csv_path =os.path.join("Resources","budget_data.csv")
print(csv_path)
with open (csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")

    csv_header = next(csv_reader)
    print(f'CSV Header: {csv_header}')
    print(type(csv_reader))
    #a=dict(csv_reader)
    #b=list(dict(csv_reader).keys())
    #c=list(map(int,a.values()))
    #print(a)
    #prof_loss=list(int(profit[1]) for profit in csv_reader)
    #fiscal_date = list(fiscal[0] for fiscal in csv_reader)
    sum=0
    count=0
    for row in csv_reader:
        count +=1


    #print(b)

    print(c)
    print(sum(c))
    print(len(c))
    print(max(c))
    #print(sum(a.values()))
    Total_Months =0
    Total = 0

    for row in (csv_reader):
        Total += int(row[1])
        Total_Months +=1

        #avg=row[1]
    print(Total_Months)
    print(Total)







