
# coding: utf-8

# ## Q4_PART ONE 
# - Use ‘movies_awards’ data set.
# 
# - You are supposed to extract data from the awards column in this dataset and split it into several columns. An example is given below. 
# 
# - The awards has details of wins, nominations in general and also wins and nominations in certain categories(e.g. Oscar, BAFTA etc.) 
# 
# - You are supposed to create a win and nominated column (these 2 columns contain total number of wins and nominations) and other columns that extract the number of wins and nominations for each category of award. 
# 
# - If a movie has 2 Oscar nominations and 4 Oscar won, the columns Oscar_Awards_Won should have value 4 and Oscar_Awards_Nominated should have value 2. You should also have a total won and nominated column which aggregates all the awards (won or nominated). 
# 
# - Create two separate columns for each award category (won and nominated). 
# 
# - Write your output to a csv file. (Sample output is given in next page)

# In[181]:

# import the libraries

import pandas as pd
from pandas import DataFrame 
import numpy as np
import re


# In[182]:

#import the data from csv
movies_awards=pd.read_csv('Data/movies_awards.csv',sep=',')
print(movies_awards.head())


# In[183]:

movies_awards_list=movies_awards[['Awards']]
movies_awards_list=movies_awards_list[movies_awards_list['Awards'].isnull()==False] # cleaning the data by removing not nulls
pd.options.mode.chained_assignment = None 


# In[184]:

movies_awards_list['Awards_won']=movies_awards_list['Awards'].apply(lambda x:(re.findall(r"(\d+) win",x))) #matching the string against string "win"
movies_awards_list['Awards_won']=movies_awards_list['Awards_won'].apply(lambda x: [0] if len(x)==0 else x) # assigning the value 0 if length is 0 else the value
movies_awards_list['Awards_won']=movies_awards_list['Awards_won'].apply(lambda x: list(map(int,x))[0]) #mapping the values to integer values


# In[185]:

movies_awards_list['Awards_nominated']=movies_awards_list['Awards'].apply(lambda x:(re.findall(r"(\d+) nom",x)))  #matching the string against string "nom"
movies_awards_list['Awards_nominated']=movies_awards_list['Awards_nominated'].apply(lambda x: [0] if len(x)==0 else x) # assigning the value 0 if length is 0 else the value
movies_awards_list['Awards_nominated']=movies_awards_list['Awards_nominated'].apply(lambda x: list(map(int,x))[0]) #mapping the values to integer values


# In[186]:

movies_awards_list['Oscar_Awards_won']=movies_awards_list['Awards'].apply(lambda x:(re.findall(r"Won (\d+) Oscar",x)))  #matching the string against string "Oscar"
movies_awards_list['Oscar_Awards_won']=movies_awards_list['Oscar_Awards_won'].apply(lambda x: [0] if len(x)==0 else x)# assigning the value 0 if length is 0 else the value
movies_awards_list['Oscar_Awards_won']=movies_awards_list['Oscar_Awards_won'].apply(lambda x: list(map(int,x))[0]) #mapping the values to integer values


# In[187]:

movies_awards_list['Oscar_Awards_nominated']=movies_awards_list['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) Oscar', x))) #matching the string against string "Oscar"
movies_awards_list['Oscar_Awards_nominated']=movies_awards_list['Oscar_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x) # assigning the value 0 if length is 0 else the value
movies_awards_list['Oscar_Awards_nominated']=movies_awards_list['Oscar_Awards_nominated'].apply(lambda x : list(map(int,x))[0])#mapping the values to integer values


# In[188]:

movies_awards_list['Golden_Globe_Awards_won']=movies_awards_list['Awards'].apply(lambda x:(re.findall(r'Won (\d+) Golden',x))) #matching the string against string "Golden"
movies_awards_list['Golden_Globe_Awards_won']=movies_awards_list['Golden_Globe_Awards_won'].apply(lambda x: [0] if len(x)==0 else x) # assigning the value 0 if length is 0 else the value
movies_awards_list['Golden_Globe_Awards_won']=movies_awards_list['Golden_Globe_Awards_won'].apply(lambda x: list(map(int,x))[0]) #mapping the values to integer values


# In[189]:

movies_awards_list['Golden_Globe_Awards_nominated']=movies_awards_list['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) Golden', x))) #matching the string against string "Golden"
movies_awards_list['Golden_Globe_Awards_nominated']=movies_awards_list['Golden_Globe_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)# assigning the value 0 if length is 0 else the value
movies_awards_list['Golden_Globe_Awards_nominated']=movies_awards_list['Golden_Globe_Awards_nominated'].apply(lambda x : list(map(int,x))[0]) #mapping the values to integer values


# In[190]:

movies_awards_list['Prime_Emmys_Awards_won']=movies_awards_list['Awards'].apply(lambda x : (re.findall(r'Won (\d+) Prime', x))) #matching the string against string "Prime"
movies_awards_list['Prime_Emmys_Awards_won']=movies_awards_list['Prime_Emmys_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)# assigning the value 0 if length is 0 else the value
movies_awards_list['Prime_Emmys_Awards_won']=movies_awards_list['Prime_Emmys_Awards_won'].apply(lambda x : list(map(int,x))[0]) #mapping the values to integer values


# In[191]:

movies_awards_list['Prime_Emmys_Awards_nominated']=movies_awards_list['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) Prime', x))) #matching the string against string "Prime"
movies_awards_list['Prime_Emmys_Awards_nominated']=movies_awards_list['Prime_Emmys_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)# assigning the value 0 if length is 0 else the value
movies_awards_list['Prime_Emmys_Awards_nominated']=movies_awards_list['Prime_Emmys_Awards_nominated'].apply(lambda x : list(map(int,x))[0]) #mapping the values to integer values


# In[192]:

movies_awards_list['BAFTA_Awards_won']=movies_awards_list['Awards'].apply(lambda x : (re.findall(r'Won (\d+) BAFTA', x))) #matching the string against string "BAFTA"
movies_awards_list['BAFTA_Awards_won']=movies_awards_list['BAFTA_Awards_won'].apply(lambda x : [0] if len(x)==0 else x)# assigning the value 0 if length is 0 else the value
movies_awards_list['BAFTA_Awards_won']=movies_awards_list['BAFTA_Awards_won'].apply(lambda x : list(map(int,x))[0]) #mapping the values to integer values


# In[193]:

movies_awards_list['BAFTA_Awards_nominated']=movies_awards_list['Awards'].apply(lambda x : (re.findall(r'Nominated for (\d+) BAFTA', x))) #matching the string against string "BAFTA"
movies_awards_list['BAFTA_Awards_nominated']=movies_awards_list['BAFTA_Awards_nominated'].apply(lambda x : [0] if len(x)==0 else x)# assigning the value 0 if length is 0 else the value
movies_awards_list['BAFTA_Awards_nominated']=movies_awards_list['BAFTA_Awards_nominated'].apply(lambda x : list(map(int,x))[0]) #mapping the values to integer values


# In[194]:

# total nominated and won awards
movies_awards_list['Awards_nominated']=movies_awards_list['Awards_nominated']+movies_awards_list['Oscar_Awards_nominated']+movies_awards_list['Golden_Globe_Awards_nominated']+movies_awards_list['Prime_Emmys_Awards_nominated']+movies_awards_list['BAFTA_Awards_nominated']
movies_awards_list['Awards_won']=movies_awards_list['Awards_won']+movies_awards_list['Oscar_Awards_won']+movies_awards_list['Golden_Globe_Awards_won']+movies_awards_list['Prime_Emmys_Awards_won']+movies_awards_list['BAFTA_Awards_won']


# In[196]:

print(movies_awards_list.head())


# In[180]:

movies_awards_list.to_csv("Data/Question4.csv")

