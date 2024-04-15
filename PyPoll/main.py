#!/usr/bin/env python3

import csv
import os

input_file = os.path.join("resources", "election_data.csv")

votes = []

def get_total_votes(name, votes):
    votes.count(name)
    return False

def get_total_percent():
    return False

if __name__ == '__main__':
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header

        # read in the votes
        for row in reader:
            votes.append(row[2]) # append candidate name to list of votes

        # total number of votes cast
        total_votes = len(votes)

        results = []  # intended for list of dictionaries - results for each candidate
        for unique_name in list(set(votes)):
            results.append({ # add dictionary of candidate and vote count
                'name': unique_name,
                'total_votes': votes.count(unique_name),
                'percent_votes': (votes.count(unique_name) / total_votes) * 100
            })

        # print results
        for result in results:
            print(result)




        #output_string = "Election Results\n"
        #output_string += "-------------------------\n"
        #output_string += f"{}: {}% ({})\n"
        #output_string += f"{}: {}% ({})\n"
        #output_string += f"{}: {}% ({})\n"
        #output_string += f"{}: {}% ({})\n"
        #output_string += f"{}: {}% ({})\n"
        #output_string += f"{}: {}% ({})\n"
        #output_string += f"{}: {}% ({})\n"
        #output_string += f"{}: {}% ({})\n"
