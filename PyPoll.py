import csv
import os

# input data file
file_to_load = ('/Users/caleb/Desktop/bootcamp/projects/python_projects/election_analysis/Resources/election_results.csv')

# output file
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# defining variables
total_votes = 0

candidate_options = []

candidate_votes = {}

winning_candidate = ""

winning_count = 0

winning_percentage = 0

# reading the data
with open(file_to_load) as election_data:
    
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    
    # counting total votes
    for row in file_reader:
        
        total_votes += 1
        
        candidate_name = row[2]

        # determining each unique candidate
        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        # counting votes for each candidate
        candidate_votes[candidate_name] +=1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # calculating percentage of votes won by each candidate
    for candidate_name in candidate_votes:
        
        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)
        
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)