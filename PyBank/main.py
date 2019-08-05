# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("budget_data.csv")

#variables to track
total_months = 0
net_profit = 0
net_change = 0
greatest_increase = 0
greatest_decrease = 0


#lists to record information
dates = []
profits_losses = []
dates = []
avg_change_list = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skipping the header
    next(csvreader, None)

    for row in csvreader:

        #increasing a counter by 1 as we go through the rows as each row represents a new month
        total_months += 1

        #aggregating the profits for each month to get a total net profit
        net_profit += int(row[1])

        #recording the dates and the profits/losses into separate lists
        profits_losses.append(row[1])
        dates.append(row[0])



    #updating avg_change list by using the dates and profits_losses lists;
    #each entry into the avg_change list is the difference between consecutive entries
    #  in the profits_losses list
    for i in range(1, total_months):
        avg_change_list.append(int(profits_losses[i])-int(profits_losses[i-1]))

        #adding up all entries in previous list
        net_change += avg_change_list[i-1]

    #calculating the average of the changes in profits/losses
    avg_change = net_change/len(avg_change_list)


    #going through the avg_change_list to find the greatest increase and decrease in profits
    for entry in range(1,total_months):
        if avg_change_list[entry-1] > greatest_increase:

            #if an entry on the avg_change list is higher than the previous highest entry, replace it
            greatest_increase = avg_change_list[entry-1]

            #store the index of that entry, then retrieve it from the dates list
            count_i = entry
        if  avg_change_list[entry-1]< greatest_decrease:

            #if an entry on the avg_change list is lower than the previous lowest entry, replace it
            greatest_decrease = avg_change_list[entry-1]
            Greatest_increase_date = dates[count_i]

            #store the index of that entry, then retrieve it from the dates list
            count_d = entry
            Greatest_decrease_date = dates[count_d]

    #printing all relevant information to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Net Profit: ${net_profit}")
    print(f"Average Change: ${round(avg_change,2)}")
    print(f"Greatest Increase in Profits: {Greatest_increase_date} ${greatest_increase}")
    print(f"Greatest Decrease in Profits: {Greatest_decrease_date} ${greatest_decrease}")

    #exporting text file of summary
    summary = open("summary.txt", "w")
    summary.write("Financial Analysis \n")
    summary.write("---------------------------- \n")
    summary.write(f"Total Months: {total_months} \n")
    summary.write(f"Total Net Profit: ${net_profit} \n")
    summary.write(f"Average Change: ${round(avg_change,2)} \n")
    summary.write(f"Greatest Increase in Profits: {Greatest_increase_date} ${greatest_increase} \n")
    summary.write(f"Greatest Decrease in Profits: {Greatest_decrease_date} ${greatest_decrease} \n")
    summary.close()
