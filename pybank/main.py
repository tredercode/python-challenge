import os # Import the os module.  This allos us to create file paths accorss operating systems. (2.08)
import csv # Import module for reading CSV files. (2.08)

# Create the file path. (2.08) Note - do not need to use '..' because directory is already in 'PyBank'.
csvpath = os.path.join('Resources','budget_data.csv')

total_months = 0 # Initial count for counting total months.
profit_loss_count = 0 # Initial count for counting Profit/Loss.
changes = [] # Change list to store the chanes in Profit/Loss.
dates = [] # Date list to store dates correspoing to Profit/Loss changes.

# Read the CSV file using CSV module. (2.08)
with open(csvpath) as csvfile:
    # CSV reader specifies variable and delimiter that holds contents. (2.08)
    csvreader = csv.reader(csvfile,delimiter=',')
    
    # Read the header row. This also skips the row. (2.08)
    csv_header = next(csvreader)

    # Read each row of data after the header. (2.08)
    previous_profit_loss = 0
    for row in csvreader:
        total_months += 1 # Count the number of rows (total months).
        profit_loss_count += int(row[1]) # Count the total Profit/Losses.

        current_profit_loss = int(row[1])
        if total_months > 1:
            monthly_change = current_profit_loss - previous_profit_loss
            changes.append(monthly_change)
            dates.append(row[0]) # Stores the dates corresponding to the changes.
        previous_profit_loss = current_profit_loss

    # Print total months and total Profit/Loss.
    print(f"Total Months: {total_months}")
    print(f"Total: ${profit_loss_count}")

    # Print average change.
    average_change = round(sum(changes) / len(changes),2)
    print(f"Average Change: ${average_change}")

    # Print greatest increase and month that it occured. 
    greatest_increase = max(changes)
    greatest_increase_date = dates[changes.index(greatest_increase)]
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")

    # Print greatest decrease and month that it occured.
    greatest_decrease = min(changes)
    greatest_decrease_date = dates[changes.index(greatest_decrease)]
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Make text file and write to it.

# Create a file in the "analysis" folder.  This will create a file named "financial_analysis.txt". 
filepath = os.path.join("analysis","financial_analysis.txt")

# Write to the file path.
with open(filepath, "w") as file:
    file.write("Analysis Results:\n")
    file.write("-----------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${profit_loss_count}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

