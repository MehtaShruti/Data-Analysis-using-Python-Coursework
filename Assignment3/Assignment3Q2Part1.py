
# coding: utf-8

# **Question 2 PART ONE**
# 
# • Use 'employee_compensation' data set.
# 
# • Find out the highest paid departments in each organization group by
# calculating mean of total compensation for every department.
# 
# • Output should contain the organization group and the departments in
# each organization group with the total compensation from highest to
# lowest value.
# 
# • Display a few rows of the output use df.head().
# 
# • Generate a csv output.

# In[2]:

# importing necessary libraries

from pandas import Series, DataFrame
import pandas as pd


# In[5]:

# importing the data from csv

employee_comp=pd.read_csv("Data/employee_compensation.csv")
print(employee_comp.head())


# In[6]:

# grouping the data on the basis of the ORganization Group and department and then calculating the mean of the total compensation
grouped=pd.DataFrame(employee_comp.groupby(['Organization Group','Department'])['Total Compensation'].agg(['mean']))
reset_group=grouped.reset_index() #reset the index of the data 
#apply the groupby operation again on the data and then sort the values
final_sorted_group=reset_group.groupby(['Organization Group']).apply(lambda reset_group: reset_group.sort_values(['mean'],ascending=False))


# In[7]:

print(final_sorted_group.head())


# In[13]:

final_sorted_group.to_csv("Data/Question2Part1.csv") #export to csv


# In[ ]:



