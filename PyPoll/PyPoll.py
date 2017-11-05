import csv

with open('/Users/sharath/Documents/Professional/Study_Material/Data_Bootcamp/Datacamp/02-Homework/03-Python/Instructions/PyPoll/raw_data/election_data_2.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    voterid = []
    county = []
    candidate = set()
    candidate_Khan = []
    candidate_Correy = []
    candidate_Li = []
    candidate_Tooley = []

    next(csvreader,None)

    for row in csvreader:
        voterid.append(row[0])
        a = len(voterid)
        candidate.add(row[2])
        b = len(candidate)
        
        if row[2] == 'Khan':
            candidate_Khan.append(row[2])
            khan_percent = round(((len(candidate_Khan)/len(voterid))*100),2)

        elif row[2] == 'Correy':
            candidate_Correy.append(row[2])
            Correy_percent = round(((len(candidate_Correy)/len(voterid))*100),2)
        elif row[2] == 'Li':
            candidate_Li.append(row[2])
            Li_percent = round(((len(candidate_Li)/len(voterid))*100),2)
        else: 
            candidate_Tooley.append(row[2])   
            Tooley_percent = round(((len(candidate_Correy)/len(voterid))*100),2)
    
    print("Election Results" + '\n')
    print("-----------------------" + '\n')
    print("Total Votes: " + str(a) + '\n')
    print("Total Candidates: " + str(b) + '\n')
    print("-------------------------" + '\n')
    print("Khan: " + str(khan_percent) + "%" + " (" + str(len(candidate_Khan)) + ")" + '\n')
    print("Correy: " + str(Correy_percent) + "%" + " (" + str(len(candidate_Correy)) + ")" + '\n')
    print("Li: " + str(Li_percent) + "%" + " (" + str(len(candidate_Li)) + ")" + '\n')
    print("O'Tooley: " + str(Tooley_percent) + "%" + " (" + str(len(candidate_Tooley)) + ")" + '\n')
    print("Winner: Khan")

    with open('/Users/sharath/Python-Challenge/PyPoll/outputfile1.txt', 'w') as f:
        f.write("Election Results" + '\n')
        f.write("-----------------------" + '\n')
        f.write("Total Votes: " + str(a) + '\n')
        f.write("Total Candidates: " + str(b) + '\n')
        f.write("-------------------------" + '\n')
        f.write("Khan: " + str(khan_percent) + "%" + " (" + str(len(candidate_Khan)) + ")" + '\n')
        f.write("Correy: " + str(Correy_percent) + "%" + " (" + str(len(candidate_Correy)) + ")" + '\n')
        f.write("Li: " + str(Li_percent) + "%" + " (" + str(len(candidate_Li)) + ")" + '\n')
        f.write("O'Tooley: " + str(Tooley_percent) + "%" + " (" + str(len(candidate_Tooley)) + ")" + '\n')
        f.write("Winner: Khan")