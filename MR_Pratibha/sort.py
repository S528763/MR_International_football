# Taking the output file in mapper(unsorted data) in read mode 
unsorted = open("int_output.txt", "r")
# Taking the sorted data in write mode into variable named sorted
sorted = open("sorted.txt", "w")

# Reading all lines in unsorted into variable dataList and sorting it
dataList = unsorted.readlines()
dataList.sort()

# For each line in dataList print the line  and write the line in the output sorted
for line in dataList:
    print line
    sorted.write(line)

# Close unsorted and sorted files
unsorted.close()
sorted.close()