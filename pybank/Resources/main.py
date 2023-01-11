#In this challenge, you are tasked with creating a Python script to sum, and extract profit and loss from a csv file.
import os
import csv

#importing csvfile

budgetdata_csv = os.path.join("","Resources", "budget_data.csv")
with open(budgetdata_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)

#operation variables
    net_profit = 0
    max_profit =0
    max_loss = 0
    month_count=0

    for row in csvreader:
        net_profit = net_profit+int(row[1])
        month_count +=1
        if int(row[1]) > max_profit:
            max_profit = int(row[1])
            month_profit = str(row[0])
        if int(row[1]) < max_loss:
            max_loss = int(row[1])
            month_loss = str(row[0])

    #Writing the results in text file in same directory as the main.py doc
    outfile = open("bank_data.txt", "w")
    outfile.write("Financial Analysis \n")
    outfile.write("The total profit for the bank is: $"+ str(net_profit)+ "\n")
    outfile.write("Total months: "+ str(month_count)+"\n")
    outfile.write(f'Greatest increase in Profits ${max_profit} in {month_profit}' + "\n") 
    outfile.write(f'Greatest Decrease in Profits ${max_loss} in {month_loss}' + "\n") 
    outfile.close()

    #Printing results on Terminal
    print("Financial Results")
    print("The total profit for the bank is: "+ str(net_profit))
    print("Total months: "+ str(month_count))
    print(f'Greatest increase in Profits $ {max_profit} in {month_profit}')
    print(f'Greatest Decrease in Profits {max_loss} in {month_loss}')


