import csv
from pprint import pprint

GET_SUM = 1
GET_DATA = 2
QUIT = 3

def get_menu():
  print()
  print("CryptoCurrency Log")
  print("------------------\n")
  print(GET_SUM,". Buy, Sell, and Total Account Value Overview")
  print(GET_DATA,". List Each Crypto Currency and it's total Value in the account")
  print(QUIT,". To quit the program\n")

  choice = int(input("Enter your option: "))

  while choice < GET_SUM or choice > QUIT:
    choice = int(input("Enter a valid option: "))
  return choice




# Initating values of totals Buy and Sell
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
    valOfAcc = totBuy - totSell
    def get_sum():
      print("The total sum of all the 'Buy' transactions is:  ",totBuy)
      
      print("The total sum of all the 'Sell'transactions is:  ",totSell)

      print("The value of the account is: ",valOfAcc)


choice = 0
while choice != QUIT:
  choice = get_menu()
  if choice == GET_SUM:
    get_sum()
#   elif choice == GET_DATA:
#     get_data()
#   elif choice == QUIT:
#     print('You have left the program.\nWe hope to see you soon!')

