# -*- coding: utf-8 -*-
# Handles multiple lines
import re
#import json


#filepath = 'awareness_2.txt'

def create_dict_of_cleaned_lines(filepath):
    with open(filepath) as fp:
        line = fp.readline()
        line_counter = 1
        line_buffer = {}
        while line:
            p = re.compile('\s+') # compile pattern
            cleaned_line = p.sub(' ', line).strip()
            line_buffer[line_counter] = cleaned_line

            # --- next loop ---
            line = fp.readline()
            line_counter += 1

    return line_buffer

#CALL:
#print create_dict_of_cleaned_lines('awareness_2.txt')

#CALL:
#d = create_dict_of_cleaned_lines('awareness_2.txt')
#print d.get(5)

def clean_content(filepath):

    f = open(filepath, 'r')
    content = f.read() # read file as string
    p = re.compile('\s+') # compile pattern
    cleaned_content = p.sub(' ', content).strip()
    f.close()

    return cleaned_content

# CALL:
#print clean_content('awareness_2.txt')


def create_word_pattern_latin(word):

    upper_v = ['A', 'E', 'I', 'O', 'U', 'Y']
    lower_v = ['a', 'e', 'i', 'o', 'u', 'y']
    upper_c = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    lower_c = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

    word_buffer = ""

    for letter in word:
        if letter in upper_c:
            word_buffer = word_buffer + 'C'
        elif letter in upper_v:
            word_buffer = word_buffer + 'V'
        elif letter in lower_c:
            word_buffer = word_buffer + 'c'
        elif letter in lower_v:
            word_buffer = word_buffer + 'v'
        else:
            word_buffer = word_buffer + letter

    return word_buffer

# CALL:
#print create_word_pattern_latin('Sana.')
#print create_word_patterns(cleaned_content)

def create_word_pattern_hindi(word):

    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    short_vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
    long_vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    word_buffer = ""

    #Latin Capital Letter V: u"\u0056"
    #Combining Macron: u"\u0304"

    for letter in word:
        if letter in upper_c:
            word_buffer = word_buffer + 'C'
        elif letter in upper_v:
            word_buffer = word_buffer + 'V'
        elif letter in lower_c:
            word_buffer = word_buffer + 'c'
        elif letter in lower_v:
            word_buffer = word_buffer + 'v'
        else:
            word_buffer = word_buffer + letter

    return word_buffer

# CALL:
#print create_word_pattern_latin('Sana.')
#print create_word_patterns(cleaned_content)


