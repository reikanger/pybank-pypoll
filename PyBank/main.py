#!/usr/bin/env python3

import csv
import os

export_file = os.path.join("analysis", "budget_analysis.csv")
input_file = os.path.join("resources", "budget_data.csv") 

months = []

if __name__ == "__main__":


    budget_data = {}

    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header

        for row in reader:
            budget_data[row[0]] = row[1]

    # total number of months included in dataset
    total_months = len(budget_data.keys())

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print("Total: ")
    print("Average Change: $")
    print("Greatest Increase in Profits: ($)")
    print("Greatest Decrease in Profits: ($)")
