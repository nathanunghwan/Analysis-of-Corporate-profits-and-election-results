import os
import csv

csv_path =os.path.join("Resources","election_data.csv")

with open (csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Header
    csv_header = next(csv_reader)
    # extract just candidate and make a list
    csv_reader_list=[i[2] for i in csv_reader]
    #print(csv_reader_list)--> ['Diana DeGette',~~ ,'Raymon Anthony Doane']
    # Total vote
    total_vote= len(csv_reader_list)
    # Use set function, collect name of candidates
    candidate = list(set(csv_reader_list))
    #print(candidate) -->['Charles Casper Stockham', 'Raymon Anthony Doane', 'Diana DeGette']
    # Candidate name, rate of vote, numbers of vote
    temp_list= [(candidate[j],
                 round(csv_reader_list.count(candidate[j])*100/total_vote,3),
                 csv_reader_list.count(candidate[j]))
                for j in range(len(candidate))]
    #print(temp_list)--> [('Diana DeGette', 73.812, 272892), ('Charles Casper Stockham', 23.049, 85213), ('Raymon Anthony Doane', 3.139, 11606)]
    # sort by name
    result_list=sorted(temp_list,key=lambda x: x[0])
    #print(result_list) -->[('Charles Casper Stockham', 23.049, 85213), ('Diana DeGette', 73.812, 272892), ('Raymon Anthony Doane', 3.139, 11606)]
    # sort by vote
    winner=sorted(temp_list,key=lambda x : -x[2])[0]
    #print(winner) -->('Diana DeGette', 73.812, 272892)

with open("analysis/result_Poll.txt", 'w') as file_csv:
    # display on terminal
    print('Election Results\n', f"{'-' * 30}\n", f'Total Votes: {total_vote}\n', f"{'-' * 30}\n", sep='\n')
    # save to txt file
    print('Election Results\n', f"{'-' * 30}\n", f'Total Votes: {total_vote}\n', f"{'-' * 30}\n", sep='\n', file=file_csv)
    # results by candidate
    for k in range(len(result_list)):
        print(f'{result_list[k][0]}: {result_list[k][1]}% ({result_list[k][2]})\n')
        print(f'{result_list[k][0]}: {result_list[k][1]}% ({result_list[k][2]})\n', file=file_csv)
    # display on terminal and  save to txt file
    print(f"{'-' * 30}\n", f'Winner: {winner[0]} \n', f"{'-' * 30}", sep='\n')
    print(f"{'-' * 30}\n", f'Winner: {winner[0]} \n', f"{'-' * 30}", sep='\n', file=file_csv)
