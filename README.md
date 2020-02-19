1.# Voyager
## Info: 44517 Sec 02 Group:8 
### Participants: Rahul Mallampati, Revanth Davuluri, Sai Samrat Adloori
-Repo_Links: https://github.com/Rahulmallampati825/Voyager
-Issue_Link: https://github.com/Rahulmallampati825/Voyager/issues/3

# Introduction
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
 2. question: For each channel_title,find the Maximum Views
    Solution:-
    Mapper Input:-
	
    pA0MdlTcBH0	17.10.12	INDIA vs HINDIA | 1 Kg Biriyani	1 Kg Biriyani	23	2017-12-09T07:20:41.000Z		55961	4285	432	341		FALSE	FALSE	FALSE	

    Mapper Output:- Lokdhun Punjabi	1		1096327

    Reducer Output:	Lokdhun Punjabi	1		1096327

    Chart: Bar chart

    3. question: For each channel_title,find the Minimum Views
 Solution:-
 Mapper Input:-

|7V6Z1uh3sqg|	17.16.11|	The startup | 1 Kg Biriyani | TVF Machi	1 Kg Biriyani|	23	|2017-11-15T11:32:04.000Z|		43202|	2755	|184	|165	|	FALSE	|FALSE|	FALSE|	
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|


  Mapper Output:- 
  |1kg Biriyani|43202|

    Reducer Output:	
    |1kg Biriyani|4024|

    Chart: Bar chart


    






