#  Implenenting mapper to find avg likes
input = open("data.txt", "r",encoding='utf-8')
# cpoy the result to avg1
output = open("avg1.txt", "w",encoding='utf-8')

for line in input:
    datalist = line.strip().split("\t")
    video_id,trending_date,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count = datalist
    output.write(channel_title + "\t" + likes + "\n")

input.close()
output.close()