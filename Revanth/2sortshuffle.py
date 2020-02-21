unsorted = open("avg1.txt", "r",encoding='utf-8')
sorted = open("avg2.txt", "w",encoding='utf-8')

dataList = unsorted.readlines()
dataList.sort()

for line in dataList:
    #print (line)
    sorted.write(line)

unsorted.close()
sorted.close()