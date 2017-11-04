import csv
import sys

with open('/Users/sharath/Documents/Professional/Study_Material/Data_Bootcamp/Datacamp/02-Homework/03-Python/Instructions/PyBank/raw_data/budget_data_1.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
   



    months = []
    Revenue = []
    change = []
    Total = 0

    next(csvreader,None)
    
    for row in csvreader:
        months.append(row[0])
        Revenue.append(int(row[1]))

        Total += int(row[1])

    

    for j in range(1,len(Revenue)):
        change.append(Revenue[j] - Revenue[j-1])
        a = sum(change)
        avg_change = sum(change)/len(change)

        max_change = max(change)
        Max_date = months[change.index(max(change))]
        min_change = min(change)
        min_date = months[change.index(min(change))]
        
    print("Financial Analysis" + '\n')
    print("-----------------------------" + '\n')
    print("Total months:" + " " + str(len(months)) + '\n')
    print("Total Revenue: $" + str(Total) + '\n')    
    print("Average Revenue Change: $" + str(avg_change) + '\n')
    print("Greatest increase in Revenue: " + str(Max_date) + " ($" + str(max_change) + ")" + '\n' )
    print("Greatest decrease in Revenue: " + str(min_date) + " ($" + str(min_change) + ")" + '\n')

    with open('/Users/sharath/Python-Challenge/PyName/outputfile.txt', 'w') as f:
       
        f.write("Financial Analysis" + '\n')
        f.write("-----------------------------" + '\n')
        f.write("Total months:" + " " + str(len(months)) + '\n')
        f.write("Total Revenue: $" + str(Total) + '\n')    
        f.write("Average Revenue Change: $" + str(avg_change) + '\n')
        f.write("Greatest increase in Revenue: " + str(Max_date) + " ($" + str(max_change) + ")" + '\n' )
        f.write("Greatest decrease in Revenue: " + str(min_date) + " ($" + str(min_change) + ")" + '\n')
    



