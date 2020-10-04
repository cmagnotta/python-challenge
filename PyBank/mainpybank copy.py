#The average of the changes in "Profit/Losses" over the entire period
#???

#The greatest increase in profits (date and amount) over the entire period


#The greatest decrease in losses (date and amount) over the entire period

import os
import csv
budget_data = os.path.join('budget_data.csv')

with open ('budget_data.csv', 'r') as csvfile:
    budget_data = csv.reader(csvfile)
    next(budget_data)                         
    numMonths = 0
    totalProfits = 0
      
    
    for rows in budget_data:

        months = str(rows[0])
        numMonths += 1
        totalProfits += int(rows[1])
        greatestTotalProfits = totalProfits - (totalProfits + 1)        
        
          
        #def profit_difference(budget_data):
            #totalProfits = totalProfits - (totalProfits + 1)
            #print(totalProfits)
        
            
            
            #if numMonths != 0: #find difference between months and the losmallest change
                #last_month = float(rows[i-1])
                #date = str(rows[i-1])            
                #return profit_difference  
            
    averageProfits = totalProfits/numMonths    
    print(f"Total Months: {numMonths}")
    print(f"Total: {totalProfits}")
    print(f"Average Profit: {averageProfits}")
    print(f"Greatest Increase in Profits: {greatestTotalProfits}") #print(months)
    #print(f"Greatest Decrease in Profits: {greatestLossProfits}") print(months)
    
    
          
          #return(min(lprofit_difference)) and print(months)

          