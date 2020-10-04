#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:07:51 2020

@author: christinemagnotta
"""

#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.


#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


#The total number of votes cast


#A complete list of candidates who received votes


#The percentage of votes each candidate won


#The total number of votes each candidate won


#The winner of the election based on popular vote.


import os
import csv
electionData = os.path.join('election_data.csv')

with open('election_data.csv', 'r') as csvfile:
    electionData = list(csv.reader(csvfile, delimiter= ",")
        
        for columns in electionData:
            
            votes.append(rows[0])
            candidates.append(rows[2])
            
        totalVotes = len(votes)
        print(totalVotes)
              
    #header = next(electionData)                    
    #votes = 0
    #totalVotes = 0
    
    #for rows in electionData


#i want to count the total number of votesfor each of four candidates
#and then find the winner based on the percentage
#this looks like a list I want to append
     
        #votes = int(rows[0])
        #candidates = str(electionData[2])
        #totalVotes += 1
        
        
        
        #candidateA = str("Khan", (electionData[2]))
        #print(candidateA)
        #candidateB = str("Correy", (electionData[2]))
        #candidateC = str("Li", (electionData[2]))
        #candidateD = str("O'Tooley", (electionData[2]))
        
        #print(totalVotes)
        #print("Khan")
        

#it = iter(col)
#next(it, None)  # skip first entry
#for column in it:
    #print column
        


#ATTEMPTING TO REVERSE ENGINEER THIS.


        
        #print
        
        #votes.append
        
        
        #totalVotes = int(electionData[0])
        #candidates = str(electionData[2])
        #candidateA = str(electionData[2])
        #candidateB = str(electionData[2])
        #candidateC = str(electionData[2])
        #candidateD = str(electionData[2])
        
            #if candidates = "Khan":
                #candidateA = 
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)

                
       

        #def electionResults(electionData):
            #data_list = list(csv.reader(data_delim))
            
            
            #so i want to list the candidates
            #then i want to count the votes each candidate got
            #then do some division to get percentages.
            
            #totalVotes len(electionData)
                
            
        
    #return len
    
    
    
    #def num_rows(group):
    #return len(group)

#def num_columns(group):
    #return len(group[0])
    
    
        #totalVotes = len(votes)
        
        #print(totalVotes)

    
    #for rows in electionData:
        
        #totalVotes = int(rows[0])
        #totalVoteCount += 1
        
        
        #print(totalVoteCount)
    
    
    
    
    
    #allCandidates = str(row[2])
    
   #totalVotes = rows[i - 1]
   
   

#three columns, voter id county candidate
#voterid = column 1, int
#county = column 2, str
#candidate = column 3, str
    #/Users/christinemagnotta/python-challenge/python-challenge/python-challenge solutions/PyPoll/election_data.csv

#ef print_percentages(wrestler_data):
    # For readability, it can help to assign your values to variables with descriptive names
    #name = str(wrestler_data[0])
    #wins = int(wrestler_data[1])
    #losses = int(wrestler_data[2])
    #draws = int(wrestler_data[3])

    # Total matches can be found by adding wins, losses, and draws together
    #total_matches = wins + losses + draws

    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    #win_percent = (wins / total_matches) * 100

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    #loss_percent = (losses / total_matches) * 100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    #draw_percent = (draws / total_matches) * 100

    # If the loss percentage is over 50, type_of_wrestler is "Jobber". Otherwise it is "Superstar".
    #if loss_percent > 50:
        #type_of_wrestler = "Jobber"
    #else:
        #type_of_wrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    #print(f"Stats for {name}")
    #print(f"WIN PERCENT: {win_percent}")
    #print(f"LOSS PERCENT: {loss_percent}")
    #print(f"DRAW PERCENT: {draw_percent}")
    #print(f"{name} is a {type_of_wrestler}")


# Read in the CSV file
#with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    #csvreader = csv.reader(csvfile, delimiter=',')

    #header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for
    #name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    #for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        #if name_to_check == row[0]:
            #print_percentages(row)
