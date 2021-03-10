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
    # csvwriter = csv.writer(csvfile, delimiter=',')
    # for row in csvreader:
    #     csvwriter.writerows()

    






# * The average of the changes in "Profit/Losses" over the entire period


#greatest increase in profits date and amount over the entire period
    #need to write new column for change
    #loop to find greatest value


#greatest decrease in profits date and amount over the entire period
    #use column for change and loop to find smallest value

#print total months, total profit/loss, average change, greatest increase and greatest decrease