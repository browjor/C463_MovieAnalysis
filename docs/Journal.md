# Journal Entries

### Work Completed So Far:
- Cemented what our project idea was
- Began working on scraper

## Week of: 9/23/2024
- The group met on 9/25 to further plan the project and to try to complete the scraper.
### JRB: 
- Worked on the scraper and used the scraper to gather data, developed script to turn messy output from scraper into clean output from file.
### EG: 
- Made progress on scraper, improving the format of the collected data. Also discussed how the final scraper should work.
### AC:
- Sorted through scholarly articles directly relating to the project. Provided the best possible literature links that portray surpervised machine learning sentiment analysis.

## Week of: 9/30/2024
### JRB:
### EG:
- Now that we collected some data, we discussed the next step. We determined that we should preprocess the data so that it can be used in WEKA.
### AC:
![image](https://github.com/user-attachments/assets/df9f239d-0fd8-4cfb-8cfb-9cc7e5cad228)


## Week of: 10/7/2024
Group met and worked on preprocessing of review text. 
### JRB:
### EG:
### AC:


## Week of: 10/14/2024
As a group, decided to change the film reviews from Back to the Future to Megalopolis(2024). There are many more reviews and they are more distributed throughout the ratings.
With the current programs, the switch is relatively easy and data has been collected for Megalopolis. 
### JRB:
### EG:
### AC:


## Week of: 10/21/2024
![20240925_172207](https://github.com/user-attachments/assets/f90cd3fc-a19f-4fd5-99ef-99996124bd50)
### JRB:
### EG:
### AC:


## Week of: 10/28/2024
- The goal of our project is to develop an AI model that will classify Letterboxd reviews for the 2024 movie Megalopolis into three separate sentiment categories, neutral, positive, and negative. Our AI model will take a review as an input and output a sentiment. To train our model, we will use pairs of data consisting of a text review and a star rating (1-10). The star rating will be transformed to a positive, neutral, or negative integer based on an arbitrary range. For example, 1-2 stars for negative sentiment, 3-7 stars for neutral sentiment, 8-10 stars for positive sentiment. For a baseline, we will predict the most frequent class. For an oracle, we will manually classify a random sampling of reviews and choose what sentiment they are. 
- As our problem falls into the area of sentiment analysis through supervised learning, we have chosen the SVM (Support Vector Machine) model to handle this multiclass classification task. We plan on cleaning, preprocessing our textual data, vectorizing the review text, and then training the SVM model with our training data. We then judge its accuracy by measuring the sentiment in test data against the star rating, our baselines, and then oracles.

![20241030_165849](https://github.com/user-attachments/assets/32b7c4eb-ceed-4c0c-bf84-808513da93cb)

![SVM_with_idf_vec](https://github.com/user-attachments/assets/a32d7a92-dd33-485e-b35d-e4ffc0e56552)


### JRB:
### EG:
### AC:


## Week of: 11/4/2024
Reworked preprocessing, used WordNet as dictionary to compare words in reviews against
*work is in generate_preprocessed_file2.py
Achieved slightly better results

###### Explanation of precision, recall, and f1 score:
- Precision: Percentage of correct positive predictions relative to total positive predictions
- Recall: Percentage of correct positive predictions relative to total actual positives
- F1 Score: Weighted harmonic mean of precision and recall, 1 is the best
- Support: How many of each class are in the dataset

![image](https://github.com/user-attachments/assets/5bd0d895-5152-4b3c-b43c-3a042e29be96)

##### After changing regularization parameter:
- "Regularization adds a penalty term to the standard loss function that a machine learning model minimizes during training. This penalty encourages the model to keep its parameters (like weights in neural networks or coefficients in regression models) small, which can help prevent overfitting"
- In our case, there is extremely little difference in changing this parameter, as seen:

![image](https://github.com/user-attachments/assets/a18734dd-5e99-4d0c-9707-35d01a5585fb)

![image](https://github.com/user-attachments/assets/53847513-5bfb-4037-90ee-ff67194316b6)

##### After changing to balanced class weights:

![image](https://github.com/user-attachments/assets/c3c7d881-fcbf-49af-9dc0-24624162b384)

##### Altering the kernel to be non-linear:
[Plot classification boundaries with different SVM Kernels](https://scikit-learn.org/dev/auto_examples/svm/plot_svm_kernels.html#sphx-glr-auto-examples-svm-plot-svm-kernels-py)

![image](https://github.com/user-attachments/assets/de7129c8-2052-449e-8f9d-d51696c3636b)

##### Experimenting with gamma
- "gamma plays a crucial role in defining the behavior of the decision boundary. It can be seen as the inverse of the radius of influence of samples selected by the model as support vectors. Intuitively, a low gamma value means that the influence of a single training example reaches far, affecting a larger region of the feature space. Conversely, a high gamma value means that the influence is close, affecting only the region near the training example"
- The gamma for the previous example is:  1 / (n_features * X. var()) as value of gamma, - if 'auto', uses 1 / n_features - if float, must be non-negative (from sklearn.svm documentation) After these calculations, the gamma used is roughly 1.
- Will try for gamma of 0.01, 0.1, and 10, just for boundaries.

  ![image](https://github.com/user-attachments/assets/9675d99d-fab7-4a4d-bfff-d8152e50e1b8)

  ![image](https://github.com/user-attachments/assets/7b68af6f-4fc4-4993-a419-f6e11022f070)

  ![image](https://github.com/user-attachments/assets/a5dbc1b3-07fe-43f2-ba25-451ed933890f)

### JRB:
### EG:
### AC:


## Week of: 11/11/2024
### JRB:
### EG:
### AC:


## Week of: 11/18/2024
### JRB:
### EG:
### AC:
