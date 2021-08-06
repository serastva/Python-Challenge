#Import Modules
import csv
from pathlib import Path

#Variables

total_votes = 0
total_candidates = 0
candidates = []
candidates_votes = []
candidate_percentage = []
percent_votes = []


#Set path to open the file
csvpath = Path('PyPoll/Resources/election_data.csv')
txt_file = Path('PyPoll/PyPoll_Summary.txt')

#opens the csv file
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
   
    #read the header row first
    csv_header = next(csvreader)

    for row in csvreader:
        #Counts total votes 
        total_votes = total_votes + 1
        total_candidates = row[2]
        
        #finds unique candidates and appends the candidate list with them
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_count = candidates.index(row[2])
            candidates_votes.append(1)
        else:
            candidates1 = candidates.index(row[2])
            candidates_votes[candidates1] += 1
        
    #Calculates the winning candidate
    winning_candidate = candidates[candidates_votes.index(max(candidates_votes))] 

    #Calculate percentage for each candidate 
    for votes in candidates_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage, 4)
        percent_votes.append(percentage)
    
#Output console also stores the output into a list to print later into the notebook

msg = []
msg.append('Election Results')
msg.append("-------------------------")
msg.append(f'Total Votes: {str(total_votes)}')
msg.append("-------------------------")
for i in range(len(candidates)):
    msg.append(f'{candidates[i]}:{str(percent_votes[i])}% ({str(candidates_votes[i])})')
msg.append("-------------------------")
msg.append(f'Winner: {winning_candidate}')
msg.append("-------------------------")

# Write to text file
with open(txt_file, "w") as file:
    for i in msg:
        file.write(str(i)+'\n')
        print(str(i))
    file.close()
