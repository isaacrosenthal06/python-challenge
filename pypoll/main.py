import os
import csv
# Create lists to hold values
votes = []
candidates = []
uniquecandidates = []
votescandidate0 = []
votescandidate1 = []
votescandidate2 =[]

votes0collective = []
votes1collective = []
votes2collective = []

#Path to collect data from the resources folder
election_csv = os.path.join( '..', 'pypoll', 'resources',  'election_data.csv')

#read in the CSV file
with open(election_csv) as csvfile:
    # Split data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #loop through all rows, set votes equal to values in column 0, and candidates equal to values in column 2
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

#loop through candidate list, and find candidates different from their succesor
for i in range(0, len(candidates) - 1):
    if candidates[i +1] != candidates[i]:
        uniquecandidates.append(candidates[i])

#read in the CSV file
with open(election_csv) as csvfile:
    #split data on commas
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #loop through rows, if row 2 value is equal to a unique candidate, add the vote info to that candidates vote total
    for row in csvreader:
        if row[2] == uniquecandidates[0]:
            votescandidate0.append(row[0])
        elif row[2] == uniquecandidates[1]:
            votescandidate1.append(row[0])
        elif row[2] == uniquecandidates[2]:
            votescandidate2.append(row[0])

#total votes equal to number of elements in votes list
totalvotes = len(votes)
#candidates equal to number of elements in unique candidate lsit
totalcandidates = len(uniquecandidates)

#calculate percent votes for each candidate by dividing by total votes, and multiple by 100
percentvotes0 = round((len(votescandidate0)/totalvotes) * 100, 3)
percentvotes1 = round((len(votescandidate1)/totalvotes) * 100, 3)
percentvotes2 = round((len(votescandidate2)/totalvotes) * 100, 3)

#zip candidate percent votes with their respective total votes
votes0collective = list(zip((str(percentvotes0) + '%' , str((len(votescandidate0))))))
votes1collective = list(zip((str(percentvotes1) + '%' , str((len(votescandidate1))))))
votes2collective = list(zip((str(percentvotes2) + '%' , str((len(votescandidate2))))))




#print desired results
print('Election Results')
print('----------------------')
print('total votes: ' + str(totalvotes))
print('----------------------')
print(str(uniquecandidates[0] + ': ' + str(votes0collective)))
print(str(uniquecandidates[1] + ': ' + str(votes1collective)))
print(str(uniquecandidates[2] + ': ' + str(votes2collective)))
print('----------------------')
if percentvotes0 > percentvotes1 and percentvotes0 > percentvotes2:
    print("winner: " + str(uniquecandidates[0]))
elif percentvotes1 > percentvotes0 and percentvotes1 > percentvotes2:
    print("winner: " + str(uniquecandidates[1]))
elif percentvotes2 > percentvotes1 and percentvotes2 > percentvotes0:
    print("winner: " + str(uniquecandidates[2]))

