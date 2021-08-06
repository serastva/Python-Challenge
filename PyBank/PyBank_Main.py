#Import Modules
import csv
from pathlib import Path

#Variables
total_months = 0
total_revenue = []
month_profit_change = []
date = []

#Set path to open the file
csvpath = Path('PyBank/Resources/budget_data.csv')
#Create an output text file
txt_file = Path('PyBank/PyBank_Summary.txt')

#Open the CSV file
with open(csvpath, "r") as csvfile:
    
    #CSV reader speifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile,delimiter=',')
   
    #read the header row first
    csv_header = next(csvreader)
    
    #For loop which will calculate the total months and total sum
    for row in csvreader:
        
        #Calculates the total months    
        total_months = total_months + 1
       
        #Calculates the total revenue
        total_revenue.append(int(row[1]))
       
        #Adds all of the values in the profits/losses to calculate the total
        sum_total_revenue = sum(total_revenue)

        date.append(row[0])

#Calculates the average of profit/loss 
for i in range(1, len(total_revenue)):
    month_profit_change.append((int(total_revenue[i]) - int(total_revenue[i-1])))

average_change = sum(month_profit_change)/len(month_profit_change)

#Calculates greatest increase and decrease
greatest_increase_profits = max(month_profit_change)
greatest_decrease_profits = min(month_profit_change)

#calls the dates for greatest increase and decrease
date_increase = date[month_profit_change.index(greatest_increase_profits)]
date_decrease = date[month_profit_change.index(greatest_decrease_profits)]
        
#Output to console

msg = []
msg.append('Financial Analysis')
msg.append("-------------------------")
msg.append(f'Total: ${sum_total_revenue}')
msg.append(f'Average Change: ${round(average_change,2)}')
msg.append(f'Greatest Increase in Profits: {date_increase} (${greatest_increase_profits})')
msg.append(f'Greatest Decrease in Profits: {date_decrease} (${greatest_decrease_profits})')

# Write to text file
with open(txt_file, "w") as file:
    for i in msg:
        file.write(str(i)+'\n')
        print(str(i))
    file.close()
        

    
