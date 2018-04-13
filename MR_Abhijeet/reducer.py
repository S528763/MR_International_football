#Reading the content of the file
s = open("sort_OP.txt","r")
r = open("reducer_OP.txt", "w")
f = open("final_OP.csv", "w")

#initialiastion
thisKey = ""
thisTotalMatches = 0
thisCounter = 0
thisHomeWin = 0
thisHomeDraw = 0
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
  thisTotalMatches += 1
  if int(home_score) == int(away_score):
    thisHomeDraw += 1
  elif int(home_score) > int(away_score):
    thisHomeWin += 1
    thisCounter += 1

# output the final entry when done
r.write(thisKey + '\t' + str(thisCounter)+'\n')
f.write("Matches,Win,Loss,Draw Win\n")
f.write(str(thisTotalMatches)+","+str(thisHomeWin)+","+str(thisTotalMatches - (thisHomeWin + thisHomeDraw))+","+str(thisHomeDraw))
print("Total Number of matches:" +  str(thisTotalMatches))
print("Total win as a Home team :" +  str(thisHomeWin))
print("Total draw as a Home team :" +  str(thisHomeDraw))
print("Total loss as a Home team :" +  str(thisTotalMatches - (thisHomeWin + thisHomeDraw)))

s.close()
r.close()