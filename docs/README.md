# C463_MovieAnalysis
This project is for C463, we plan on implementing sentiment analysis of web-scraped Letterboxd reviews.

## Goals:
- The goal of our project is to develop a model that will attempt to match written user review statements with associated “star” ratings given for the movie Back To The Future (1985), specifically those given on the review site Letterboxd (letterboxd.com). This places our task broadly in the scope of supervised machine learning in sentiment analysis, and we will compare the effectiveness of various machine learning models, choosing the one that most closely matches the star rating given for a user review. In terms of inputs, the model will take the user as text and output a predicted star rating. 

## Infrastructure:
- The infrastructure of our project depends on collecting reviews via a custom Python web-scraper built using Selenium web automation. With a looping mechanism and acceptable delays (to not overwhelm Letterboxd), we aim to collect around 100,000 elements. Within these review elements are the date of review, the user, the review text, and the text rating. With further processing, we can split the review elements into usable chunks, and ultimately, store them in a text file on disk. An example of gathered review elements is shown below:

# Analysis:
- After processing, we can partition our larger dataset into elements used to train, to validate, and predict with a model. In terms of finding and building the correct model, we plan to export our data into a format suitable for WEKA, a machine learning workbench. With this, we have access to many machine learning models, and after a systematic comparison can choose an appropriate one. As our project already has a source of oracles (the star reviews), the whole project can be comparing different baselines. In the end, the true output of our project should be a list of generalization errors for various supervised learning models.
