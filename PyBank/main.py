#!/usr/bin/env python3

import csv
import os

export_file = os.path.join("analysis", "budget_analysis.csv")
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

    # greatest decrease in profits (date and amount) over entire period

    output_string = ""
    output_string += "Financial Analysis\n"
    output_string += "----------------------------\n"
    output_string += f"Total Months: {total_months}\n"
    output_string += f"Total: ${total_profit_loss}\n"
    output_string += f"Average Change: ${changes_average}\n"
    output_string += f"Greatest Increase in Profits: {} (${})\n"
    output_string += f"Greatest Decrease in Profits: {} (${})"

    # write to console
    print(output_string)

    # write to file
    with open(export_file, 'w') as fd:
        fd.write(output_string)

    # testing - to remove
    print()
    print(budget_data["Jan-14"])
    print(budget_data["Feb-14"])
