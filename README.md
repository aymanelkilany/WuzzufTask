# WuzzufTask
As the required was two tasks, I wasn't able to install elasticsearch server on my machine, I just added comments where the indexing should happen on the code. 

I worked on a sample of hotels in a file called 'hotels1' to get you the output you needed. The number of hotels in the database was around 21000 and the allowed Watson calls was around 2500. I just wrote the code to provide the requirments exactly. 

Sequence of steps, 

- Preprocessed data to extract category hotels only
- Extract All reviews for each hotel
- Pass all reviews in order to analyze each one of them and get their tones scores 
- Nornmalize the Scores 
- Merge the Nornmlaized scores with each hotel data and there where each hotel should be indexed
-return all hotels data as JSON 
-Build Flask Service around the code 
