import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

vote_count_total = 0
candidate_list = []
unique_candidates = set()

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',') # Setup csv reader.

    csv_header = next(csvreader) # Skip the header.

    # Loop through rows to count total votes and create list of candidates.
    for row in csvreader:
        vote_count_total += 1
        candidate_list.append(row[2])

# Use a set to find unique candidate names. 
unique_candidates = set(candidate_list)

# Make dictionary for each candidate and thier votes.  Start votes at 0. 
vote_count_candidate = {element: 0 for element in unique_candidates}
for candidate in candidate_list:
    if candidate in vote_count_candidate:
        vote_count_candidate[candidate] += 1
    else:
        vote_count_candidate[candidate] = 1

# Find candidate percentages and store in dictionary.
candidate_percentages = {}
for candidate, votes in vote_count_candidate.items():
    percentage = round((votes / vote_count_total) * 100, 3)
    candidate_percentages[candidate] = percentage

# Find the winner.
winner = max(vote_count_candidate, key=vote_count_candidate.get)

# Write to text file.

# Create file path for text file.
filepath = os.path.join("analysis","election_analysis.txt")

#Write to the file path.
with open(filepath, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {vote_count_total}\n")
    file.write("-------------------------\n")
    for candidate, votes_count in vote_count_candidate.items():
        percentage = candidate_percentages[candidate]
        file.write(f"{candidate}: {percentage}% ({votes_count})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------")
    