#Reading the content of the file
input = open("../data/results.csv","r")
output = open("mapper_OP.txt","w")
for line in input : 
    datalist = line.strip().split(",")
    date,home_team,away_team,home_score,away_score,tournament,city,country = datalist
    output.write( home_team + "\t" + home_score + "\t" + away_score + "\n")
input.close()
output.close()

home_team,home_score,away_score