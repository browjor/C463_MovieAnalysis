
import os
from misc_old.example_word_cleaning import remove_characters_make_lowercase
import re

from nltk.corpus import words, stopwords


def return_word_set():

    # Define a set of English words for fast lookup
    english_words = set(words.words())
    stop_words = set(stopwords.words('english'))
    word_set = set()
    with open(os.getcwd()+'\\clean_output.txt','r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            listy = line.split(" ",1)
            if "This review may contain spoilers. I can handle the truth." in listy[1]:
                continue
            else:
                string = remove_characters_make_lowercase(listy[1])
                listy2 = string.split(" ")
                for word in listy2:
                    word_set.add(word)

    #convert to list for easier access
    sorted_word_set = sorted(word_set)
    sorted_list = []
    for i in sorted_word_set:
        sorted_list.append(i)
    new_sorted_list = []
    pattern = r'^[\u0000-\u007F]*$'
    digit_pattern = r'\d'
    for l in sorted_list:
        if len(l) == 0:
            continue
        l = re.sub(digit_pattern, '', l)
        if re.search(pattern, l) is not None:
            new_sorted_list.append(l.strip(" "))
        if len(l) == 0:
            continue

    #back to set
    new_sorted_set = set()
    for p in new_sorted_list:
        if len(p) != 0:
            if p in stop_words:
                continue
            if p in english_words:
                new_sorted_set.add(p)
    new_sorted_set = sorted(new_sorted_set)
    return new_sorted_set

