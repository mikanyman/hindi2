# -*- coding: utf-8 -*-

'''
# TOIMIVA TESTI
def calling_function(char):
    lower_w_diacritics = ['ī','i']
    char_buffer = ''
    if char in lower_w_diacritics:
        char_buffer = char_buffer + translit_maatra(char)
    else:
        char_buffer = char_buffer + "Ei tunnistusta"
    return char + " = " + char_buffer
# CALL:
print calling_function('ī') # ī
'''

'''
# TOIMIVA TESTI + LOOPPI --> Looppi pilkkoo merkin kahtia --> break korjasi
def calling_function(char):

    upper_v = ['A', 'E', 'I', 'O', 'U', 'Y']
    lower_v = ['a', 'e', 'i', 'o', 'u', 'y']
    lower_v_diacritics = ['ī'] # ī
    upper_c = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
    lower_c = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
    vowels = upper_v + lower_v + lower_v_diacritics
    consonants = upper_c + lower_c

    char_buffer = ''
    for c in char:
        if char in vowels:
            maatra = translit_maatra(char)
            char_buffer = char_buffer + maatra
            break
        else:
            char_buffer = char_buffer + "Ei tunnistusta"

    return char + " = " + char_buffer
# CALL:
#print calling_function('ī') # ī
'''

#if '\xc4\xab' == 'ī':
#    print "True"

#if u'ī' == u'\u012b':
#    print "True"

#teststring = 'longstringfortest'
#for i, c in enumerate(teststring):
#    if c == 'g':
#        print teststring[i+1]




#print int("012b", 16) # results in 299
#print unichr(299) # results in ī
#print ord(u'ī') # results in 299
# code point: \u012b
# utf-8 encoded code point: \xc4\xab

"""
# --- TOIMIVA ---
def new(word):

    # --- TOIMIVA ---
    probchar = 'ī'
    O12b = probchar.decode('utf-8')

    word_buffer = ''
    for c in word:
        if c == 'k':
            word_buffer = word_buffer + 'क'
        if c == 'l':
            word_buffer = word_buffer + 'ल'
        if c == O12b: # u'\u012b' = ī TOIMIVA: O12b
            word_buffer = word_buffer + 'ी' # ी

    return word_buffer

# --- TOIMIVA ---
syote = 'klī'
ensyote = syote.decode('utf-8')
print new(ensyote)

#print new(u'kl\u012b') # MUUTETTAVA SYÖTE UNICODEKSI
#kalīka
"""

"""
inp = u'\u012b'
for c in inp:
    if c == u'\u012b':
        print "Match! \xc4\xab"
    else:
        print "\xc4\xab sucks!"
# Results in "Match! ī"
"""

#print b'\xc2\xb5'.decode('utf-8')

#print u'µ'

unicode_string = u"क";
bytestring = unicode_string.encode('utf-8'); # If it is encoded; it is no longer Unicode
unicode_again = bytestring.decode('utf-8')

print unicode_again