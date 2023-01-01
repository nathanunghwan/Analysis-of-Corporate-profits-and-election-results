import os
import csv

csv_path =os.path.join("Resources","election_data.csv")

with open (csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_reader)
    print(f'CSV Header: {csv_header}')
    csv_reader_list=[i[2] for i in csv_reader]
    total_vote= len(csv_reader_list)
    candidate = list(set(csv_reader_list))
    temp_list= [(candidate[j],round(csv_reader_list.count(candidate[j])*100/total_vote,3),csv_reader_list.count(candidate[j]))
                  for j in range(len(candidate))]

    result_list=sorted(temp_list,key=lambda x: x[0])
    winner=sorted(temp_list,key=lambda x : -x[2])[0]



with open("analysis/result_Poll.txt", 'w') as file_csv:

    print('Election Results\n', f"{'-' * 30}\n", f'Total Votes: {total_vote}\n', f"{'-' * 30}\n", sep='\n')
    print('Election Results\n', f"{'-' * 30}\n", f'Total Votes: {total_vote}\n', f"{'-' * 30}\n", sep='\n', file=file_csv)
    for k in range(len(result_list)):
        print(f'{result_list[k][0]}: {result_list[k][1]}% ({result_list[k][2]})\n')
        print(f'{result_list[k][0]}: {result_list[k][1]}% ({result_list[k][2]})\n', file=file_csv)
    print(f"{'-' * 30}\n", f'Winner: {winner[0]} \n', f"{'-' * 30}", sep='\n')
    print(f"{'-' * 30}\n", f'Winner: {winner[0]} \n', f"{'-' * 30}", sep='\n', file=file_csv)
