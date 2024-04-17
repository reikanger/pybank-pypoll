# Homework 3

Run the main.py scripts, one each for PyBank and PyPoll, with a Python interpreter:
```shell
python main.py
```

## Repository Contents
- Images - image files from starter code archive 
- PyBank - PyPoll files
- PyPoll - PyPoll files
- Instructions.pdf - instructions for assignment copied from class website

### PyBank
- main.py - main script of the PyBank assignment
- analysis - output files created by main.py
- resources - input files processed by main.py

### PyPoll
- main.py - main script of the PyPoll assignment
- analysis - output files created by main.py
- resources - input files processed by main.py

## Credits
Google Gemini helped give me the idea to iterate over the budget_data dictionary in PyBank twice, in order to compare values.

Code snippet in question:
```python
# find the matching dates where greatest increase and greatest decrease occurred
# iterate over budget_data twice to be able to compare against two entries - credit to Google Gemini for the nested for loop idea
for date, pl in budget_data.items():
  for date2, pl2 in budget_data.items():
    if pl - pl2 == greatest_increase:
      greatest_increase_date = date
    if pl - pl2 == greatest_decrease:
      greatest_decrease_date = date
```
