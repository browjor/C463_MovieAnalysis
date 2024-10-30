from generating_word_set import return_word_set
from example_word_cleaning import remove_characters_make_lowercase
import os
import pandas as pd
word_set = return_word_set()
positive = 0
negative = 0
neutral = 0
preprocessed_data = []
with open(os.getcwd() + '\\clean_output.txt', 'r', encoding='utf-8') as file:
    while True:
        line = file.readline()
        if not line:
            break
        listy = line.split(" ", 1)
        if "This review may contain spoilers. I can handle the truth." in listy[1]:
            continue
        else:
            rating = int(listy[0])
            #balanced, slightly more neutral
            if 1 <= rating <= 3:
                rating = 'negative'
                negative += 1
            elif 4 <= rating <= 7:
                rating = 'neutral'
                neutral += 1
            elif 8 <= rating <= 10:
                rating = 'positive'
                positive += 1
            # favors extremes
            #if 1 <= rating <= 4:
            #    rating = 'negative'
            #elif 5 <= rating <= 6:
            #    rating = 'neutral'
            #elif 7 <= rating <= 10:
            #    rating = 'positive'
            string = remove_characters_make_lowercase(listy[1])
            new_string = ""
            listy2 = string.split(" ")
            for word in listy2:
                if word in word_set:
                    new_string += word + " "
            if len(new_string) != 0:
                preprocessed_data.append([rating,new_string])


#randomizing selections and writing train, test, human_oracle to file
negative = []
positive = []
neutral = []
for datum in preprocessed_data:
    if datum[0] == 'negative':
        negative.append(datum)
    elif datum[0] == 'positive':
        positive.append(datum)
    elif datum[0] == 'neutral':
        neutral.append(datum)
    else:
        print("ERROR")

negative_dataframe = pd.DataFrame(negative)
positive_dataframe = pd.DataFrame(positive)
neutral_dataframe = pd.DataFrame(neutral)

train_negative_dataframe = negative_dataframe.sample(frac=0.72, random_state=1234, replace=False)
negative_dataframe = negative_dataframe.drop(train_negative_dataframe.index)
print(len(train_negative_dataframe))
test_negative_dataframe = negative_dataframe.sample(frac=0.892, random_state=5678, replace=False)
negative_dataframe = negative_dataframe.drop(test_negative_dataframe.index)
print(len(test_negative_dataframe))
humanOracle_negative_dataframe = negative_dataframe
print(len(humanOracle_negative_dataframe))

train_positive_dataframe = positive_dataframe.sample(frac=0.72, random_state=9876, replace=False)
positive_dataframe = positive_dataframe.drop(train_positive_dataframe.index)
print(len(train_positive_dataframe))
test_positive_dataframe = positive_dataframe.sample(frac=0.892, random_state=6543, replace=False)
positive_dataframe = positive_dataframe.drop(test_positive_dataframe.index)
print(len(test_positive_dataframe))
humanOracle_positive_dataframe = positive_dataframe
print(len(humanOracle_positive_dataframe))


train_neutral_dataframe = neutral_dataframe.sample(frac=0.72, random_state=7456, replace=False)
neutral_dataframe = neutral_dataframe.drop(train_neutral_dataframe.index)
print(len(train_neutral_dataframe))
test_neutral_dataframe = neutral_dataframe.sample(frac=0.892, random_state=1245, replace=False)
neutral_dataframe = neutral_dataframe.drop(test_neutral_dataframe.index)
print(len(test_neutral_dataframe))
humanOracle_neutral_dataframe = neutral_dataframe
print(len(humanOracle_neutral_dataframe))

training_dataframe = pd.concat([train_negative_dataframe, train_positive_dataframe, train_neutral_dataframe], axis=0, ignore_index=True, verify_integrity=True)
print(len(training_dataframe))
testing_dataframe = pd.concat([test_negative_dataframe, test_positive_dataframe, test_neutral_dataframe], axis=0, ignore_index=True, verify_integrity=True)
print(len(testing_dataframe))
human_oracle_dataframe = pd.concat([humanOracle_negative_dataframe, humanOracle_positive_dataframe, humanOracle_neutral_dataframe], axis=0, ignore_index=True, verify_integrity=True)
print(len(human_oracle_dataframe))

training_dataframe = training_dataframe.sample(frac=1, random_state=7456, replace=False)
testing_dataframe = testing_dataframe.sample(frac=1, random_state=1245, replace=False)
human_oracle_dataframe = human_oracle_dataframe.sample(frac=1, random_state=1245, replace=False)

human_oracle_dataframe.to_csv(os.getcwd() + '\\for_human_oracle.csv', index=False, columns=[1])
training_dataframe.to_csv(os.getcwd() + '\\clean_training.csv', index=False)
testing_dataframe.to_csv(os.getcwd() + '\\clean_testing.csv', index=False)
human_oracle_dataframe.to_csv(os.getcwd() + '\\clean_human_oracle.csv', index=False)





