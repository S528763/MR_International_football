s = open("sort_OP.txt","r")
r = open("reducer_OP.txt", "w")

thisKey = ""
thisCounter = 0
thisHomeWin = 0
for line in s:
  data = line.strip().split(',')
  home_team,home_score,away_score = data

  if home_team != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisCounter)+'\n')

    # start over when changing keys
    thisKey = home_team 
    thisCounter = 0
  
  # apply the aggregation function
  if int(home_score) > int(away_score):
    thisHomeWin += 1
    thisCounter += 1

# output the final entry when done
r.write(thisKey + '\t' + str(thisCounter)+'\n')
print("Totl win as a Home team :" +  str(thisHomeWin))

s.close()
r.close()