import emoji
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Removes stopwords from a string
def remove_stopwords(string):
    cached_stopwords = stopwords.words()
    word_list = word_tokenize(string)
    filtered_words = []

    for word in word_list:
        if word not in cached_stopwords:
            filtered_words.append(word)

    filtered_string = ""
    for word in filtered_words:
        filtered_string += " " + word

    return filtered_string


def lemmatize(string):
    wordnet_lemmatizer = WordNetLemmatizer()
    word_list = word_tokenize(string)

    for word in word_list:
        string = string.replace(word, wordnet_lemmatizer.lemmatize(word))

    return string


# Removes special characters from a string
def remove_special_char(string):
    char_to_erase = "\"\n\t!#$%&'()*+,-./:;<=>?@[\]‘🥰🏿^_—`{|}~🏻‍⋯’•“”️"

    for char in char_to_erase:
        string = string.replace(char, " ")

    return string


# Removes standalone numbers from a string
def remove_numbers(string):
    string = re.sub(r"\b[\+-]?[0-9]*[\.]?[0-9]+([eE][\+-]?[0-9]+)?\b", "", string)
    return string


# Removes user tags (@dario.p_95) from a string
def remove_user_tags(string):
    string = re.sub(r"@\S+", "", string)
    return string


# Removes braille pattern from a string
def remove_braille_pattern(string):
    braille_pattern = re.compile("["u"\u2800""]", flags=re.UNICODE)
    string = braille_pattern.sub(r'', string)
    return string


# Removes multiple consecutive white space characters in a string by replacing them with one white space character
def remove_multiple_whitespace(string):
    string = re.sub(r" +", " ", string)
    return string


# Returns emojis from a given string
def get_emojis(string):
    emojis = ""
    for emoji_item in string:
        if emoji_item in emoji.UNICODE_EMOJI:
            emojis += emoji_item + " "

    return emojis


# Removes emojis from a given string
def remove_emojis(string):
    for char in string:
        if char in emoji.UNICODE_EMOJI:
            string = string.replace(char, "")

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)

    string = emoji_pattern.sub(r'',string)

    return string


# Removes \n in a string
def remove_new_line(string):
    string = string.replace("\n", " | ")
    return string
