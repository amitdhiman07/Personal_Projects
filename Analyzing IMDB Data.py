#!/usr/bin/env python
# coding: utf-8

# # Analyzing IMDb Data
# 

# ### Let's start with basic level

# In[1]:


# importing the necessary libraries

import pandas as pd 
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# ### Reading the IMDb file and store it into a variable called "movies"

# In[4]:


movies = pd.read_csv(r"C:\Users\Amit\Desktop\random/imdb_clean.csv")
movies.head()


# ### Checking the shape of the dataset

# In[5]:


movies.shape


# ### Checking the data types

# In[6]:


movies.dtypes


# ### Calculate the average movie duration

# In[14]:


# str.extract('(\d+)') method used to extract the numeric digits.
movies["duration"] = movies["runtime"].str.extract('(\d+)').astype(int)
print(movies["duration"])


# In[16]:


movies["duration"].mean()


# ### Sort the DataFrame by duration to find out the shortest and longest movies

# In[60]:


display_cols = ["title","duration"]
movies_sorted = movies.sort_values("duration",ascending=False)

movies_uni_dur = movies_sorted['duration'].unique()
movies_uni_title = movies_sorted['title'].unique()

# Checking the length of my array

print(f"The length of movies_uni_title array is : {len(movies_uni_title)}")
print("The length of movies_uni_dur array is : " ,len(movies_uni_dur))

print("------------------------")
table = [movies_uni_title , movies_uni_dur]

table_data = pd.Series(table , index= ["Title" , "Duration"])
print(table_data)
print("------------------------")

print("Longest")
print(movies_sorted[display_cols].iloc[:10])

print("------------------------")
print("Shortest")
print(movies_sorted[display_cols].iloc[-10:])


# ### Create a histogram of duration

# In[70]:


ax = movies.loc[:,'duration'].plot.hist(bins = 30)


# In[67]:


movies.duration.plot(kind="box" , figsize = (10,10))


# In[66]:


# Checking how many movies are outliers

movies.describe()


# In[71]:


movies[movies.duration > 200].title.value_counts().sum()


# ### Intermediate Level

# ### Counting different genres.

# In[77]:


total = movies.genre.value_counts()


# ### Displaying that same data 

# In[78]:


p = total.plot.bar()
p.set(title="Number of movies per genre",xlabel="genre", ylabel="Number of movies")
p.legend(loc="upper right");


# ### Count the number of missing values in each columns

# In[79]:


movies.info()


# In[80]:


movies.apply(pd.isnull).sum()


# In[82]:


# OR
movies.isnull().sum()


# ### Calculate the average rating for the movies 2 hours or longer and compare that with the average rating for the movies shorter than 2 hours

# In[86]:


avg_movie_rating_longer = movies[movies.loc[:,'duration'] >= 120].rating.mean()
avg_movie_rating_longer 


# In[87]:


avg_movie_rating_shorter = movies[movies.loc[:,"duration"] < 120].rating.mean()
avg_movie_rating_shorter


# In[88]:


print(f"The average rating for the movies 2 hours or longer ({avg_movie_rating_longer}) greater than the average rating for the movies shorter than 2 hours which is {avg_movie_rating_shorter}")


# ### Using visualization to detect whether there is a relationship between duration and rating

# In[90]:


ax = movies.plot.scatter(x = "rating" ,
                         y ="duration" ,
                         figsize=(10,4), 
                         c= "red" ,
                         s=100)


# ##### The graph shows no pattern between points. Therefore, there is no correlation 

# ### Calculate the average duration for each genre

# In[93]:


movies.groupby('genre')['duration'].mean().sort_values(ascending=False)


# ### Advanced Level

# In[94]:


movies.loc[:,'duration'].hist(by=movies.loc[:,"genre"],sharex=True)


# ### Finding the title of the movie with the highest rating in each genre

# In[97]:


movies.sort_values("rating" , ascending=False).groupby('genre').title.first().head(20)


# ### Check if there are multiple movies with the same title.
# 

# In[98]:


movies.head(15)


# ### Calculate the average rating for each genre, but only include genres with at least 10 movies

# In[101]:


rating_genre = movies.groupby('genre').rating.agg(['count','mean'])
genre_rating = rating_genre["count"] >= 10


# In[103]:


final_rating = rating_genre[genre_rating]


# In[104]:


final_rating


# In[ ]:




