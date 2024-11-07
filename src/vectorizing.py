import os, csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report


training_set = []
training_set_ratings = []
training_set_strings = []
with open(os.getcwd()+'\\clean_training.csv','r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        training_set.append(row)
        training_set_strings.append(row[1])
        training_set_ratings.append(row[0])

testing_set = []
testing_set_strings = []
testing_set_ratings = []

with open(os.getcwd()+'\\clean_testing.csv','r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        testing_set.append(row)
        testing_set_strings.append(row[1])
        testing_set_ratings.append(row[0])

# Initialize the TfidfVectorizer
vectorizer = TfidfVectorizer(use_idf=True)

training_tfidf = vectorizer.fit_transform(training_set_strings)
testing_tfidf = vectorizer.transform(testing_set_strings)

n_features = training_tfidf.shape[1]
X_var = training_tfidf.toarray().var()
# Default gamma calculation
default_gamma = 1 / (n_features * X_var)
print("Default gamma:", default_gamma)

svm_model = SVC(kernel="rbf", gamma=0.01, random_state=42, class_weight="balanced")
svm_model.fit(training_tfidf, training_set_ratings)
testing_predictions = svm_model.predict(testing_tfidf)

print("Classification Report for SVC \n"
      "- RBF Kernel- Gamma 0.01 -with Balanced Class Weights")
print(classification_report(testing_set_ratings, testing_predictions))
print("\n")

svm_model = SVC(kernel="rbf", gamma=0.1, random_state=42, class_weight="balanced")
svm_model.fit(training_tfidf, training_set_ratings)
testing_predictions = svm_model.predict(testing_tfidf)

print("Classification Report for SVC \n"
      "- RBF Kernel- Gamma 0.1 -with Balanced Class Weights")
print(classification_report(testing_set_ratings, testing_predictions))
print("\n")

svm_model = SVC(kernel="rbf", gamma=10, random_state=42, class_weight="balanced")
svm_model.fit(training_tfidf, training_set_ratings)
testing_predictions = svm_model.predict(testing_tfidf)

print("Classification Report for SVC \n"
      "- RBF Kernel- Gamma 10 -with Balanced Class Weights")
print(classification_report(testing_set_ratings, testing_predictions))
print("\n")