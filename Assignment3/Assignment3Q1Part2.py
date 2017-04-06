
# coding: utf-8

# **Q1_PART TWO**
# 
# • Use ‘vehicle_collisions’ data set.
# 
# • For each borough, find out distribution of each collision scale. (One car
# involved? Two? Three? or more?) (From 2015 to present)
# 
# • Display a few rows of the output use df.head().
# 
# • Generate a csv output with five columns ('borough', 'one-vehicle', 'twovehicles',
# 'three-vehicles', 'more-vehicles')

# In[6]:

# import necessary packages

from pandas import Series, DataFrame
import pandas as pd
import calendar


# In[7]:

# import the data from csv

vehicle_data=pd.read_csv("Data/vehicle_collisions.csv")
print(vehicle_data.head())


# In[11]:

vehicle_data['DATE']=pd.to_datetime(vehicle_data['DATE']) # convert to datetime
vehicle_range=vehicle_data[vehicle_data['DATE'].isin(pd.date_range("01/01/16","12/31/16"))] #range of dates
vehicle_range['YEAR']=vehicle_range['DATE'].dt.year  # extract year
vehicle_range['MONTH']=vehicle_range.DATE.dt.month # extract month
vehicle_range['MONTH']=vehicle_range['MONTH'].apply(lambda x:calendar.month_abbr[x]) #iterate for every month to convert to abbreviated month name
print(vehicle_range.head())


# In[12]:

borough_group=pd.DataFrame(vehicle_range.groupby(['BOROUGH']).size().reset_index()) # group by Borough
print(borough_group.head())


# In[13]:

borough_group['one-vehicle']=borough_group['BOROUGH'].apply(lambda x: len(vehicle_data[(vehicle_data['BOROUGH']==x)
                 & (vehicle_data['VEHICLE 1 TYPE'].isnull()==False) #condition where only one vehicle is involved
                 & (vehicle_data['VEHICLE 2 TYPE'].isnull()==True)
                 & (vehicle_data['VEHICLE 3 TYPE'].isnull()==True)
                 & (vehicle_data['VEHICLE 4 TYPE'].isnull()==True)
                 & (vehicle_data['VEHICLE 5 TYPE'].isnull()==True)]))

borough_group['two-vehicle']=borough_group['BOROUGH'].apply(lambda x: len(vehicle_data[(vehicle_data['BOROUGH']==x)
                 & (vehicle_data['VEHICLE 1 TYPE'].isnull()==False) #condition where only two vehicles are involved
                 & (vehicle_data['VEHICLE 2 TYPE'].isnull()==False)
                 & (vehicle_data['VEHICLE 3 TYPE'].isnull()==True)
                 & (vehicle_data['VEHICLE 4 TYPE'].isnull()==True)
                 & (vehicle_data['VEHICLE 5 TYPE'].isnull()==True)]))

borough_group['three-vehicle']=borough_group['BOROUGH'].apply(lambda x: len(vehicle_data[(vehicle_data['BOROUGH']==x)
                 & (vehicle_data['VEHICLE 1 TYPE'].isnull()==False) #condition where only three vehicles are involved
                 & (vehicle_data['VEHICLE 2 TYPE'].isnull()==False)
                 & (vehicle_data['VEHICLE 3 TYPE'].isnull()==False)
                 & (vehicle_data['VEHICLE 4 TYPE'].isnull()==True)
                 & (vehicle_data['VEHICLE 5 TYPE'].isnull()==True)]))

borough_group['four-vehicle']=borough_group['BOROUGH'].apply(lambda x: len(vehicle_data[(vehicle_data['BOROUGH']==x)
                 & (vehicle_data['VEHICLE 1 TYPE'].isnull()==False) #condition where only four vehicles are involved
                 & (vehicle_data['VEHICLE 2 TYPE'].isnull()==False)
                 & (vehicle_data['VEHICLE 3 TYPE'].isnull()==False)
                 & (vehicle_data['VEHICLE 4 TYPE'].isnull()==False)
                 & (vehicle_data['VEHICLE 5 TYPE'].isnull()==True)]))

borough_group['five-vehicle']=borough_group['BOROUGH'].apply(lambda x: len(vehicle_data[(vehicle_data['BOROUGH']==x)
                 & (vehicle_data['VEHICLE 1 TYPE'].isnull()==False) #condition where only five vehicles are involved
                 & (vehicle_data['VEHICLE 2 TYPE'].isnull()==False)
                 & (vehicle_data['VEHICLE 3 TYPE'].isnull()==False)
                 & (vehicle_data['VEHICLE 4 TYPE'].isnull()==False)
                 & (vehicle_data['VEHICLE 5 TYPE'].isnull()==False)]))


# In[25]:

print(borough_group)


# In[26]:

borough_group.to_csv("Data/Question1Part2.csv",index=False) #exporting the data to csv

