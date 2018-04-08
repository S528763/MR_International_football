#Reading the content of the file(i.e mapperoutput)
input = open("mapper_tournament.txt","r")
#Write the sorted output to sort_tournament.txt file
output = open("sort_tournament.txt","w")
# Read all the lines from the mapper output(i.e. mapper_tournament.txt)
lines = input.readlines()
# Does natural sort
lines.sort()

for line in lines:
# Writes each sorted line into the sort_tournament.txt file
  output.write(line)
#Close the mapper_tournament.txt file
input.close()
#Close the sort_tournament.txt file
output.close()