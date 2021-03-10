import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')

votes = 0
total_votes = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        #find total number of votes cast
        votes += 1
        total_votes.append(votes) 
print(f"total votes: {max(total_votes)}")
