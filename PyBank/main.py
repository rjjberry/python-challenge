#Homework for Python series
import os
import csv

# Path to collect data from the budget_data file
budget_data = os.path.join('budget_data.csv')

total = 0
number = 0
last_number = 0
g_incr_prof = 0
monthly_diff = 0
total_monthly_diff = 0
avg_change = 0.00
avg_change = float(avg_change)
g_decr_prof = 0
month_count = 0
last_month_str = " "
last_month_str = str(last_month_str)

# Read in the CSV file
with open(budget_data, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row
    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
#    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:
#          Capture monthly Profit/Loss amt
        number = int(row[1])
#          Capture Total monthly Profit/Loss amt
        total += number      
        
#       print(row[0], row[1], total, month_count, last_month_str)
#          Capture monthly difference amt
        monthly_diff = number - last_number
#          Capture total monthly difference amt
        
#          Capture largest increase amt        
        if monthly_diff > g_incr_prof:
           g_incr_prof = monthly_diff
#          Capture smallest decrease amt        
        if monthly_diff < g_decr_prof:
           g_decr_prof = monthly_diff
#          Capture monthly count        
        if row[0] != last_month_str:
           last_month_str = str(row[0])
           month_count += 1

        total_monthly_diff += monthly_diff
        last_number = number
    else:
#          Capture/Calculate avg change        
        avg_change = total_monthly_diff / month_count    
#          Print final totals
        print("Financial Analysis")
        print("------------------")
        print("Total Months: ", month_count)
        print("Total: ", total)
        print("Average Change: ", avg_change)
        print("Greatest Increase in Profits:  ", g_incr_prof)
        print("Greatest Decrease in Profits:  ", g_decr_prof)

        import sys
        sys.stdout=open("output_file.txt","w")

#          Output final totals to file
        print("Financial Analysis")
        print("------------------")
        print("Total Months: ", month_count)
        print("Total: ", total)
        print("Average Change: ", avg_change)
        print("Greatest Increase in Profits:  ", g_incr_prof)
        print("Greatest Decrease in Profits:  ", g_decr_prof)
        sys.stdout.close()
