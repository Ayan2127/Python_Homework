import csv


budget_csvpath = "/Users/ayankhalif/Downloads/Starter_Code-6/PyBank/Resources/budget_data.csv"

with open(budget_csvpath, encoding= 'utf') as csvfile:
  csvreader = csv.reader(csvfile, delimiter= ",")
  
  #skips header
  next(csvreader, None)
  
  #list variables
  total_months = []
  net_profit = []
  profit_change = []
  

  #for each column- append values for column 0 (months) and column 1 (profit/losses)
  for column in csvreader:
    
     total_months.append(column[0])
     net_profit.append(int(column[1]))
     
  #for each n in selected range append subtracted net profit values by month  
  #source:https://copyprogramming.com/howto/how-does-iterating-through-range-len-input-string-1-1-1-give-the-reverse-string 
  for n in range(len(net_profit)-1):
     profit_change.append((net_profit[n+1])-(net_profit[n]))
     
     
     #max and min functions to find greatest profit and lowest profit
     greatest_profit = max(profit_change)
     lowest_profit = min(profit_change)

  #End print statements, included 'print("")' to ensure print statements generate neatly to terminal
  print(" ") 
  print("Financial Analysis:")
  print("_____________________________________")
  print(f"Total Months: {len(total_months)}")
  print(f"Total: ${sum(net_profit)}")
  print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
  print(f"Greatest Increase in Profits: {total_months[profit_change.index(max(profit_change))+1]} ${(greatest_profit)}")
  print(f"Greatest Decrease in Profits: {total_months[profit_change.index(min(profit_change))+1]} ${(lowest_profit)}")
  print(" ")
  
  with open('financial_analysis.txt', 'w') as f:
     f.write("Finacial Analysis:  ")
     f.write("\n")
     f.write('_____________________________________')
     f.write("\n")
     f.write(f"Total Months: {len(total_months)}")
     f.write("\n")
     f.write(f"Total: ${sum(net_profit)}")
     f.write("\n")
     f.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
     f.write("\n")
     f.write(f"Greatest Increase in Profits: {total_months[profit_change.index(max(profit_change))+1]} ${(greatest_profit)}")
     f.write("\n")
     f.write(f"Greatest Decrease in Profits: {total_months[profit_change.index(min(profit_change))+1]} ${(lowest_profit)}")

     
     
