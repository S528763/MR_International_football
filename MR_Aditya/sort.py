# Aditya Srimat Tirumala Pallerlamudi - S528763

# Reading the content of the data file (mapper_output.txt) into a variable 'unsorted_data'
unsorted_data = open("mapper_output.txt", "r")
# Writing the content to the data file (sorted_output.txt) into a variable 'sorted_data'
sorted_data = open("sorted_output.txt", "w")

# Reading all the lines except the line 1 from the variable 'unsorted_data' to a list i.e. dataList
dataList = unsorted_data.readlines()[1:]
# Sorting the dataList values
dataList.sort()

# For loop that iterates every line in dataList and 
# writes to a data file (sorted_data.txt) through a variable 'sorted_data'
for line in dataList:
    sorted_data.write(line)

# Closing the unsorted_data and sorted_data files
unsorted_data.close()
sorted_data.close()