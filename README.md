# C463_MovieAnalysis
This project is for C463, we plan on implementing sentiment analysis of web-scraped Letterboxd reviews.

### Main Functionalities:
1. Command line access:
   - Accomplished through taking an argument from the command line, whether it be a movie title to be searched or a
   command such as "movie reviewanalysis"
2. Search for a movie's reviews
    - Acommplished through Selenium web automation, where a movie name can be inputted from the command line and a
   list will be generated from searching this movie in Letterboxd itself
      - if there is any ambiguity, the program should return a list of movies that can be further clarified
3. Generate sentiment analysis of a movie's reviews
   - Accomplished through Selenium web automation, where when a movie has been specified enough, all of (or a sample of)
   a movie's reviews will be web scraped, stored, and analysed to return insights.
