#### Project Name
## Trending YouTube Video Statistics

#### Course: 
```
BigData-44517
```

#### Project Number
```
Sec 02-8
```

### Team Members
1. Rahul Mallampati
1. Revanth Davuluri
1. Sai Samrat Adloori 
<br/>

#### Link to the repo
https://github.com/Rahulmallampati825/Voyager



#### Issue tracker link
https://github.com/Rahulmallampati825/Voyager/issues/3

## Introduction:
YouTube (the world-famous video sharing website) maintains a list of the top trending videos on the platform.
According to Variety magazine, “To determine the year’s top-trending videos.
YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments and likes)
<br/>

#### Data Source Description
- The provided dataset is Youtube views likes and dislikes.Data is saved in .csv format with text data.
- Some of the key attributes are channel_title, views, likes, dislikes.
- VOLUME:There are 37640 rows with 16 columns and the size of the data set is up to 57MB.The source of the dataset is publicly    available website https://www.kaggle.com/datasnaek/youtube-new/data.
- VARIETY: The data is structured, it is in CSV format and can interpret using MS Excel.
- VELOCITY:The data is updated yearly once. Hence, the velocity is slow.
- VERACITY: The data is clean, accurate and trustworthy.
- VALUE: This dataset is helpful in viewing their maximum likes, comments, and views. 

#### Data :
- Local : [./https://github.com/Rahulmallampati825/Voyager/blob/master/Data/CAvideosfinal.csv ]
- Original : <https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset#IMDb%20movies.csv>


#### Big Data Problems :

- **Max - Sai Samrat Adloori**
- Question : For each channel_title,find the maximum number of likes.
- Solution : 
    1. Mapper Input : n1WpP7iowLc,17.14.11,EminemVEVO,10,2017-11-10T17:00:03.000Z,Eminem|"Walk"|"On"|"Water"|"Aftermath/Shady/Interscope"|"Rap",17158579,787425,43420,125882
    
    2. Mapper Output:
     EminemVEVO	787425
   
      iDubbbzTV	127794
   
      Rudy Mancuso 146035
   
      nigahiga	    132239
    
    3. Reducer input:
      AndresSTyle	4655
    
      AndresSTyle	5521
    
      AndresSTyle	6208

    4. Reducer Output:
      AndresSTyle	 6208.0
    
      Mind Warehouse	 57105.0
    
    5. Chart: Bar Chart:
    
     ![bar_chart]( "bar chart")
   
- **Min - Rahul Mallampati**
- Question : For each channel_title, find the minimum number of views.
- Solution : 
    1. Mapper Input :n1WpP7iowLc,17.14.11,EminemVEVO,10,2017-11-10T17:00:03.000Z,Eminem|"Walk"|"On"|"Water"|"Aftermath/Shady/Interscope"|"Rap",17158579,787425,43420,125882
    
    2. Mapper Output:
      EminemVEVO	       17158579
    
      iDubbbzTV	        1014651
    
      Rudy Mancuso	    3191434
    
    3. Reducer input:
      AndresSTyle	353694
     
      AndresSTyle	456096
     
      AndresSTyle	520401
     
    4. Reducer Output:
      AndresSTyle,353694.0
     
      Mind Warehouse,75065.0
     
      SeekingTheTruth,119011.0

     5.  Chart: Bar Chart:
    
    ![bar_chart](https://github.com/Rahulmallampati825/Voyager/blob/master/Images/minimum%20views.png "bar chart")


- **Count - Revanth Davuluri**
- Question : For each channel_title, find the Average number of likes.
- Solution : 
     1. Mapper Input :n1WpP7iowLc,17.14.11,EminemVEVO,10,2017-11-  10T17:00:03.000Z,Eminem|"Walk"|"On"|"Water"|"Aftermath/Shady/Interscope"|"Rap",17158579,787425,43420,125882
     
    2. Mapper Output:
      EminemVEVO	787425
    
      iDubbbzTV	  127794
    
      Rudy Mancuso 146035
    
    3.Reducer input:
      AndresSTyle	4655
     
      AndresSTyle	5521
     
      AndresSTyle	6208
    4. Reducer Output:
      AndresSTyle	4655.0
     
      Mind Warehouse	11788.0
     
      SeekingTheTruth	3277.0

    5. Chart: Bar Chart:
   ![bar_chart](https://github.com/Rahulmallampati825/Voyager/blob/master/Images/Average%20likes%20.png "bar chart")





