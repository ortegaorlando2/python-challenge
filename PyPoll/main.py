# importing needed funtions and modules
import os
import csv

#We are going to open the polling file first, using relative path


#define the path

pollpath = os.path.join('Resources','election_data.csv')

#open file for reading with the file indicator votes
with open(pollpath, 'r') as votes:

#Use the reader function in csv to assign the file content to a string variable
     entirevotepoll=csv.reader(votes)
#skip the header
     pollheader = next(entirevotepoll)

#initialize values to read as separate lists the columns of the file
     VoterID=[]
     County=[]
     Candidate=[]  

#Use the function append and an iterator to construct lists to use later in the code
     for column in entirevotepoll:
        VoterID.append(column[0])
        County.append(column[1])   
        Candidate.append(column[2])
     
#Initialize values to extract a lit of Candidates
     voters=len(VoterID)
     CandidateNew=''
     Candidatelist=[]  
    
#iterate over the range of lines in the file looking for unique Candidate names and make a list of them
     for i in range(1,voters):
         CandidateNew=Candidate[i]
         if CandidateNew in Candidatelist:
             pass
         else:
            Candidatelist.append(CandidateNew)

#Initializes vote counts for each candidate
     Votes=[0,0,0,0]

#Calculates the number of points for each candidate by identifying the Candidate and add one vote at a time

     for i in range(1,voters):
        CurrentCandidate=Candidate[i]
        if CurrentCandidate == Candidatelist[0]:
             Votes[0]=Votes[0]+1
        elif CurrentCandidate == Candidatelist[1]:
              Votes[1]=Votes[1]+1
        elif CurrentCandidate == Candidatelist[2]:
              Votes[2]=Votes[2]+1
        else:
              Votes[3]=Votes[3]+1 

#Prints number of votes and list of candidates on the screen
print(f'\nTotal number of votes= {len(VoterID)} \n')
print(f'Candidates: \n {"-"*45}')
print(*Candidatelist, sep='\n')

#Prints the Final vote Analysis
print(f'\n \n Final Vote Tally \n {"-"*40} ')
print(f' Candidate__Votes__ Percent\n {"-"*40} ')
for i in range(0,len(Candidatelist)):
    print(f'{Candidatelist[i]}__{Votes[i]}__{(Votes[i]*100/voters):.2f}%')

#determines the winner using the max() function and identifies its position in the Candidates list
winner=max(Votes)
indexwin=Votes.index(winner)

#Prints the winner on the screen
print(f'\n{"$"*60}')
print(f'The winner is: {Candidatelist[indexwin]}  with {(Votes[indexwin]*100/voters):.2f}% of {voters} votes casted')
print(f'{"$"*60} \n')

#Preparing the text file with the Election results for a ficticious town (La Borracha)
output=os.path.join('Analysis','LaBorracha.txt')
output= open(output,'w') 
output.write('La Borracha State Election Results\n')
output.write(f'\nTotal number of votes= {len(VoterID)} \n')
output.write(f'Candidates: \n {"-"*45} \n')
for i in range(0,len(Candidatelist)):
    output.write(f'{Candidatelist[i]} & ')
output.write(f'\n \n Final Vote Tally \n {"-"*40} \n')
output.write(f' Candidate__Votes__ Percent\n {"-"*40} \n')
for i in range(0,len(Candidatelist)):
    output.write(f'{Candidatelist[i]}__{Votes[i]}__{(Votes[i]*100/voters):.2f}% \n')
output.write(f'\n{"$"*60} \n')
output.write(f'The winner is: {Candidatelist[indexwin]}  with {(Votes[indexwin]*100/voters):.2f}% of {voters} votes casted \n')
output.write(f'{"$"*60} \n')

output.close()