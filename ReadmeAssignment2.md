Question 1 :In the question we are asked to prove Ziph's law by showing the plot between the Ranks and frequency of words on any corpus from Natural Language toolkit.
 **PART I**
 For this, the below steps were followed:
  -Import the packages: webtext from the nltk corpus( for the webtext data), matplotlib( to plot grahs), glob( to open the file), csv( for interacting with csv) , re(regular expressionscxvbcvbcvjbn
  -First of all we will ready our data, according to the requirements for the analysis by removing the punctuations and converting the words to the lower case
  -count the frequency of the words and mention its rank ( frequency is inversely proportional to its rank)
  -write the words, their frequencies and rank into the csv file
**PART II**
  Plot the graph:
  -read the frequencies, rank of the words and plot the loglog graph between the two(prove ziph's law)
  
Question 2: In this question, we are given the data(json files) of various restaurants, hotels and attractions, we have to create the folder hierarchy with the lowest being 
on the basis of terms and place the json files in the correct folder
For this, the below steps were followed:
**PART I**
 -import packages: os,json
 -get the path of the data folder where all the json files are placed
 -load the json file( a dictionary), then get the location(key) which is a subdictionary inside the json file
 -get the values of the keys to get the desired directory path( country>state>city>zipcode>term>jsonfile)
 -keep appending the path with the original directory structure
**PART II**
 -we are expected to place the names of the restaurants in the csv file along with the city, country code,Day of week,Start time hour, start time minute,
 end time hour and end time minute
 -for this we have to traverse through the dictionary to get the key 'hours', inside that we can strip start time hour and end time hour to achieve the expected result
 


  
  
