s = open("avg1.txt","r",encoding='utf-8')
r = open("avgdata.txt", "w",encoding='utf-8')

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  channel_title, likes = data
  

  if channel_title != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = channel_title 
    thisValue = 0.0
  
  # apply the aggregation function to find Avg likes
    thisValue +=float(likes)


# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()