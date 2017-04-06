
# coding: utf-8

# **Question2 PART TWO**
# 
# • Use 'employee_compensation' data set.
# 
# • Data contains fiscal and calendar year information. Same employee details exist twice in the dataset. Filter data by calendar year and find average salary (you might have to find average for each of the columns for every employee. Eg. Average of Total Benefits, Average of total compensation etc.) for every employee.
# 
# • Now, find the people whose overtime salary is greater than 5% of salaries (salaries refers to ’Salaries' column)
# 
# • For each ‘Job Family’ these people are associated with, calculate the percentage of total benefits with respect to total compensation (so for each job family you have to calculate average total benefits and average total compensation). Create a new column to hold the percentage value.
# 
# • Display the top 5 Job Families according to this percentage value using df.head().
# 
# • Write the output (jobs and percentage value) to a csv.

# In[2]:

#import libraries
from pandas import Series, DataFrame
import pandas as pd


# In[3]:

# read data from csv
employee_comp=pd.read_csv("Data/employee_compensation.csv")
print(employee_comp.head())


# In[11]:

# check if the year type is Calendar and group by Employee Identifier
print(employee_comp[employee_comp['Year Type']=='Calendar'].groupby(['Employee Identifier']).mean().reset_index().head())


# In[12]:

#check if the Overtime is 5% mpre than Salaries
employee_comp=employee_comp[employee_comp['Overtime']>0.05*employee_comp['Salaries']]
print(employee_comp.head())


# In[27]:

# group by family to calculate the mean
mean_job=pd.DataFrame(employee_comp.groupby(['Job Family']).mean().reset_index())
mean_job['Percent_Total_Benefit']=(mean_job['Total Benefits']/mean_job['Total Compensation'])*100 #calculate the percentage of total benefits over total compensation


# In[30]:

Family_data=mean_job.drop(mean_job.columns[[1,2,3,4,5,6,7,8,9,10,11]],axis=1).head()


# In[31]:

Family_data.to_csv("Data/Question2Part2.csv") # export the data to csv


# In[ ]:



