# PyPoll Script

# Bring in Poll Data Set 
# 3 columns: Voter ID, County, Candidate
import os
import csv 

election_file ='election_data.csv'

candidates = []

# Open csv 
with open(election_file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvfile)
    for row in csv_reader: 
        if row[2] not in candidates:
            candidates.append(row[2])
    print(f'Candidate List: {candidates}')

with open(election_file) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvfile)
    khan= 0
    correy= 0
    li=0
    otooley=0
    for row in csv_reader:
       if row[2] == "Khan":
            khan += 1
       elif row[2] == "Correy":
            correy += 1
       elif row[2] == "Li":
            li += 1
       elif row[2] == "O'Tooley":
            otooley += 1
vote_total = khan + correy + li + otooley

#print(vote_total)
        
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_total}")
print("-------------------------")
print(f'Khan: {round((khan/vote_total)*100,2)}% ({khan})')
print(f'Correy: {round((correy/vote_total)*100,2)}% ({correy})')
print(f'Li: {round((li/vote_total)*100,2)}% ({li})')
print(f"O'Tooley: {round((otooley/vote_total)*100,2)}% ({otooley})")
print("-------------------------")
if khan > correy and khan > li and khan > otooley:
    winner = "Khan"
elif correy > khan and correy > li and correy > otooley:
    winner = "Correy"
elif li > khan and li > correy and li > otooley:
    winner = "Li"
elif otooley >= khan and otooley >= li and otooley >= correy:
    winner = "O'Tooley"
print(f'Winner: {winner}')
print("-----------------------------------------------------------------------")

# save summary to txt
output = 'ElectionResults.txt'
with open(output, 'w', newline ='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-----------------------------------------------------------------------"])
    csvwriter.writerow([f"Total Votes: {vote_total}"])
    csvwriter.writerow(["-----------------------------------------------------------------------"])
    csvwriter.writerow([f'Khan: {round((khan/vote_total)*100,2)}% ({khan})'])
    csvwriter.writerow([f'Correy: {round((correy/vote_total)*100,2)}% ({correy})'])
    csvwriter.writerow([f'Li: {round((li/vote_total)*100,2)}% ({li})'])
    csvwriter.writerow([f"O'Tooley: {round((otooley/vote_total)*100,2)}% ({otooley})"])
    csvwriter.writerow(["-----------------------------------------------------------------------"])
    csvwriter.writerow([f'Winner: {winner}'])
    csvwriter.writerow(["-----------------------------------------------------------------------"])