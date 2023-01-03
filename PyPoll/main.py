import os
import csv

csv_path =os.path.join("Resources","election_data.csv")

with open (csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Header
    csv_header = next(csv_reader)

    # extract just candidate and make a list
    candidate=[i[2] for i in csv_reader]
    #print(candidate)--> ['Diana DeGette',~~ ,'Raymon Anthony Doane']
    # Total vote
    total_vote= len(candidate)
    # Use set function, collect name of candidates
    name = list(set(candidate))
    #print(name) -->['Charles Casper Stockham', 'Raymon Anthony Doane', 'Diana DeGette']
    # Candidate name, rate of vote, numbers of vote
    result= [(name[j],
                 round(candidate.count(name[j])*100/total_vote,3),
                 candidate.count(name[j]))
                for j in range(len(name))]
    #print(result)--> [('Diana DeGette', 73.812, 272892), ('Charles Casper Stockham', 23.049, 85213), ('Raymon Anthony Doane', 3.139, 11606)]
    # sort by name
    sort_by_name=sorted(result,key=lambda x: x[0])
    #print(sort_by_name) -->[('Charles Casper Stockham', 23.049, 85213), ('Diana DeGette', 73.812, 272892), ('Raymon Anthony Doane', 3.139, 11606)]
    # sort by vote
    winner=sorted(result,key=lambda x : -x[2])[0]
    #print(winner) -->('Diana DeGette', 73.812, 272892)

with open("analysis/result_Poll.txt", 'w') as file_csv:
    # display on terminal
    print('Election Results\n', f"{'-' * 30}\n", f'Total Votes: {total_vote}\n', f"{'-' * 30}\n", sep='\n')
    # save to txt file
    print('Election Results\n', f"{'-' * 30}\n", f'Total Votes: {total_vote}\n', f"{'-' * 30}\n", sep='\n', file=file_csv)
    # results by candidate
    for k in range(len(sort_by_name)):
        print(f'{sort_by_name[k][0]}: {sort_by_name[k][1]}% ({sort_by_name[k][2]})\n')
        print(f'{sort_by_name[k][0]}: {sort_by_name[k][1]}% ({sort_by_name[k][2]})\n', file=file_csv)
    # display on terminal and  save to txt file
    print(f"{'-' * 30}\n", f'Winner: {winner[0]} \n', f"{'-' * 30}", sep='\n')
    print(f"{'-' * 30}\n", f'Winner: {winner[0]} \n', f"{'-' * 30}", sep='\n', file=file_csv)
