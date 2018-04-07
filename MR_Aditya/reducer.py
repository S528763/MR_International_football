s = open("sort_OP.txt","r")
r = open("reducer_OP.txt", "w")

thisKey = ""
thisCounter = 0
collection = {}
for line in s:
  data = line.strip().split(',')
  year,home_team,away_team = data

  if collection.has_key(str(year)) != True:
    collection[str(year)] = {}
  
  if collection[str(year)].has_key(home_team) != True:
    collection[str(year)][home_team] = 1
  else:
    collection[str(year)][home_team] += 1
  
  if collection[str(year)].has_key(away_team) != True:
    collection[str(year)][away_team] = 1
  else:
    collection[str(year)][away_team] += 1

    
# output the final entry when done
for line in collection:
  r.write("For year "+ str(line)+"\n")
  for temp in collection[line]:
    r.write("Team: " + temp + "\tMatches: " + str(collection[line][temp])+"\n")

s.close()
r.close()