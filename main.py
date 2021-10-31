import csv
from pprint import pprint

# Initaiting values of totals Buy and Sell
totBuy = 0
totSell = 0

# Reading the CVS file 
with open('example_log.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

# Summing transactions with 'Buy' and 'Sell' type:
    for row in reader:
         
          if row['Transaction Type'] =='Buy':
            totBuy += float(row['Quantity Transacted'])
         
          if row['Transaction Type'] =='Sell':
            totSell += float(row['Quantity Transacted'])
    
# Printing the results 
    print("The total sum of all the 'Buy' transactions is:  ",totBuy)
    
    print("The total sum of all the 'Sell'transactions is:  ",totSell)
