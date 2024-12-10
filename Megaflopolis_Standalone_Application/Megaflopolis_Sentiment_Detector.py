import pickle
import nltk
from nltk.corpus import wordnet, stopwords
from nltk.stem.snowball import SnowballStemmer
import re
from sklearn.feature_extraction.text import TfidfVectorizer

if __name__ == "__main__":

    with open('svc_linear_241210.pkl', 'rb') as model_file:
        model = pickle.load(model_file)

    with open('fitted_vectorizer_241210.pkl', 'rb') as vec_file:
        vectorizer = pickle.load(vec_file)

    with open('chi_selector_241210.pkl', 'rb') as chi_file:
        chi_selector = pickle.load(chi_file)

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

    replace_with_space_1 = r'[\u0021-\u0040]'
    replace_with_space_2 = r'[\u005b-\u0060]'
    keep_1 = r'[^\sa-zA-Z\u1F600-\u1F64F]'
    space = r'[\u0041]{2,}'

    stemmer = SnowballStemmer("english")

    user_input = input("Please input your review of Megalopolis(2024). Don't be shy :)")


    def preprocess(user_input):
        string = re.sub(replace_with_space_1, " ", user_input)
        string = re.sub(replace_with_space_2, " ", string)
        string = re.sub(space, " ", string)
        string = re.sub(keep_1, "", string)
        string = string.lower()
        listy2 = string.split(" ")
        new_string = ""
        for word in listy2:
            word = word.strip()
            if len(word) <= 2:
                continue
            if word in stop_words:
                continue
            if (word in proper_noun_set) or (word in wordnet_words):
                try:
                    word = stemmer.stem(word)
                    new_string += word + ' '
                except Exception as e:
                    continue
            else:
                continue
        if len(new_string) <= 0:
            print("Uh oh, looks like we couldnt read that! Please try again.")
            preprocess(user_input)
        else:
            return new_string

    def guess_review(user_input):
        review = [preprocess(user_input)]
        review_tfidf = vectorizer.transform(review)
        chi_review_selector = chi_selector.transform(review_tfidf)
        prediction = model.predict(chi_review_selector)
        print("We think that YOU think this movie is:" + str(prediction[0]))
        user_input_2=input("If you'd like to input another review, type Y/N.")
        if user_input_2 == "Y":
            user_input_3 = input("Please input your review of Megalopolis(2024). Don't be shy :)   ")
            guess_review(user_input_3)
        else:
            print("Bye!")

    guess_review(user_input)
