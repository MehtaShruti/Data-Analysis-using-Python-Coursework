
# coding: utf-8

# **Question 3 **
# 
# • Use ‘cricket_matches’ data set.
# 
# • Calculate the average score for each team which host the game and win the game.
# 
# • Remember that if a team hosts a game and wins the game, their score can be innings_1 runs or innings_2 runs. You have to check if the host team won the game, check which innings they played in (innings_1 or innings_2), and take the runs scored in that innings. The final answer is the average score of each team satisfying the above condition.
# 
# • Display a few rows of the output use df.head()
# 
# • Generate a csv output
# 

# In[2]:

# import packages

from pandas import Series, DataFrame
import pandas as pd


# In[4]:

# import data from csv

cricket_matches=pd.read_csv("Data/cricket_matches.csv")
print(cricket_matches.head())


# In[8]:

# checking if the home team is same as the winning team
cricket_matches=cricket_matches[cricket_matches.home==cricket_matches.winner]
cricket_matches_gp=pd.DataFrame(cricket_matches.groupby('home').size().reset_index()) # group by home team
cricket_matches_gp.columns=['home','count'] # making names of the columns
print(cricket_matches_gp.head())


# In[17]:

# summing the innings of the team which played in the first inning
winners_first_inning=cricket_matches.groupby('home').apply(lambda x: x[x['home']==x['innings1']]['innings1_runs'].sum())
winners_first_inning
# summing the innings of the team which played in the second inning
winners_second_inning=cricket_matches.groupby('home').apply(lambda x: x[x['home']==x['innings2']]['innings2_runs'].sum())
print(winners_second_inning.head())


# In[20]:

#winners_innings is the sum of first and second inning
winners_innings=winners_first_inning+winners_second_inning
print(winners_innings.head())


# In[21]:

# reset the index of the innings of the winners
winners_innings=pd.DataFrame(winners_innings.reset_index())
winners_innings.columns=['home','Total Score']# combining the columns 
print(winners_innings.head())


# In[24]:

scores_innings=pd.merge(cricket_matches_gp,winners_innings) #merge the columns
scores_innings['Avg Score']=(scores_innings['Total Score']/scores_innings['count'])#calculating the average score
print(scores_innings.head())


# In[27]:

scores_innings.to_csv("Data/Question3.csv")#exporting data to csv


# In[ ]:



