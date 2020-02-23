s = open("min2.txt","r",encoding='utf-8')
r = open("minoutput.txt","w",encoding='utf-8')

thisKey = ""
thisValue = 9999999.0

for line in s:
  data = line.strip().split('\t')
<<<<<<< HEAD:Rahul/3reducer.py
  channel_title, views = data
 
=======
  channel_title, likes = data
  #print(line)
>>>>>>> 893778d8b9d8a854bc562307d2643136e765fdff:saisamrat/3reducer.py

  if channel_title != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + '\t' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = channel_title 
    thisValue = 9999999.0
  
  # apply the aggregation function
  
  thisValue = min(thisValue,float(views))

# output the final entry when done
r.write(thisKey + '\t' + str(thisValue)+'\n')

s.close()
r.close()