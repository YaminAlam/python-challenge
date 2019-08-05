# Modules
import os
import csv


# Set path for file
csvpath = os.path.join("election_data.csv")

#initial variables
vote_count = 0
max_vote = 0

#initial blank dictionary
voterFreqDic = {}

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skipping the header
    next(csvreader, None)
    
    
    for row in csvreader:

        #treats each line in csv file as a vote
        vote_count += 1

        #if a candidate is not in the voterFreq dictionary, update the keys with their name and 
        #give them 1 vote
        if row[2] not in voterFreqDic:
            voterFreqDic.update( {row[2] : 1} )
        else: 

            #if their name is already in the dictionary, update that value for the key(candidate) by 1
            voterFreqDic[row[2]]+=1
   
#printing out information to relay
print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")
for candidate,votes in voterFreqDic.items():
    print(f"{candidate}: {round((voterFreqDic[candidate]/vote_count)*100,0)}% ({votes})")
print("-------------------------")
print(f"Winner: {max(voterFreqDic, key = voterFreqDic.get)}")
print("-------------------------")

 #exporting text file of summary
summary = open("summary.txt", "w")
summary.write("Election Results \n")
summary.write("------------------------- \n")
summary.write(f"Total Votes: {vote_count} \n")
summary.write(f"------------------------- \n")
for candidate,votes in voterFreqDic.items():
    summary.write(f"{candidate}: {round((voterFreqDic[candidate]/vote_count)*100,0)}% ({votes}) \n")
summary.write(f"------------------------- \n")
summary.write(f"Winner: {max(voterFreqDic, key = voterFreqDic.get)} \n")
summary.write("-------------------------")
summary.close()
