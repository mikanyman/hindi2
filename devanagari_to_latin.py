#!C:\Python27
# -*- coding: utf-8 -*-

import re

# https://www.omniglot.com/writing/devanagari_conjuncts.php
# https://gomputor.wordpress.com/2008/09/27/search-replace-multiple-words-or-characters-with-python/
# Correction Python 2.x --> Python 3: Iterator objects: d.iteritems() -> iter(d.items())

def replace_str(txt, dict):
    for i, j in iter(dict.items()):
        txt_out = txt.replace(i, j)
    return txt_out

txt_1 = 'आजा सनम मधुर चाँदनी में'

# --- Dual Latin ---


# --- Single Vowels ---
dict_1 = {'ु':'u','ा':'ā','ँ':'ā̃'}
dict_2 = {'ाँ':'ā̃'}

# --- Syllables ending in ā ---
dict_3 = {u'\u0906':'ā'}
dict_4 = {'जा':'jā'}

# --- Single Consonants ---
dict_5 = {'स':'sa'}
dict_6 = {'न':'na'}
dict_7 = {'म$':'m'}


# --- Devanagari Conjuncts ---
txt_2 = replace_str(txt_1, dict_1)
txt_3 = replace_str(txt_2, dict_2)
txt_4 = replace_str(txt_3, dict_3)
txt_5 = replace_str(txt_4, dict_4)
txt_6 = replace_str(txt_5, dict_5)
txt_7 = replace_str(txt_6, dict_6)
txt_8 = replace_str(txt_7, dict_7)

print(txt_8)
