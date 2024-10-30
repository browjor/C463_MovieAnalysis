import nltk
from nltk.corpus import words, stopwords

nltk.download('words')
nltk.download('stopwords')

# Define a set of English words for fast lookup
english_words = set(words.words())
stop_words = set(stopwords.words('english'))

# Function to check if a word is in the English dictionary
def is_english_word(word):
    return word.lower() in english_words

def remove_characters_make_lowercase(string):
    return (string.replace(",", " ")
            .replace("?", " ")
            .replace("#", "")
            .replace(";", "")
            .replace("~", "")
            .replace("%", "")
            .replace("+", " ")
            .replace("@", " ")
            .replace("[", " ")
            .replace("]", " ")
            .replace("^", " ")
            .replace("’", "")
            .replace("“", "")
            .replace("*", "")
            .replace("'","")
            .replace(".", " ")
            .replace(")", " ")
            .replace("(", " ")
            .replace("_", " ")
            .replace("...", " ")
            .replace("(", " ")
            .replace("(", " ")
            .replace("(", " ")
            .replace(")", " ")
            .replace("/"," ")
            .replace("-"," ")
            .replace(":"," ")
            .replace("|", " ")
            .replace("'","")
            .replace("!"," ")
            .replace("\"","")
            .replace("”","")
            .replace("   ", " ")
            .replace("  ", " ")
            .lower())

def string_preprocessing(string):
    string = remove_characters_make_lowercase(string)
    string_list = string.split(" ")
    new_string = ""
    for word in string_list:
        if is_english_word(word):
            new_string += word + " "
    return new_string

word = "hello"
#if is_english_word(word):
#    print(f"{word} is an English word.")
#else:
#    print(f"{word} is not found in the English dictionary.")

example_string_1 = "Never got it. Never understood the appeal. I saw it a few years after its release and was, and are still, underwhelmed. Fox is a twitchy, uncomfortable dork, Chris Lloyd is a hammy prick, not nearly as funny as his turn on TAXI or as Commander Kruge, the Klingon baddie in STAR TREK III: THE SEARCH FOR SPOCK.∥Not a horrible film at all, just one I do not like or give a shit about. I've seen it twice and have no desire to ever see it again- dull as a silent fart. Same goes for the awful sequels."
example_string_2 = "Es horrible y no entiendo porque les gusta tanto. ¿Acaso solo les gusta porque es una película de los ochenta, EH?"
example_string_3 = "This shit stinks.😭😭😭🤢🤢🤮🤮🤮 Rick and morty but worse."
example_string_4 = "why is no one even phased at the whole thing with his mom ??? also wth the way she was portrayed ugh couldnt stop cringing AND! the most incredible thing on this film is that i have to believe that grown ass man is 17!! SEVEN FUCKING TEEN"
example_string_5 = "A Mood™ is totally ignoring the film in class, for the most part, so that I can finish reading a Jameson piece that I assigned for my class later in the day. I READ A SHORT ESSAY BY FREDRIC JAMESON AND TBH UNDERSTOOD MOST OF IT AND DID A GREAT JOB LECTURING IT IMO. It's just one of those films that constantly gets homaged to. In some ways it is inspiring and creative and well-made, but it's hard to see that past the pastiches it's born."
example_string_6 = "I mean, at the end of the day, Aubrey Plaza IS Wow Platinum, and that's that on that. Coppola sure is ambivalent about a large part of his legacy being his dynasty of actors, directors and nepo babies, isn't he? There was a lot of mostly derisive laughter in my screening, which seemed like an impulsive reaction to being faced with something that is often so nakedly earnest, vulnerable and personal, and as such frequently provoking secondhand embarrassment. It's not… more"


#print(remove_characters_make_lowercase(example_string_1))
example_string_1 = remove_characters_make_lowercase(example_string_1)
example_string_1_list = example_string_1.split(" ")
#print("Number of words in Example_String_1: "+str(len(example_string_1_list)))
example_string_1 = ""
for word in example_string_1_list:
    if is_english_word(word):
        example_string_1 += word + " "

example_string_1_list_new = example_string_1.split(" ")
#print("Number of words in checked example string 1: "+str(len(example_string_1_list_new)))
#print(example_string_1)




