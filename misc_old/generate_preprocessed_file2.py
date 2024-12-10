import os
import pandas as pd
import re
import nltk
from nltk.corpus import wordnet, stopwords

# Download WordNet and load its vocabulary
nltk.download('wordnet')
nltk.download('stopwords')
wordnet_words = set(word.name().split('.')[0] for word in wordnet.all_synsets())
stop_words = set(stopwords.words('english'))
proper_noun_list = movie_details = [
    "Megalopolis 2024",
    "Cesar Catilina",
    "Mayor Franklyn Cicero",
    "Julia Cicero",
    "Clodio Pulcher",
    "Hamilton Crassus III",
    "Wow Platinum",
    "Fundi Romaine",
    "Jason Zanderz",
    "Teresa Cicero",
    "Vesta Sweetwater",
    "Constance Crassus Catilina",
    "Clodia Pulcher",
    "Charles Cothope",
    "Commissioner Stanley Hart",
    "Nush 'The Fixer' Berman",
    "Laurence Fishburne",      # Cast for Fundi Romaine
    "Jason Schwartzman",       # Cast for Jason Zanderz
    "Kathryn Hunter",          # Cast for Teresa Cicero
    "Grace VanderWaal",        # Cast for Vesta Sweetwater
    "Talia Shire",             # Cast for Constance Crassus Catilina
    "Chloe Fineman",           # Cast for Clodia Pulcher
    "James Remar",             # Cast for Charles Cothope
    "D.B. Sweeney",            # Cast for Commissioner Stanley Hart
    "Dustin Hoffman",          # Cast for Nush 'The Fixer' Berman
    "Adam Driver",             # Additional cast
    "Aubrey Plaza",            # Additional cast
    "Shia LaBeouf",            # Additional cast
    "Nathalie Emmanuel",       # Additional cast
    "Jon Voight",              # Additional cast
    "Forest Whitaker",         # Additional cast
    "Francis Ford Coppola",    # Director
    "Francis Ford Coppola",    # Producer
    "megaflopolis"
]

for word in proper_noun_list:
    word = word.lower()

proper_noun_set = set(proper_noun_list)

positive = 0
negative = 0
neutral = 0

replace_with_space_1 = r'[\u0021-\u0040]'
replace_with_space_2 = r'[\u005b-\u0060]'
keep_1 = r'[^\sa-zA-Z\u1F600-\u1F64F]'
space = r'[\u0041]{2,}'


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
            string = listy[1].strip('\n')
            string = re.sub(replace_with_space_1, " ", string)
            string = re.sub(replace_with_space_2, " ", string)
            string = re.sub(space, " ", string)
            string = re.sub(keep_1, "", string)
            string = string.lower()
            listy2 = string.split(" ")
            new_string = ""
            for word in listy2:
                word = word.strip()
                if len(word)<=2:
                    continue
                if word in stop_words:
                    continue
                if word in proper_noun_set:
                    new_string += word + ' '
                    continue
                if word in wordnet_words:
                    new_string += word + ' '
            if len(new_string) != 0:
                preprocessed_data.append([rating,new_string.strip()])



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




