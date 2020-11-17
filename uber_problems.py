# Q1
# On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file. Write a program that reads this file as a stream and 
# returns the top 3 candidates at any given time. If you find a voter voting more than once, report this as fraud.

# I decided to use dictionary to store the candidate ID and the count of it. Of course, we need to make sure that there is no fraud, so I initialized an
# array to keep track of the voters ID. If there is duplicate in terms of voting ID, the program will detect it as a fraud and exits the program
counts = dict()
check_voters = []

while True:
    vote_id = input("Enter the voters ID: /Type 'quit' to exit\n")
    if vote_id == "quit":
        break
    
    if not vote_id in check_voters:
        check_voters.append(vote_id)
        print("This voter ID is valid")

    else:
        print("There might be fraudulent activity here!")
        break
        
    candidate_id = input("Enter the candidate ID:")
    
    counts[candidate_id] = counts.get(candidate_id, 0) + 1
    sorted_voted = sorted(counts.items(), key=lambda x:-x[1])[:3]
    
    print("The top 3 candidates currently are:")
    for key, value in sorted_voted:
        print (key)



