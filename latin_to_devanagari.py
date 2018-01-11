# -*- coding: utf-8 -*-

upper_v = ['A', 'E', 'I', 'O', 'U', 'Y']
lower_v = ['a', 'i', 'o', 'u', 'e', 'y'] # a
lower_v_diacritics = [u'\u0101', u'\u01e1', u'\u012b', u'\u016b', u'\u1e5b'] # ā, ǡ, ī, ū, ṛ
upper_c = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
lower_c = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
lower_c_diacritics = [u'\u1e45', u'\u00f1', u'\u1e6d', u'\u1e0d', u'\u1e5b', u'\u1e47', u'\u015b', u'\u1e63'] # ṅ, ñ, ṭ, ḍ, ṛ, ṇ, ś, ṣ

vowels = upper_v + lower_v + lower_v_diacritics
consonants = upper_c + lower_c + lower_c_diacritics

def translit_char(char):

    # --- Latin Single Vowels ---
    if char == 'a': ret_val = 'अ'
    if char == 'i': ret_val = 'इ'
    if char == 'u': ret_val = 'उ'
    if char == 'e': ret_val = 'ए'
    if char == 'o': ret_val = 'ओ'

    # --- Latin Vowels with Diacritics ---
    if char == u'\u0101': ret_val = 'आ' # ā
    if char == u'\u01e1': ret_val = 'ऑ' # ǡ
    if char == u'\u012b': ret_val = 'ई' # ī
    if char == u'\u016b': ret_val = 'ऊ' # ū
    if char == u'\u1e5b': ret_val = 'ऋ' # ṛ

    # --- Latin Diftongs ---
    if char == 'ai': ret_val = 'ऐ'
    if char == 'au': ret_val = 'औ'

    # --- Single Latin Consonants ---
    if char == 'k': ret_val = 'क'
    if char == 'g': ret_val = 'ग'
    if char == 'c': ret_val = 'च'
    if char == 'j': ret_val = 'ज'
    if char == 'z': ret_val = 'ज़'
    if char == 't': ret_val = 'त'
    if char == 'd': ret_val = 'द'
    if char == 'n': ret_val = 'न'
    if char == 'p': ret_val = 'प'
    if char == 'f': ret_val = 'फ़'
    if char == 'b': ret_val = 'ब'
    if char == 'm': ret_val = 'म'
    if char == 'y': ret_val = 'य'
    if char == 'r': ret_val = 'र'
    if char == 'l': ret_val = 'ल'
    if char == 'v': ret_val = 'व'
    if char == 's': ret_val = 'स'
    if char == 'h': ret_val = 'ह'

    # --- Single Latin Consonants with Diacritics ---
    if char == u'\u1e45': ret_val = 'ङ' # ṅ
    if char == u'\u00f1': ret_val = 'ञ' # ñ
    if char == u'\u1e6d': ret_val = 'ट' # ṭ
    if char == u'\u1e0d': ret_val = 'ड' # ḍ
    if char == u'\u1e5b': ret_val = 'ड़' # ṛ
    if char == u'\u1e47': ret_val = 'ण' # ṇ
    if char == u'\u015b': ret_val = 'श' # ś
    if char == u'\u1e63': ret_val = 'ष' # ṣ

    # --- Double Latin Consonants ---
    #if char == 'kh': ret_val = 'ख'
    #if char == 'gh': ret_val = 'घ'
    #if char == 'ch': ret_val = 'छ'
    #if char == 'jh': ret_val = 'झ'
    #if char == 'th': ret_val = 'थ'
    #if char == 'dh': ret_val = 'ध'
    #if char == 'ph': ret_val = 'फ'
    #if char == 'bh': ret_val = 'भ'

    if char == 'ṭh'.decode('utf-8'): ret_val = 'ठ'
    if char == 'ḍh'.decode('utf-8'): ret_val = 'ढ'
    if char == 'ṛh'.decode('utf-8'): ret_val = 'ढ़'

    if char == 'll': ret_val = 'ळ'

    return ret_val


def translit_maatra(char):

    # --- Latin Single Vowels ---
    if char == 'i': ret_val = 'ि' # i
    if char == 'u': ret_val = 'ु' # u
    if char == 'e': ret_val = 'े'
    if char == 'o': ret_val = 'ो'

    # --- Latin Vowels with Diacritics ---
    if char == u'\u0101': ret_val = 'ा' # ā
    if char == u'\u01e1': ret_val = 'ॉ' # ǡ
    if char == u'\u012b': ret_val = 'ी' # ī
    if char == u'\u016b': ret_val = 'ू' # ū
    if char == u'\u1e5b': ret_val = 'ृ' # ṛ

    # --- Latin Diftongs ---
    #if char == 'ai': ret_val = 'ै'
    #if char == 'ou': ret_val = 'ौ'

    def translit_conjuncts(A, B):
        if A == 'क' and B == 'क': ret_val = 'क्क'
        if A == 'स' and B == 'त': ret_val ='स्त'

    return ret_val

def latin_to_deva(word):

    word = word.decode('utf-8')

    char_buffer = ''
    for i, char in enumerate(word):

        # --- if char is first character in word ---
        if word[0]:
            char_buffer + translit_char(char)

        if char in consonants:
            prev_char = word[i - 1]

            # --- process conjuncts consonants ---
            #--- st ---
            if char == 't' and prev_char == 's':
                char_buffer = char_buffer[:-3]
                char_buffer = char_buffer + 'स्त'

            # --- process aspirated consonants ---
            # --- kh ---
            if char == 'h' and prev_char == 'k':
                char_buffer = char_buffer + translit_char(char)
                char_buffer = char_buffer[:-6]
                char_buffer = char_buffer + 'ख'
            # --- gh ---
            if char == 'h' and prev_char == 'g':
                char_buffer = char_buffer + translit_char(char)
                char_buffer = char_buffer[:-6]
                char_buffer = char_buffer + 'घ'
            # --- ch ---
            if char == 'h' and prev_char == 'c':
                char_buffer = char_buffer + translit_char(char)
                char_buffer = char_buffer[:-6]
                char_buffer = char_buffer + 'छ'
            # --- jh ---
            if char == 'h' and prev_char == 'j':
                char_buffer = char_buffer + translit_char(char)
                char_buffer = char_buffer[:-6]
                char_buffer = char_buffer + 'झ'
            # --- th ---
            if char == 'h' and prev_char == 't':
                char_buffer = char_buffer + translit_char(char)
                char_buffer = char_buffer[:-6]
                char_buffer = char_buffer + 'थ'
            # --- dh ---
            if char == 'h' and prev_char == 'd':
                char_buffer = char_buffer + translit_char(char)
                char_buffer = char_buffer[:-6]
                char_buffer = char_buffer + 'ध'
            # --- ph ---
            if char == 'h' and prev_char == 'p':
                char_buffer = char_buffer + translit_char(char)
                char_buffer = char_buffer[:-6]
                char_buffer = char_buffer + 'फ'
            # --- bh ---
            if char == 'h' and prev_char == 'b':
                char_buffer = char_buffer + translit_char(char)
                char_buffer = char_buffer[:-6]
                char_buffer = char_buffer + 'भ'
            if char == 'h':
                next
            else:
                char_buffer = char_buffer + translit_char(char)

        if char in vowels:
            prev_char = word[i - 1]

            # --- process diftongs ---
            # -- ai --
            if char == 'i' and prev_char == 'a':
                char_buffer = char_buffer + 'ै'
            # --- ou ---
            elif char == 'u' and prev_char == 'o':
                char_buffer = char_buffer[:-3]
                char_buffer = char_buffer + 'ौ'
            # --- process maatras ---
            elif prev_char in consonants:
                # process default a
                if char == 'a':
                    pass
                else:
                    char_buffer = char_buffer + translit_maatra(char)
            else:
                char_buffer = char_buffer + 'xxx'

        else: # USE THIS FOR CAPTURING UNRECOGNIZED CHARS
            pass
            #if char == 'u00f1':
            #    char_buffer = char_buffer + translit_maatra(char)
            #    break
            #else:
            #    #char_buffer = char_buffer + u'\u00f1'.encode('utf-8')
            #    char_buffer = char_buffer + 'xxx'
            #    break

    return char_buffer

# CALL:
# --- Functioning ---
#call = 'āṣidhṛdak' # ñidhīd
#call_utf8 = call.decode('utf-8')
#print latin_to_deva(call_utf8)

# Test
#call = 'āṣidhṛdak' # ñidhīd
#call_utf8 = call.decode('utf-8')
print latin_to_deva('namaste')


# ī
# ā, ǡ, ī, ū, ṛ
# ṅ, ñ, ṭ, ḍ, ṛ, ṇ, ś, ṣ