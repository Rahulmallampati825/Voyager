1.# BD_PROJECT
# Info: 44517 Sec 02 Group:8 
# Participants: Rahul Mallampati, Revanth Davuluri, Sai Samrat Adloori
Repo_Links: https://github.com/Rahulmallampati825/Voyager
Issue_Link: https://github.com/Rahulmallampati825/Voyager/issues/3

Big Data Problems:-
question:-  For each Channel_title,find the Average Views.

Solution:-
    Mapper Input:- |video_id|	trending_date|	title|channel_title|	category_id	publish_time|		views|	likes|	dislikes|	comment_count	|	comments_disabled|	ratings_disabled	|video_error_or_removed|
   |--------|----------|--------|--------|----------|------|--------|------|---------|--------|---------|------|
   |kzwfHumJyYc|	17.14.11|	Sharry Mann: Cute Munda ( Song Teaser) Parmish Verma  Releasing on 17 November|	Lokdhun Punjabi	1|	2017-11-12T12:20:39.000Z|		1096327|	33966|	798|	882	|	FALSE|	FALSE|	FALSE|

   Mapper Output:-|channel_title|views|
                   |-----------|------|
                   |1 Kg Biriyani|43202|
                   |1 Minutes news|75888|

   Reducer output:-|channel_title| avg|
                |---------|----------|
                |1kg Biriyani|1057090.034|

    Chart: Bar chart




