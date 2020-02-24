#Homework for Python series
import os
import csv

# Path to collect data from the budget_data file
election_data = os.path.join('election_data.csv')

voter_count = 0
Khan_count = 0
Khan_pct = 0.000
Khan_pct = float(Khan_pct)

Correy_count = 0
Correy_pct = 0.000
Correy_pct = float(Correy_pct)

Li_count = 0
Li_pct = 0.000
Li_pct = float(Li_pct)

OTooley_count = 0
OTooley_pct = 0.000
OTooley_pct = float(OTooley_pct)

Runoff_count = 0
Runoff2_count = 0

Runoff_str = " "
Runoff_str = str(Runoff_str)
Runoff2_str = " "
Runoff2_str = str(Runoff2_str)
Winner_str = " "
Winner_str = str(Winner_str)

# Read in the CSV file
with open(election_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        voter_count += 1

        if row[2] == 'Khan':
             Khan_count += 1
        elif row[2] == 'Correy':
            Correy_count += 1
        elif row[2] == 'Li':
            Li_count += 1
        else:
            OTooley_count += 1

if Khan_count >= Correy_count:
    Runoff_str = 'Khan'
    Runoff_count = Khan_count
elif Khan_count < Correy_count:
    Runoff_str = 'Correy'
    Runoff_count = Correy_count

if Li_count >= OTooley_count:
    Runoff2_str = 'Li'
    Runoff2_count = Li_count
elif Li_count < OTooley_count:
    Runoff2_str = 'OTooley'
    Runoff_count = OTooley_count

if Runoff_count >= Runoff2_count:
    Winner_str = Runoff_str
elif Runoff_count < Runoff2_count:
    Winner_str = Runoff2_str

Khan_pct = (Khan_count / voter_count) * 100
Khan_pct = round(Khan_pct, 2)
Correy_pct = (Correy_count / voter_count) * 100
Correy_pct = round(Correy_pct, 2)
Li_pct = (Li_count / voter_count) * 100
Li_pct = round(Li_pct, 2)
OTooley_pct = (OTooley_count / voter_count) * 100
OTooley_pct = round(OTooley_pct, 2)

print("Election results: ")
print("-------------------")
print("Total Votes: ", voter_count)
print("-------------------")
print("Khan: ", Khan_pct, "% (", Khan_count, ")")
print("Correy: ", Correy_pct, "% (", Correy_count, ")")
print("Li: ", Li_pct, "% (", Li_count, ")")
print("O'Tooley:  ", OTooley_pct, "% (", OTooley_count, ")")
print("-------------------")
print("Winner: ", Winner_str)
print("-------------------")


import sys
sys.stdout=open("output_file.txt","w")

print("Election results: ")
print("-------------------")
print("Total Votes: ", voter_count)
print("-------------------")
print("Khan: ", Khan_pct, "% (", Khan_count, ")")
print("Correy: ", Correy_pct, "% (", Correy_count, ")")
print("Li: ", Li_pct, "% (", Li_count, ")")
print("O'Tooley:  ", OTooley_pct, "% (", OTooley_count, ")")
print("-------------------")
print("Winner: ", Winner_str)
print("-------------------")
sys.stdout.close()