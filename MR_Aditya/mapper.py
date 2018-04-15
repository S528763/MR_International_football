# Aditya Srimat Tirumala Pallerlamudi - S528763

# Reading the content of the data file (results.csv) stored in data folder into a variable 'mapper_input'
mapper_input = open("../data/results.csv", "r")
# Writing the content to the data file (mapper_output.txt) through a variable 'mapper_output'
mapper_output = open("mapper_output.txt", "w")

# Splitting the data against columns with a comma(,) and adding to a list i.e. datalist
for line in mapper_input:
    datalist = line.strip().split(",")
    
    # Checking the length of the datalist, if it is true then assigning the attributes to the datalist
    if len(datalist) == 8:
        date,home_team,away_team,home_score,away_score,tournament,city,country = datalist
        # Writing the intermediate key-value pairs to the output file (mapper_output.txt)
        mapper_output.write(home_team + "\n")

# Closing the mapper_input and mapper_output files
mapper_input.close()
mapper_output.close()