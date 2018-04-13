# Aditya Srimat Tirumala Pallerlamudi - S528763

# Reading the content of the file
input = open("mapper_OP.txt","r")
output = open("sort_OP.txt","w")

lines = input.readlines()

# Sorting the lines
lines.sort()

# Writing the lines to file
for line in lines:
  output.write(line)

# Closing the files
input.close()
output.close()