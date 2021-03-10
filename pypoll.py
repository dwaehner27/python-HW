import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

total_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        #find total number of votes cast
        total_votes += 1
        print(total_votes)  



#list of canidates who recieved votes

#percentage of votes per canidate

#total number of votes each canidate won

#winner of the election

#export text file with results