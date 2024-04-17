#!/usr/bin/env python3

import csv
import os

export_file = os.path.join("analysis", "budget_analysis.txt")
input_file = os.path.join("resources", "budget_data.csv") 

budget_data = {}
months = []

if __name__ == "__main__":
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header

        for row in reader:
            budget_data[row[0]] = int(row[1])

    # total number of months included in dataset
    total_months = len(budget_data.keys())

    # net total amount of profit/losses over entire period
    total_profit_loss = sum(budget_data.values())

    # changes in profit/losses over entire period
    changes = []
    profit_losses = list(budget_data.values())  # dictionaries are un-ordered, maybe a problem? looks like it works

    for i in range(1, len(profit_losses)):
        changes.append(profit_losses[i] - profit_losses[i - 1])

    # average of changes in profit/losses over entire period
    changes_average = round(sum(changes) / len(changes), 2)

    # greatest increase in profits (date and amount) over entire period
    greatest_increase = max(changes)

    # greatest decrease in profits (date and amount) over entire period
    greatest_decrease = min(changes)

    # find the matching dates where greatest increase and greatest decrease occurred
    # iterate over budget_data twice to be able to compare against two entries - credit to Google Gemini for the nested for loop idea
    for date, pl in budget_data.items():
        for date2, pl2 in budget_data.items():
            if pl - pl2 == greatest_increase:
                #print(f"greatest increase - date: {date} and change: {pl - pl2}")
                greatest_increase_date = date
            if pl - pl2 == greatest_decrease:
                #print(f"greatest decrease - date: {date} and change: {pl - pl2}")
                greatest_decrease_date = date

    # build output
    output_string = ""
    output_string += "Financial Analysis\n"
    output_string += "----------------------------\n"
    output_string += f"Total Months: {total_months}\n"
    output_string += f"Total: ${total_profit_loss}\n"
    output_string += f"Average Change: ${changes_average}\n"
    output_string += f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    output_string += f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"

    # write to console
    print(output_string)

    # write to file
    with open(export_file, 'w') as fd:
        fd.write(output_string)
