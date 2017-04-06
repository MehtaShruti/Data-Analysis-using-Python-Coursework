
# coding: utf-8

# # Assignment 3

# **Q1_PART ONE**
# 
# • Use ‘vehicle_collisions’ data set.
# 
# • For each month in 2016, find out the percentage of collisions in
# Manhattan out of that year's total accidents in New York City.
# 
# • Display a few rows of the output use df.head().
# 
# • Generate a csv output with four columns (‘Month’, ‘Manhattan’, ‘NYC’, ‘Percentage’)

# In[12]:

# import the libraries 

from pandas import Series, DataFrame
import pandas as pd
import calendar


# In[13]:

# read the data from the csv

vehicle_data=pd.read_csv("Data/vehicle_collisions.csv")
print(vehicle_data.head())


# In[14]:

vehicle_data['DATE']=pd.to_datetime(vehicle_data['DATE'])  # convert the Date to datetime
vehicle_range=vehicle_data[vehicle_data['DATE'].isin(pd.date_range("01/01/16","12/31/16"))] # a range of dates, in which date lies 
vehicle_range['YEAR']=vehicle_range['DATE'].dt.year #extract year
vehicle_range['MONTH']=vehicle_range.DATE.dt.month # extract month
vehicle_range['MONTH']=vehicle_range['MONTH'].apply(lambda x:calendar.month_abbr[x]) # for every row abbreviate the month's name
print(vehicle_range.head())


# In[5]:

vehicle_man=vehicle_range[vehicle_range.BOROUGH=='MANHATTAN']# check if the Borough name is Manhattan
count_man=vehicle_man['BOROUGH'].value_counts().reset_index(drop=True)
vcount=pd.DataFrame(vehicle_man.groupby(['MONTH']).size().reset_index()) #group by name of manhattan
vcount.columns=['MONTH','MANNHATTAN']
print(vcount)


# In[6]:

count_nyc=vehicle_range['BOROUGH'].value_counts().reset_index(drop=True) # reset the index
nyccount=pd.DataFrame(vehicle_range.groupby(['MONTH']).size().reset_index()) # groupby the name of the month
nyccount.columns=['MONTH','NYC']# combine the column names
print(nyccount)


# In[15]:

frame=pd.merge(vcount,nyccount) # merge the column names
frame
frame['PERCENTAGE']=(frame['MANNHATTAN']/frame['NYC'])*100 #calculate the percentage of the accidents in Manhattan over NYC
frame.to_csv('Data/Question1Part1.csv',index=False) # export to CSV

