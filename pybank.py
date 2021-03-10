#import os and csv
import os
import csv
#csvpath = os.path.join('Resources', 'budget_data.csv')
csvpath = r'Resources\\budget_data.csv'
total_months = 0
monthcounter = []
total_profit = 0
profitsbymonth = []
profitlist = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        # total number of months
        total_months += 1
        monthcounter.append(total_months)
        # net profit/loss
        total_profit += float(row[1])
        profitsbymonth.append(total_profit)
        profit = float(row[1])
        profitlist.append(profit)
        
# print(profitlist)
# print(profitsbymonth)
# print(monthcounter)
print(f"total months: {max(monthcounter)}")
print(f"total profit is: {max(profitsbymonth)}")
print(f"here is my max profit {max(profitlist)}")
print(f"here is my min profit {min(profitlist)}")


    
