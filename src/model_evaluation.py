import os, csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
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

testing_parameters = [((1, 5), True, 10000, 1, "Ngram=(1,2) | Use-Idf=True | Max Features=15000 | MinDf=1 | Float64"),
                      ((1, 3), True, 15000, 1, "Ngram=(1,3) | Use-Idf=True | Max Features=15000 | MinDf=1 | Float64"),
                      ((1, 4), True, 15000, 1, "Ngram=(1,4) | Use-Idf=True | Max Features=15000 | MinDf=1 | Float64"),
                      ((1, 1), True, 8000, 1, "Ngram=(1,2) | Use-Idf=True | Max Features=8000 | MinDf=1 | Float64"),
                      ((1, 2), True, 8000, 1, "Ngram=(1,3) | Use-Idf=True | Max Features=8000 | MinDf=1 | Float64"),
                      ((1, 3), True, 8000, 1, "Ngram=(1,4) | Use-Idf=True | Max Features=8000 | MinDf=1 | Float64"),
                      ((1, 1), True, 2000, 1, "Ngram=(1,2) | Use-Idf=True | Max Features=2000 | MinDf=1 | Float64"),
                      ((1, 2), True, 2000, 1, "Ngram=(1,3) | Use-Idf=True | Max Features=2000 | MinDf=1 | Float64"),
                      ((1, 3), True, 2000, 1, "Ngram=(1,4) | Use-Idf=True | Max Features=2000 | MinDf=1 | Float64")]

model_parameters = [("rbf", "balanced", 1, "Rbf Kernel | Balanced Class Weights | Gamma 1")]


def tfidf_vectorize_text(input_ngram, useidf, maxfeatures, mindf, description):
    vectorizer = TfidfVectorizer(ngram_range=input_ngram, use_idf=useidf, max_features=maxfeatures, min_df=mindf)
    training_tfidf = vectorizer.fit_transform(training_set_strings)
    testing_tfidf = vectorizer.transform(testing_set_strings)
    return training_tfidf, testing_tfidf, description


def perform_SVM_fitting_and_test(training, testing, kernel, bal_class_weight , gamma, model_description, vectorize_description):
    svm_model = SVC(kernel=kernel, class_weight=bal_class_weight, gamma=gamma)
    svm_model.fit(training, training_set_ratings)
    testing_predictions = svm_model.predict(testing)
    print("Classification Report for SVC \n")
    print(vectorize_description+"\n")
    print(model_description+"\n")
    print(classification_report(testing_set_ratings, testing_predictions))
    #scores = cross_val_score(svm_model, training, training_set_ratings, cv=5)
    #print("Cross-validation scores on training set:", scores)
    #print("Mean CV accuracy on training set:", scores.mean())
    print("\n")

for test in testing_parameters:
    model_input = tfidf_vectorize_text(input_ngram=test[0], useidf=test[1], maxfeatures=test[2], mindf=test[3],
                                       description=test[4])
    for model in model_parameters:
        perform_SVM_fitting_and_test(training=model_input[0],testing=model_input[1],kernel=model[0],bal_class_weight=model[1],gamma=model[2], model_description=model[3], vectorize_description=model_input[2])

