# PyBank Script 

# Bring in Financial Data Set - budget_data.csv

import os 
import csv
budget_file = "budget_data.csv"

# Create a Python script that analyzes the records to calculate each of the following:
def average (numbers):
    total = 0.0
    for number in numbers:
        total += number
    find_average = total/len(numbers)
    return find_average

months = []
total_PL = []
monthly_profit_change = [] 
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        months.append(row[0])
        total_PL.append(row[1])
        monthly_profit_change.append(int(row[1]))
    month_count = len(months)
    print(f'Total Months: {month_count}')
    value_total = 0
    for values in total_PL:
        value_total += int(values)
    print(f'Total: ${value_total}')
    net_change = [j-i for i,j in zip(monthly_profit_change[:-1], monthly_profit_change[1:])]
    print(f'Average Change: ${round(average(net_change),2)}')
    net_change.sort(reverse=True)
    print(f'The greatest increase in profits: ${net_change[0]}')
    print(f'The greatest decrease in profits: ${net_change[len(net_change)-1]}')
output = 'Financial Analysis.txt'
with open(output, 'w', newline ='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["------------------------------------------------------"])
    csvwriter.writerow([f'Total Months: {month_count}'])
    csvwriter.writerow([f'Total: ${value_total}'])
    csvwriter.writerow([f'Average Change: ${round(average(net_change),2)}'])
    csvwriter.writerow([f'The greatest increase in profits: ${net_change[0]}'])
    csvwriter.writerow([f'The greatest decrease in profits: ${net_change[len(net_change)-1]}'])
