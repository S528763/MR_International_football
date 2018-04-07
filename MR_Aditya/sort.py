#Reading the content of the file
input = open("mapper_OP.txt","r")
output = open("sort_OP.txt","w")

lines = input.readlines()
lines.sort()

for line in lines:
  output.write(line)

input.close()
output.close()