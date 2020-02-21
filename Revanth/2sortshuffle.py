unsorted = open("avg1.txt", "r",encoding='utf-8')
# mapper contents to avg2.txt folder
sorted = open("avg2.txt", "w",encoding='utf-8')

dataList = unsorted.readlines()
# sorted list of mapper
dataList.sort()

for line in dataList:
    #print (line)
    sorted.write(line)

unsorted.close()
sorted.close()