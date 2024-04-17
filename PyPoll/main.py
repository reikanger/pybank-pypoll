#!/usr/bin/env python3

import csv
import os

input_file = os.path.join("resources", "election_data.csv")
export_file = os.path.join("analysis", "election_results.txt")

votes = []

def get_percent(x, total):
    '''return percentage value of x compared to total'''
    return round((x / total) * 100, 3)

if __name__ == '__main__':
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header

        # read in the votes
        for row in reader:
            votes.append(row[2]) # append candidate name to list of votes

        # total number of votes cast
        total_votes = len(votes)

        # build dictionary of candidate to their total number of votes
        candidate_votes = {}
        for unique_name in list(set(votes)):
            candidate_votes[unique_name] = votes.count(unique_name)

        # find winning candidate
        highest_vote = max(candidate_votes.values())
        for name, votes in candidate_votes.items():
            if votes == highest_vote:
                winning_candidate = name
                break

        # build output
        output_string = "Election Results\n"
        output_string += "-------------------------\n"
        output_string += f"Total Votes: {total_votes}\n"
        output_string += "-------------------------\n"

        for name, votes in candidate_votes.items():
            output_string += f"{name}: {get_percent(votes, total_votes)}% ({votes})\n"

        output_string += "-------------------------\n"
        output_string += f"Winner: {winning_candidate}\n"
        output_string += "-------------------------"

        # print to console
        print(output_string)

        # write to file
        with open(export_file, 'w') as fd:
            fd.write(output_string)
