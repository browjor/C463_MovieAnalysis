import os, csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import pickle
import numpy as np
from collections import Counter
from sklearn.feature_selection import SelectKBest, chi2

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



#printmajorityclass - we know that there are 3436 negative ratings and 3231 positive ratings
negative_ratings = []
for rating in testing_set_ratings:
    negative_ratings.append('negative')
print("Classification report for majority classifier:")
print(classification_report(testing_set_ratings, negative_ratings))
print("\n")

# vectorize the training and testing set
vectorizer = TfidfVectorizer(ngram_range=(1,3),use_idf=True, max_features=37500, min_df=2)
training_tfidf = vectorizer.fit_transform(training_set_strings)
testing_tfidf = vectorizer.transform(testing_set_strings)



# keeping high impact chi features
chi2_selector = SelectKBest(chi2, k=2000)
training_after_chi = chi2_selector.fit_transform(training_tfidf, training_set_ratings)
testing_after_chi = chi2_selector.transform(testing_tfidf)

#gamma calculations
n_features = training_after_chi.shape[1]
X_var = training_after_chi.toarray().var()
# Default gamma calculation
default_gamma = 1 / (n_features * X_var)
print("Calculated gamma:" + str(default_gamma) +"\n")

svm_model = SVC(kernel="linear")
svm_model.fit(training_after_chi, training_set_ratings)
testing_predictions = svm_model.predict(testing_after_chi)

print("Classification Report \n"
      "- Using 1,3 ngram and tfidf vectorizer - Max 37500 features as float64 "
      "- Using Chi-Squared value to keep top 2000 features"
      "- SVC Model: Linear Kernel  \n"
      )

print(classification_report(testing_set_ratings, testing_predictions))
print("\n")

#save fitted model to file for use in AI application
#pickle.dump(svm_model, open('../Megaflopolis_Standalone_Application/svc_linear_241210.pkl', 'wb'))
#pickle.dump(vectorizer, open('../Megaflopolis_Standalone_Application/fitted_vectorizer_241210.pkl', 'wb'))
pickle.dump(chi2_selector, open('../Megaflopolis_Standalone_Application/chi_selector_241210.pkl', 'wb'))