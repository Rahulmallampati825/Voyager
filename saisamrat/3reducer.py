#  giving input 02.txt which is the output of sortshuffle
s = open("02.txt","r",encoding='utf-8')
# the o/p of reducer is maxdata.txt
r = open("maxdata.csv", "w",encoding='utf-8')

thisKey = ""
thisValue = 0.0

for line in s:
  data = line.strip().split('\t')
  channel_title, likes = data
  #print(line)

  if channel_title != thisKey:
    if thisKey:
      # output the last key value pair result
      r.write(thisKey + ',' + str(thisValue)+'\n')

    # start over when changing keys
    thisKey = channel_title 
    thisValue = 0.0
  
  # apply the aggregation function
  thisValue = max(thisValue,float(likes))

# output the final entry when done
r.write(thisKey + ',' + str(thisValue)+'\n')

s.close()
r.close()