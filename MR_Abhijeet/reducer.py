s = open("sort_OP.txt","r")
r = open("reducer_OP.txt", "w")

thisKey = ""
thisCounter = 0

for line in s:
  data = line.strip().split('\t')
  home_team,home_score,away_score = data

  if home_team != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisCounter)+'\n')

    # start over when changing keys
    thisKey = home_team 
    thisCounter = 0
  
  # apply the aggregation function
  if home_score > away_score:
    thisCounter += 1

# output the final entry when done
r.write(thisKey + '\t' + str(thisCounter)+'\n')

s.close()
r.close()