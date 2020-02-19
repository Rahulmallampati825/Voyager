1.# BD_PROJECT
## Info: 44517 Sec 02 Group:8 
### Participants: Rahul Mallampati, Revanth Davuluri, Sai Samrat Adloori
-Repo_Links: https://github.com/Rahulmallampati825/Voyager
-Issue_Link: https://github.com/Rahulmallampati825/Voyager/issues/3

# Introduction:
        YouTube (the world-famous video sharing website) maintains a list of the top trending videos on the platform.
         According to Variety magazine, “To determine the year’s top-trending videos,
          YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments and likes)

# Data Source:

            Volume: There are 37640 rows with 16 columns and the size of the data set is up to 57MB.

            Variety: The data is structured, it is in CSV format and can interpret using MS Excel.

            Velocity: The data is updated yearly once. Hence, the velocity is slow.

            Veracity: The data is clean, accurate and trustworthy.

            Value: This dataset is helpful in viewing their maximum likes, comments, and views.
            

Big Data Problems:-
question:-  For each Channel_title,find the Average Views.

Solution:-
    Mapper Input:- 
   
   |kzwfHumJyYc|	17.14.11|	Sharry Mann: Cute Munda ( Song Teaser) Parmish Verma  Releasing on 17 November|	Lokdhun Punjabi	1|	2017-11-12T12:20:39.000Z|		1096327|	33966|	798|	882	|	FALSE|	FALSE|	FALSE|

   Mapper Output:- 
                   |1 Kg Biriyani|43202|
                   |1 Minutes news|75888|

   Reducer output:-
                |1kg Biriyani|1057090.034|

    Chart: Bar chart


    






