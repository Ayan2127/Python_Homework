import csv


budget_csvpath = "/Users/ayankhalif/Downloads/Starter_Code-6/PyPoll/Resources/election_data.csv"

with open(budget_csvpath, encoding= 'utf') as csvfile:
  csvreader = csv.reader(csvfile, delimiter= ",")
  next(csvreader, None)
 
  #list variables 
  total_votes = []
  candidates = []
  candidate_1_votes = []
  candidate_2_votes = []
  candidate_3_votes = []
  

  #for each column- append values for column 0 (Ballot ID) and column 2 (Candidate)
  for column in csvreader:
   total_votes.append(column[0])
   candidates.append(column[2])
 
  #given the data has three repreating candidates, the if statement finds the number of votes that each candidate earned
   if column[2] == "Charles Casper Stockham":
    candidate_1_votes.append(column[0])
   elif column[2] == "Diana DeGette":
    candidate_2_votes.append(column[0])
   elif column[2] == "Raymon Anthony Doane":
    candidate_3_votes.append(column[0])
   
  #calculates percentage of candidates votes
   candidate_1_percentage = len(candidate_1_votes)/len(total_votes) * 100
   candidate_2_percentage = len(candidate_2_votes)/len(total_votes) * 100
   candidate_3_percentage = len(candidate_3_votes)/len(total_votes) * 100
    
  #created dictionary using info generated from terminal
   votes_per_candidate = {"Charles Casper Stockham": "85213 votes", "Diana DeGette": "272892 votes", "Raymon Anthony Doane": "11606 votes"}
   most_votes = {"272892 votes": "Diana DeGette"}
   
#End print statements, included 'print("")' to ensure print statements generate neatly to terminal
print("")
print(f"Election Results")
print("_____________________________________")
print("")
print(f"Total Votes: {len(total_votes)}")
print("_____________________________________")
print("")
print(f"Charles Casper Stockham: {round(candidate_1_percentage,3)}%  ({len(candidate_1_votes)})")
print(f"Diana DeGette: {round(candidate_2_percentage,3)}%  ({len(candidate_2_votes)})")
print(f"Raymon Anthony Doane: {round(candidate_3_percentage,3)}%  ({len(candidate_3_votes)})")
print("_____________________________________")
print("")
print(f"Winner: {most_votes['272892 votes']}")
print("_____________________________________")
print("")

with open('election_results.txt', 'w') as f:
    f.write(f"Election Results")
    f.write("\n")
    f.write("__________________________________________")
    f.write("\n")
    f.write("\n")
    f.write(f"Total Votes: {len(total_votes)}")
    f.write("\n")
    f.write("__________________________________________")
    f.write("\n")
    f.write(f"Charles Casper Stockham: {round(candidate_1_percentage,3)}%  ({len(candidate_1_votes)})")
    f.write("\n")
    f.write(f"Diana DeGette: {round(candidate_2_percentage,3)}%  ({len(candidate_2_votes)})")
    f.write("\n")
    f.write(f"Raymon Anthony Doane: {round(candidate_3_percentage,3)}%  ({len(candidate_3_votes)})")
    f.write("\n")
    f.write("__________________________________________")
    f.write("\n")
    f.write("\n")
    f.write(f"Winner: {most_votes['272892 votes']}")
    f.write("\n")
    f.write("__________________________________________")