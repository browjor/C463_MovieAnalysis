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

######  Baseline - Simple Majority Classifier:
- Predicted every feature of the data as "neutral" (the majority class)

![image](https://github.com/user-attachments/assets/4dfc3b44-ace6-47bd-a1f4-47d598e6c3af)


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

##### New Approach - Use tf-idf vectorizor in combination with n-grams:
- To capture some semantic relationships other than just term frequency, tf-idf can be used with n-gram. This was easy to set up, just a parameter in the sklearn TfidfVectorizer, but fully capturing 1,2 ngrams led to roughly 155000 features for the transformed dataset, which led to a numpy memory error that said 22 GB of RAM were required. Luckily, another parameter in the vectorizer is the maximum number of features. Here's two tests with the top (most influential) 50000 features and 250000 features, for a linear and rbf kernel.
- 50000 features:

 ![image](https://github.com/user-attachments/assets/39795f2b-bd9d-45ce-860a-94048241ae21)
 
 ![image](https://github.com/user-attachments/assets/ea924df2-c93b-47aa-bfb9-edae820b8dc1)
 
- 25000 features:

![image](https://github.com/user-attachments/assets/0fe1fe0c-fe12-4015-99ed-5d729cd8085a)

![image](https://github.com/user-attachments/assets/e24cecfc-a0e8-4672-92a3-2726de1440bc)

- Trying with 75000 features and converting the float 64 arrays to float 32 arrays

![image](https://github.com/user-attachments/assets/4ee6108f-a22a-4da5-8fed-709b24d20355)

![image](https://github.com/user-attachments/assets/b3dff6ab-85ac-41a4-90ab-cd78a773a50a)

Conclusion: Not a huge difference. 


### JRB:
### EG:
### AC:


## Week of: 11/11/2024
### JRB:
### EG: Experimented with changing the boundaries for positive, neutral, and negative reviews. When I changed it to a more extreme approach (favoring negative and positive), I saw a slight improvement in the accuracy of the model. The previous best was 52%, and I got 53%.
![Screenshot 2024-11-13 161355](https://github.com/user-attachments/assets/af747d07-4993-4e0d-9272-8bb5da5492a4)

(Note: The image says it uses balanced class weights, but it actually used extreme weights.)

I also tried an approach that had more neutral than positive or negative. I got an accuracy of 59% which seems like an improvement. However, over 60% of the ratings were neutral, meaning that if the model just guessed neutral every time, it would be more accurate than the more sophisticated model. This shows that this approach isn't the way to go. 

### AC:


## Week of: 11/18/2024
### JRB:
### EG:
### AC:
