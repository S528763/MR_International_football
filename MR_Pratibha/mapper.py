# Taking input file results.csv in read mode and taking the contents into variable custom_input
custom_input = open("results.csv", "r")

# Taking output file int_output.txt in write mode and taking the contents into variable output
output = open("int_output.txt", "w")

# Reading every line in custom_input and splitting the data with delimiter ","
# Trimed data is stored in listOfData 
for line in custom_input:
    listOfData = line.strip().split(",")

# length of listOfData is equal to 8 then take the contents into listOfData      
    if len(listOfData) == 8:
        date,home_team,away_team,home_score,away_score,tournament,city,country = listOfData
# If home_score is equal to away_score then write it to output file "output"        
        if home_score == away_score:
            output.write(date.split("-")[0] + "\t" + home_score + "\t" + away_score + "\n")

# Close the input file
custom_input.close()
# Close the output file
output.close()