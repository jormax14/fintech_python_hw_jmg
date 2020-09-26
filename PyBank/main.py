#import dependencies
import pathlib
import csv

#assign csv path
budget_path = f'Resources/budget_data.csv'

#read cvs file
with open(budget_path, 'r') as budget_csv:

    budget_reader = csv.reader(budget_csv, delimiter=",")
    budget_header = next(budget_reader)

#set inital variables and blank lists
    month_count = 0
    total_profit = 0
    month_list = []
    profit_list = []
    
#loop for total variables and populate blank lists
    for row in budget_reader:
        month_count +=1
        total_profit += int(row[1])
        month_list.append(row[0])
        profit_list.append(row[1])
    
#loop through profit_list to solve for monthly_change
    monthly_change = [int(profit_list[i+1]) - int(profit_list[i]) for i in range(len(profit_list)-1)]

#solve for remaining qustions based on previously set variables and lists
    avg_change = round(sum(monthly_change) / (month_count - 1),2)
    
    max_change = max(monthly_change)
    max_change_month = month_list[monthly_change.index(max_change)+1]
    
    min_change = min(monthly_change)
    min_change_month = month_list[monthly_change.index(min_change)+1]

#print results
print(f"Financial Analysis")
print(f"-"*25)
print(f"Total Months: {month_count}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits: {max_change_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_month} (${min_change})")

#output results to text file
with open("main_output.txt","w") as txtfile:
    print(f"Financial Analysis", file=txtfile)
    print(f"-"*25, file=txtfile)
    print(f"Total Months: {month_count}", file=txtfile)
    print(f"Total: ${total_profit}", file=txtfile)
    print(f"Average Change: ${avg_change}", file=txtfile)
    print(f"Greatest Increase in Profits: {max_change_month} (${max_change})", file=txtfile)
    print(f"Greatest Decrease in Profits: {min_change_month} (${min_change})", file=txtfile)