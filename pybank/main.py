import os
import csv

# Create lists to hold values
dates =[]
months = []
changes = []
profit_losses = []
profitchange = []

#Path to collect data from the resources folder

budget_csv = os.path.join( '..', 'pybank', 'resources',  'budget_data.csv')

#read in the CSV file
with open(budget_csv) as csvfile:
    #Split data on commas
    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)

    #loop through all rows
    for row in csvreader:
        #add column 0 values to dates list
        dates.append(row[0])
        #split month and day
        split_place = row[0].split('-')
        #add month to months list
        months.append(split_place[0])
        #add data to profit/losses list from column 1
        profit_losses.append(int(row[1]))
        
#loop through all values in profit losses list
for i in range(0, len(profit_losses) - 1):
    # if next value is different from current value
    if profit_losses[i + 1] != profit_losses[i]:
        #append profit change to include the difference between next and current vlaues
        profitchange.append(float(profit_losses[i + 1])-float(profit_losses[i]))

#total profit is sum of all data
totalprofit_losses = sum(profit_losses)
#average change by dividing total change by number of elements
averagechange = (sum(profitchange)/(len(profitchange)))
#total months equal to number of months in months list
totalmonths = len(months)

#remove 1st value of dates, so it is sinked up with profit change list
dates.remove(dates[1])

#create zip between dates and profit change
profitlossesdates = list(zip(dates, profitchange))

#print desired results
print('Financial Analysis')
print('------------------------')
print('Total: ' + '$' + str(totalprofit_losses))
print('Total months: ' + str(totalmonths))
print('Average Change: ' + '$' + str(round(averagechange, 2)))
print('Greatest Increase in Profits: ' + str(max(profitlossesdates, key=lambda x:x[1])))
print('Greatest Decrease in Profits: ' + str(min(profitlossesdates, key=lambda x:x[1])))