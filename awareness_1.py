# -*- coding: utf-8 -*-

# Handles single line

vowels = ['a','e','i','o','u','y']
consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q', 'r','s','t','v','w','x','z']
content = "abcde fghi jklm nopq rstuv wxyz"

word_counter = 0
word_buffer = ""
word_store = ""
word_pattern = ""

for num, name in enumerate(content, start=1):
    if num == 1:
        print "---------- START ----------"
        print "Content to analyse: the text string: \"" + content + "\""
        print "Tasks:"
        print "======"
        print "1. Isolate words and ennumerate them"
        print "2. Echo words"
        print "3. Find their Consonant-Vowel patterns"

    if name == ' ':
        # ----- When at End of Word -----
        word_counter = word_counter + 1
        word_store = word_store + word_buffer + " "
        print "word number = " + str(word_counter) + ", word = " + word_buffer + ", word pattern = " + word_pattern
        word_buffer = ""
        word_pattern = ""
    else:
        # ----- When Processing Word
        word_buffer = word_buffer + name
        if name in consonants:
            word_pattern = word_pattern + 'C'
        else:
            word_pattern = word_pattern + 'V'

    if len(content) == num:
        # ----- When Processing Last Word
        word_counter = word_counter + 1
        word_store = word_store + word_buffer
        print "word number = " + str(word_counter) + ", word = " + word_buffer + ", word pattern = " + word_pattern
        word_buffer = ""
        word_pattern = ""
        print "---------- STOP ----------"
    #print("Letter {} is {}".format(num, name))
