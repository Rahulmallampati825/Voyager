s = open("min2.txt","r",encoding='utf-8')
r = open("minoutput.csv","w",encoding='utf-8')

thisKey = ""
thisValue = 9999999.0

for line in s:
  data = line.strip().split('\t')
  channel_title, views = data
 

  if channel_title != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + ',' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = channel_title 
    thisValue = 9999999.0
  
  # apply the aggregation function
  
  thisValue = min(thisValue,float(views))

# output the final entry when done
r.write(thisKey + ',' + str(thisValue)+'\n')

s.close()
r.close()