## PyPoll Instructions
#In this challenge, you are tasked with creating a Python script to sum, and extract profit and loss from a csv file.
import os
import csv

#importing csvfile

electiondata_csv = os.path.join("","Resources", "election_data.csv")
with open(electiondata_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csv_header = next(csvfile)

#operation variables
    charles_casper = 0
    diana_degette =0
    raymon_anthony = 0
    vote_count = 0
    candidate_list = []
    for row in csvreader:
        vote_count +=1
        if row[2] not in candidate_list:
            candidate_list.append(str(row[2]))
        if row[2] == candidate_list[0]:
            charles_casper+=1
        elif row[2] == candidate_list[1]:
            diana_degette +=1
        elif row[2] == candidate_list[2]:
            raymon_anthony +=1
#Sorting and selecting a winner
    results = {candidate_list[0]:charles_casper,
    candidate_list[1]:diana_degette, candidate_list[2]:raymon_anthony}
    winner =max(zip(results.values(), results.keys()))[1]
    
 #Percentages rounded to 3 decimal places

charles_cas_percent= round((charles_casper/vote_count)*100,3)
diana_deg_percent= round((diana_degette/vote_count)*100,3)
ray_ant_percent= round((raymon_anthony/vote_count)*100,3)

#creating a poll data.txt file with the election results
outfile = open("Poll_data.txt", "w")
outfile.write("----------------------\n")
outfile.write("Election Results \n")
outfile.write("---------------------- \n")
outfile.write("Total Votes: "+ str(vote_count)+ "\n")
outfile.write("----------------------\n")
outfile.write(f'{candidate_list[0]}: {charles_cas_percent} ({charles_casper})' + "\n")
outfile.write(f'{candidate_list[1]}: {diana_deg_percent} ({diana_degette})' + "\n") 
outfile.write(f'{candidate_list[2]}: {ray_ant_percent} ({raymon_anthony})' + "\n") 
outfile.write(f'Winner: {winner}' + "\n")
outfile.write("----------------------")
outfile.close()

#Verify
print(candidate_list)
print("Total Votes: " + str(vote_count))
print("election results " + str(results))
print(f'Charles Casper {charles_cas_percent}')
print(f'Diana Degette {diana_deg_percent}')
print(f'Raymon Anthony Doane: {ray_ant_percent}')
print(winner)