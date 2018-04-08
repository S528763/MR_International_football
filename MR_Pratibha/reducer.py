# Taking input file sorted.txt in read mode and taking the contents into variable sorted
sorted = open("sorted.txt", "r")

# Taking output file final_output.txt in write mode and taking the contents into variable sortcateg
sortcateg = open("final_output.txt", "w")

# Initializing key-value pairs to null and zero
thisKey = None
num_draws = 0

# Reading the lines in sorted and storing it into variable data
data = sorted.readlines()

# For each line in data we are cleaning the data with tab space as delimiter
for line in data:
    listOfData = line.strip().split("\t")
    
# Storing the cleaned data year, home_score,away_score into listOfData    
    year, home_score, away_score = listOfData

# 
    if thisKey and thisKey != year:
        sortcateg.write("Year: " + thisKey + "\t Draw matches: " + str(num_draws) + "\n")
        thisKey = year;
        num_draws = 0

    thisKey = year
    num_draws += 1
    
if thisKey != None:
    sortcateg.write("Year: " + thisKey + "\t Draw matches: " + str(num_draws) + "\n")

# Close the input file
sorted.close()
# Close the output file
sortcateg.close()