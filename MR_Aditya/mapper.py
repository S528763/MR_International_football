# Aditya Srimat Tirumala Pallerlamudi - S528763

# Reading the content of the file
input = open("../data/results.csv","r")
mapper_output = open("mapper_OP.txt","w")

# Splitting data against columns and adding to list
for line in input:
    datalist = line.strip().split(",")
    date,home_team,away_team,home_score,away_score,tournament,city,country = datalist
    mapper_output.write( date[:4] + "," + home_team + "," + away_team + "\n")

# Closing the files
input.close()
mapper_output.close()