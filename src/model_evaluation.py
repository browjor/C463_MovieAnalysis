import os, csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import cross_val_score
import numpy as np

training_set = []
training_set_ratings = []
training_set_strings = []
with open(os.getcwd()+'\\clean_training_posneg.csv','r',encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        training_set.append(row)
        training_set_strings.append(row[1])
        training_set_ratings.append(row[0])

testing_set = []
testing_set_strings = []
testing_set_ratings = []

with open(os.getcwd()+'\\clean_testing_posneg.csv','r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        testing_set.append(row)
        testing_set_strings.append(row[1])
        testing_set_ratings.append(row[0])

testing_parameters = [((1, 1), 37500, 2, "No N-Gram (1,1) | Max Features=37500 | MinDf=2"),
                      ((1, 2), 37500, 2, "1,2 N-Gram (1,2) | Max Features=37500 | MinDf=2"),
                      ((1, 3), 37500, 2, "1,3 N-Gram (1,3) | Max Features=37500 | MinDf=2")
                      ]
chi_squared_parameters = [100, 500, 1000, 2000]

model_parameters = [("linear", 1,  "Linear Kernel - Regularization=1"),
                    ("rbf", 1,  "Rbf Kernel - Regularization=1"),
                    ("linear", 2,  "Linear Kernel - Regularization=2"),
                    ("rbf", 2,  "Rbf Kernel - Regularization=2"),
                    ("linear", 5,  "Linear Kernel - Regularization=5"),
                    ("rbf", 5,  "Rbf Kernel - Regularization=5"),
                    ("linear", 10,  "Linear Kernel - Regularization=10"),
                    ("rbf", 10,  "Rbf Kernel - Regularization=10")
                    ]


def tfidf_vectorize_text(input_ngram, maxfeatures, mindf, description):
    vectorizer = TfidfVectorizer(ngram_range=input_ngram, max_features=maxfeatures, min_df=mindf)
    training_tfidf = vectorizer.fit_transform(training_set_strings)
    testing_tfidf = vectorizer.transform(testing_set_strings)
    return training_tfidf, testing_tfidf, description


def perform_SVM_fitting_and_test(training, testing, kernel, regularization ,model_description, vectorize_description, chi_best_features):
    svm_model = SVC(kernel=kernel,C=regularization,gamma='auto')
    svm_model.fit(training, training_set_ratings)
    testing_predictions = svm_model.predict(testing)
    print("Classification Report for SVC")
    print(vectorize_description)
    print("Chi-squared selection for "+str(chi_best_features)+ " best features.")
    print(model_description)
    print(classification_report(testing_set_ratings, testing_predictions))
    #scores = cross_val_score(svm_model, training, training_set_ratings, cv=5)
    #print("Cross-validation scores on training set:", scores)
    #print("Mean CV accuracy on training set:", scores.mean())
    print("\n")

for test in testing_parameters:
    model_input = tfidf_vectorize_text(input_ngram=test[0], maxfeatures=test[1], mindf=test[2],
                                       description=test[3])
    for k in chi_squared_parameters:
        for model in model_parameters:
            chi2_selector = SelectKBest(chi2, k=k)
            training_after_chi = chi2_selector.fit_transform(model_input[0], training_set_ratings)
            testing_after_chi = chi2_selector.transform(model_input[1])
            perform_SVM_fitting_and_test(training=training_after_chi,testing=testing_after_chi,kernel=model[0], regularization=model[1], model_description=model[2], vectorize_description=model_input[2], chi_best_features=k)

