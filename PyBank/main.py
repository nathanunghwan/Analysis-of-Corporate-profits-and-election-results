import os
import csv

csv_path =os.path.join("Resources","budget_data.csv")
print(csv_path)
with open (csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")

    csv_header = next(csv_reader)
    #print(f'CSV Header: {csv_header}')
    
    a=dict(csv_reader)
    b=list(a.keys())
    c=list(map(int,a.values()))
    
    net_total_amount = sum(c)
    total_months = len(b)
    change = [0] + [ (c[i] - c[i-1]) for i in range(1,total_months)]
    avg_change=sum(change)/(len(change)-1)
    max_increase=max(change)
    date_increase=b[change.index(max_increase)]
    max_decrease=min(change)
    date_decrease=b[change.index(max_decrease)]

    #print(a)
    #print(b)
    #print(c)
    print(f'Total Month: {total_months}')
    print(f'Total: ${net_total_amount}')
    
    print(f'Average Change: ${round(avg_change,2)}')
    print(f'Greatest Increase in Profits: {date_increase} (${max_increase})')
    print(f'Greatest Decrease in Profits: {date_decrease} (${max_decrease})')


    '''
    a= list(csv_reader)
    prof_loss=list(int(profit[1]) for profit in a)
    fiscal_date = [fiscal[0] for fiscal in a]
    net_total_amount = sum(prof_loss)
    total_months = len(fiscal_date)
    change = [ (prof_loss[i] - prof_loss[i-1]) for i in range(1,total_months)]
    average_change= sum(change)/len(change)
    #print(list(csv_reader))
    print(fiscal_date )
    print(prof_loss)
    print(total_months)
    print(net_total_amount)
    print(average_change)
    '''
    '''
    for i in range(1,len(net_total_amount)):
        a=net_total_amount[i]
        b=net_total_amount[i+1]
        a, b = b, b-a

'''


   
    '''
    sum=0
    count=0
    for row in csv_reader:
        count +=1
        sum += int(row[1])



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
'''






