#Reading the content of the file
input = open("../data/results.csv","r")
output = open("mapper_OP.txt","w")

#Loop
for line in input : 
    datalist = line.strip().split(",")
    #Assigning the data object to resp keys
    date,home_team,away_team,home_score,away_score,tournament,city,country = datalist
    #writing required fields to output dir
    output.write( home_team + "," + home_score + "," + away_score + "\n")

#Close the opened files
input.close()
output.close()
