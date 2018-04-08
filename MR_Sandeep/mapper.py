#To read the data from the given data
input = open("../data/results.csv","r")
#To write the mapper output to the file
output = open("mapper_tournament.txt","w")
#For each line in the data clean the data and split it by,
for line in input : 
    datalist = line.strip().split(",")
    date,home_team,away_team,home_score,away_score,tournament,city,country = datalist
    output.write( tournament  + "\n")
#Close the results.csv file
input.close()
#Close the mapper_tournament.txt file
output.close()