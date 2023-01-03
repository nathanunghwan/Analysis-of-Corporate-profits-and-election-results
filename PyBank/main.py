import os
import csv

csv_path =os.path.join("Resources","budget_data.csv")

with open (csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")
    # Header
    csv_header = next(csv_reader)
    # Connvert Dict type
    dic_csv = dict(csv_reader)
    # Extract keys and convert to list ----"Month"
    key_csv = list(dic_csv.keys())
    #print(key_csv) -->['Jan-10',~~, 'Feb-17']
    # Extract values and convert to list(int type) ---"Profit/loss"
    value_csv = list(map(int,dic_csv.values()))
    #print(value_csv) -->[1088983, -354534,~~ , 607208, 382539]
    # Total Profit/Loss
    net_total_amount = sum(value_csv)
    # Total Months
    total_months = len(key_csv)
    # Profit loss monthly change,The first month = 0
    change = [0] + [(value_csv[i] - value_csv[i-1]) for i in range(1,total_months)]
    #print(change)  -->[0, -1443517, ~~, 90895, -224669]
    # Average Change of profit and loss
    avg_change = sum(change)/(len(change)-1)
    # Greatest increase in profit
    max_increase = max(change)
    # Use index to find that month
    date_increase = key_csv[change.index(max_increase)]
    # Greatest decrease in profit
    max_decrease = min(change)
    # Use index to find that month
    date_decrease = key_csv[change.index(max_decrease)]

with open ("analysis/result.txt",'w') as file_csv:
    # What to print out
    contents=['Financial Analysis\n',f"{'-'*30}\n",
              f'Total Month: {total_months}\n',
              f'Total: ${net_total_amount}\n',
              f'Average Change: ${round(avg_change, 2)}\n',
              f'Greatest Increase in Profits: {date_increase} (${max_increase})\n',
              f'Greatest Decrease in Profits: {date_decrease} (${max_decrease})']
    # print on terminal and save to txt file
    for j in range(len(contents)):
        print(contents[j])
        print(contents[j],file=file_csv)
