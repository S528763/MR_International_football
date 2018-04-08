#Reading the content of the file
input = open("mapper_OP.txt","r")
output = open("sort_OP.txt","w")

lines = input.readlines()
#sort record
lines.sort()
#Loop
for line in lines:
  output.write(line)

#Close opened files
input.close()
output.close()