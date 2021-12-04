import csv
from pprint import pprint

#Initiating the menu choices'values
GET_SUM = 1
GET_DATA = 2
QUIT = 3

the_list = []
cryptos = {}
#Defining function for the menu
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




#Initating values of totals Buy and Sell
totBuy = 0
totSell = 0

#Reading the CVS file 
with open('example_log.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

#Summing transactions with 'Buy' and 'Sell' type:
    for row in reader:
         
          if row['Transaction Type'] =='Buy':
            totBuy += float(row['Quantity Transacted'])
         
          if row['Transaction Type'] =='Sell':
            totSell += float(row['Quantity Transacted'])
            
          
          data = row['Asset'] +": "+ row['Quantity Transacted']

          if(row['Asset'] in cryptos.keys()):
            cryptos[row['Asset']] += float(row['Quantity Transacted'])
          else:
            # print(row['Quantity Transacted'])
            cryptos[row['Asset']] = float(row['Quantity Transacted'])

          the_list.append(data)
#Printing the results 
    valOfAcc = totBuy - totSell

    #Defining the summing function
def get_sum():
  print("The total sum of all the 'Buy' transactions is:  ",totBuy)
  
  print("The total sum of all the 'Sell'transactions is:  ",totSell)

  print("The value of the account is: ",valOfAcc)

def get_data(data):
    for line in the_list:
      print(line)

#Menu choices and output
choice = 0
while choice != QUIT:
  choice = get_menu()
  if choice == GET_SUM:
    get_sum()
  if choice == GET_DATA:
    for x, y in cryptos.items():
      print(x,": ",y)
    # print(cryptos)
    # get_data(data)
  elif choice == QUIT:
    print("You have left the program.\nWe hope to see you soon!\U0001F44B")

