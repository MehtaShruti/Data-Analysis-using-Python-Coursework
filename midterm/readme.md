**Question 1** : It is  focused on the enron email analysis, which basically revolved around the two main people involved in the scandal, Kenneth Lay and Jeffrey Skilling..

**ANALYSIS I**:

This analysis is performed to analyse the emails Kenneth Lay received other than the business conversations.
Such as the events he attended and advertisements emails he has received. We have analysed the the *notes_inbox* folder
out of all the emails

**Conclusion: He has been interacting with a lot of Natural Gas Companies, Energy related companies, attending meetings outside, attending events outside.**

<img width="1280" alt="noteslist" src="https://cloud.githubusercontent.com/assets/25044358/23640737/7a26f4ee-02bd-11e7-9220-90f99153517a.png">

**ANALYSIS 2**:

**PART I** : This analysis is performed on *Jeffrey Skilling* to analyse the number of emails he has sent and received over the
period of time (Represented as : Day > Number of emails on that day of week, see graph)

<img width="1280" alt="screen shot 2017-03-06 at 10 39 09 pm" src="https://cloud.githubusercontent.com/assets/25044358/23640899/542d7e60-02be-11e7-9523-e978af1a1e70.png">


**PART II**: In this analysis, we have analysed people interacting with Skilling on the weekends

<img width="1280" alt="weekend" src="https://cloud.githubusercontent.com/assets/25044358/23640869/1fae838c-02be-11e7-9639-25fd4f772f08.png">


**PART III**: This analysis helps us finding out the list of people outside ENRON, who have been communicating with Jeffrey along
with the email ids. This data is stored as a csv file


<img width="1280" alt="companieslist" src="https://cloud.githubusercontent.com/assets/25044358/23640918/84bf035a-02be-11e7-9811-7bd45dcbda97.png">

**Conclusion**: We conclude that he has received most of the emails during the weekdays(part I) and there were people working on weekends in Enron (part II) also we found out the list of companies that were the ENRON clients from which continuous interaction was taking place( part III)


**ANALYSIS 3**

**PART I **: In this analysis, we have extracted the list of the people who have ever been into contact with Kenneth Lay in all the communication he has had in and outside Enron. We have stored the list of people he has received emails from in *from_email_list.txt*, sent emails to in *to_email_list.txt* and the text of his emails in the file *email_body.txt*.


**PART II** : from the list of people he has communicated with, further analysis is done on the most common people has has sent emails to and received from 

<img width="1280" alt="mostcommon" src="https://cloud.githubusercontent.com/assets/25044358/23641058/4a9ec970-02bf-11e7-971f-600c1d2f8b77.png">


**PART III**: the last analysis is performed to measure the frequency of the words he has used in the conversation of the emails

<img width="1280" alt="freq_words" src="https://cloud.githubusercontent.com/assets/25044358/23641038/30f384a2-02bf-11e7-94b1-37ac6a8cc0ad.png">

**Conclusion**: Kenneth Lay, the lead person behind the scandal was analysed where in we figured out the people he has been interating with. In analysis II we found out the most frequent people he has interacted with. In part III, we found out the most frequent words in used in his conversations.

**Question 2**:

**Analysis (Collection, Storage and Retrieval)** : It is the data collection, storage and retrieval from the Archive API in NYT Developers Networks. 
I have collected the data of Year 2015 for and organized the folder according to the newsdesk, 
section, sub-section and then storing the abstract and url of the articles in the text file of that corresponding folder. ( Focused on Collection and Storage of data( only headlines and URL to a .txt file)

**The news headline has been stored as a separate text file in order to make it more readable rather than storing it in a json**

<img width="1280" alt="news" src="https://cloud.githubusercontent.com/assets/25044358/23641203/22334596-02c0-11e7-8547-fab6788326d0.png">

Analysis I: This analysis is based upon the criminal rates in different cities with different type of count of crimes

**Conclusion: We have analysed the crimes happening in the cities of US, number of different types crimes occured in the cities**

**Analysis II** : 
This analysis is based on the **Books API: Best Sellers** wherein I have analysed the number of early releases that the books that got newly published within 2 years

<img width="1280" alt="books_published" src="https://cloud.githubusercontent.com/assets/25044358/23641211/2f75e768-02c0-11e7-937c-e24678d5730d.png">

**Conclusion: This analysis explains the books that have been published within two years of their old date of publication**

**Analysis III**: This anlysis is related to Donald Trump's Presidential political promotional times
<img width="1280" alt="graph_trump" src="https://cloud.githubusercontent.com/assets/25044358/23641209/2e1281d8-02c0-11e7-8d2c-c4371de494df.png">

**Conclusion: We have anlysed the words related to the political promitional times and plot the graph based on the number of articles published in the month of Jan, Feb an Mar**



