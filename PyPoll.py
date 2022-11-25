# Dependencies
import csv
import os

# Adding file path variables
file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initializng a total vote counter
total_votes = 0

# Creating spaces to store candidates and their votes recieved
candidate_options = []
candidate_votes = {}

# Creating a county list and county votes dictionary
counties = []
county_votes = {}

# Tracking the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Tracking the largest county and county voter turnout
largest_turnout = ""
largest_turnout_count = 0
largest_turnout_percentage = 0

# Reading the csv and converting it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Reading the header
    header = next(reader)

    # Iterating through each row in the header
    for row in reader:

        # Adding to the total vote count
        total_votes = total_votes + 1

        # Getting the candidate name from each row
        candidate_name = row[2]

        # Extracting the county name from each row
        county_name = row[1]

        # If the candidate does not match any existing candidate, adding it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Adding the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Adding a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # If the county name does not match an existing county, adding it to 
        # the county list
        if county_name not in counties:

            # Adding the existing county to the list of counties
            counties.append(county_name)

            # Tracking the county's vote count
            county_votes[county_name] = 0

        # Adding a vote to that county's vote count
        county_votes[county_name] += 1


# Saving the results to a text file
with open(file_to_save, "w") as txt_file:

    # Printing the final vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # Getting the county from the county dictionary
    for county in county_votes:
        # Retrieving the county vote count
        vote = county_votes[county]
        
        # Calculating the percentage of votes for the county
        county_percentage = (vote/total_votes) * 100

        # Printing the county results
        county_results = (f"{county}: {county_percentage:.1f}% ({vote:,})\n")
        print(county_results)
        txt_file.write(county_results)
        
        # Determining the winning county and getting its vote count
        if (vote>largest_turnout_count):

            largest_turnout_count = vote

            largest_turnout = county

    # Printing the county with the largest turnout
    turnout_results = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"-------------------------\n"
    )
    print(turnout_results)
    txt_file.write(turnout_results)

    # Saving the final candidate vote count to the text file
    for candidate_name in candidate_votes:

        # Retrieving vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Printing each candidate's voter count and percentage
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determining winning vote count, winning percentage, and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Printing the winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)