input = open("data.txt", "r",encoding='utf-8')
output = open("01.txt", "w",encoding='utf-8')

for line in input:
    datalist = line.strip().split("\t")
    video_id,trending_date,channel_title,category_id,publish_time,tags,views,likes,dislikes,comment_count = datalist
    output.write(channel_title + "\t" + likes + "\n")

input.close()
output.close()