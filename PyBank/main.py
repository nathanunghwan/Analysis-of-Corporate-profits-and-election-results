import os
import csv

csv_path =os.path.join("Resources","budget_data.csv")

with open (csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")

    csv_header = next(csv_reader)
    #print(f'CSV Header: {csv_header}')
    
    dic_csv = dict(csv_reader)
    key_csv = list(dic_csv.keys())
    value_csv = list(map(int,dic_csv.values()))
    
    net_total_amount = sum(value_csv)
    total_months = len(key_csv)
    change = [0] + [ (value_csv[i] - value_csv[i-1]) for i in range(1,total_months)]
    avg_change = sum(change)/(len(change)-1)
    max_increase = max(change)
    date_increase = key_csv[change.index(max_increase)]
    max_decrease = min(change)
    date_decrease = key_csv[change.index(max_decrease)]

with open ("result.txt",'w') as file_csv:
    contents=['Financial Analysis\n','-'*30,
              f'\nTotal Month: {total_months}',
              f'\nTotal: ${net_total_amount}',
              f'\nAverage Change: ${round(avg_change, 2)}',
              f'\nGreatest Increase in Profits: {date_increase} (${max_increase})',
              f'\nGreatest Decrease in Profits: {date_decrease} (${max_decrease})']

    for j in range(len(contents)):
        print(contents[j])
        print(contents[j],file=file_csv)





