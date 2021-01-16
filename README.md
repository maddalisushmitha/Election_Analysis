# Election_Analysis
## Overview of Election Audit:

Analyzing data received from Colorado Board of employee Tom on congressional election so as to find results as follows

1.Calculating total number of votes casted.  
2.Getting a complete list of candidates and counties who received the votes  
3.Calculating total number of votes received by the candidate and county   
4.Calculating percentage of votes received by the candidate and county   
5.Winning candidate and winning county based on the previous steps  

## Election-Audit Results:

- Total Votes casted in the congressional election 369,711

 ![TV](https://github.com/maddalisushmitha/Election_Analysis/blob/main/Images%20for%20readme/Total_Votes.png)

- Number of votes and the percentage of total votes for each county

### Code:

  #for loop to get the county from the county dictionary.  
  for county_name in county_votes:  
  #Retrieve the county vote count.  
  votes_of_county = county_votes.get(county_name)  
  #Calculate the percentage of votes for the county.  
  vote_of_countypercentage = float(votes_of_county) / float(total_votes) * 100  
   #Print the county results to the terminal.  
  county_results = (  
      f"{county_name}: {vote_of_countypercentage:.1f}% ({votes_of_county:,})\n")  
  print(county_results)  
 
 ![NV](https://github.com/maddalisushmitha/Election_Analysis/blob/main/Images%20for%20readme/County_Votes_and_Percentages.png)
 
- County with largest number of votes: Denver

### Code:

   #if statement to determine the winning county and get its vote count.  
   if (votes_of_county > winning_county_count):   
       winning_county_count = votes_of_county  
       winning_county = county_name  
            
![L](https://github.com/maddalisushmitha/Election_Analysis/blob/main/Images%20for%20readme/Largest_County_Votes.png)

- Number of votes and the percentage of the total votes each candidate received

### Code:

   # Save the final candidate vote count to the text file.  
    for candidate_name in candidate_votes:  
        # Retrieve vote count and percentage  
        votes = candidate_votes.get(candidate_name)  
        vote_percentage = float(votes) / float(total_votes) * 100  
        
![C](https://github.com/maddalisushmitha/Election_Analysis/blob/main/Images%20for%20readme/Candidate_Votes.png)

- Candidate that won the election

### Code

   # Determine winning vote count, winning percentage, and candidate.  
   if (votes > winning_count) and (vote_percentage > winning_percentage):  
       winning_count = votes  
       winning_candidate = candidate_name  
       winning_percentage = vote_percentage  
            
![W](https://github.com/maddalisushmitha/Election_Analysis/blob/main/Images%20for%20readme/Winning_candidate.png)

## Election-Audit Summary:
- This script can be used for an election with
1.  This code can be leveraged for any number of other county elections with different candidates to assess the voting percentage and winning candidate. Code doesn't hard code county or candidate name, so it can be used directly with new data values without modifications to the code.

### Code
# Candidate Options and candidate votes.  
candidate_options = []  
candidate_votes = {}  
#Creating a county list and county votes dictionary to store votes and names of county.  
county_options = []  
county_votes = {}  

2. This code can be even leveraged not just for county level elections but for state, national, presidential elections to understand winning candidate









