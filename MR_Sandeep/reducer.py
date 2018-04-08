#To read the data from the sort output(i.e sort_tournament.txt)
s = open("sort_tournament.txt","r")
#To write the reducer output to the reducer_tournament.txt file
r = open("reducer_tournament.txt", "w")
#Initilizing thiskey to null
thisKey = ""
#Initilizing thisCounter to 0
thisCounter = 0

for line in s:
    data = line.strip()
    tournament=data
# If the line in the sort_tournament.txt is not null it enters the loop
    if tournament != thisKey: 
# If the key is a unique one then enter the loop   
        if thisKey:
            r.write(thisKey + '\t' + str(thisCounter)+'\n')
# Set thisKey to the present value
        thisKey = tournament
# Set the counter to 0
        thisCounter = 0
# If thisKey is not unique increase the counter by 1(Bascilly counts the number of tournments)
    thisCounter += 1
# Write the key value pair to the reducer output file         
r.write(thisKey + '\t' + str(thisCounter)+'\n')
#Close the sort_tournament.txt file
s.close()
#Close the reducer_tournament.txt file
r.close()