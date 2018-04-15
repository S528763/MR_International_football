# Aditya Srimat Tirumala Pallerlamudi - S528763

# Reading the content of the data file (sorted_output.txt) into a variable 'sorted'
sorted = open("sorted_output.txt", "r")
# Writing the content to the data file (final_output.txt) through a variable 'final_output'
final_output = open("final_output.txt", "w")
# Writing the content to the data file (csv_output.csv) through a variable 'csv_output' in a csv format
csv_output = open("csv_output.csv", "w")

# Creating a variable 'thisKey' for iterating keys in key-value pairs
thisKey = None
# Creating a variable 'count' for counting the matches
count = 0

# Reading all the lines from the variable 'sorted' to a list i.e. data
data = sorted.readlines()

# Writing headers for the data to the file 'csv_output'
csv_output.write("Home Team,Matches played\n")

# For loop that iterates every line in data
for line in data:
    datalist = line.strip()
    
    # Assigning the required attribute 'home_team' to the datalist
    home_team = datalist
    # Writing the result to a file if the key is not already present in the output
    if thisKey and thisKey != home_team:
        final_output.write("Home Team: " + thisKey + ", Matches played: " + str(count) + "\n")
        
        # Writing the result to a specific output file for csv format
        csv_output.write(thisKey + "," + str(count) + "\n")
        # modifying the thisKey value as per the iteration
        thisKey = home_team;
        count = 0

    thisKey = home_team
    # Increasing the count variable to get the total number of matches
    count += 1
    
# Writing the result to the files if the key is not null
if thisKey != None:
    final_output.write("Home Team: " + thisKey + ", Matches played: " + str(count) + "\n")
    csv_output.write(thisKey + "," + str(count) + "\n")

# Closing the sorted, final_output and csv_output files
sorted.close()
final_output.close()
csv_output.close()