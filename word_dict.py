# -*- coding: utf-8 -*-

upper_c = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
lower_c = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
# ṅ, ñ, ṭ, ḍ, ṛ, ṇ, ś, ṣ
lower_c_diacritics = [u'\u1e45', u'\u00f1', u'\u1e6d', u'\u1e0d', u'\u1e5b', u'\u1e47', u'\u015b', u'\u1e63']
aspirated_consonants = ['kh', 'gh', 'ch', 'jh', 'th', 'dh', 'ph', 'bh', u'ṭh', u'ḍh', u'ṛh']

upper_v = ['A', 'E', 'I', 'O', 'U', 'Y']
lower_v = ['a', 'i', 'o', 'u', 'e', 'y']
lower_v_diacritics = [u'\u0101', u'\u01e1', u'\u012b', u'\u016b', u'\u1e5b', u'\u00f5']  # ā, ǡ, ī, ū, ṛ, õ

vowels = upper_v + lower_v + lower_v_diacritics
consonants = upper_c + lower_c + lower_c_diacritics + aspirated_consonants

diftongs = ['ai', 'au', u'aĩ']

conjunct_tuple_list = [
    (u'k', u'k'), (u'k', u'kh'), (u'k', u'g'), (u'k', u'gh'), (u'k', u'ṅ'), (u'k', u'c'), (u'k', u'ch'), (u'k', u'j'),
    (u'k', u'z'), (u'k', u'jh'), (u'k', u'ñ'), (u'k', u'ṭ'), (u'k', u'ṭh'), (u'k', u'ḍ'), (u'k', u'ṛ'), (u'k', u'ḍh'),
    (u'k', u'ṛh'), (u'k', u'ṇ'), (u'k', u't'), (u'k', u'th'), (u'k', u'd'), (u'k', u'dh'), (u'k', u'n'), (u'k', u'p'),
    (u'k', u'ph'), (u'k', u'f'), (u'k', u'b'), (u'k', u'bh'), (u'k', u'm'), (u'k', u'y'), (u'k', u'r'), (u'k', u'l'),
    (u'k', u'v'), (u'k', u'ś'), (u'k', u'ṣ'), (u'k', u's'), (u'k', u'h'), (u'k', u'ḷ'), (u'k', u'kṣ'), (u'k', u'jñ'),

    (u'kh', u'k'), (u'kh', u'kh'), (u'kh', u'g'), (u'kh', u'gh'), (u'kh', u'ṅ'), (u'kh', u'c'), (u'kh', u'ch'), (u'kh', u'j'),
    (u'kh', u'z'), (u'kh', u'jh'), (u'kh', u'ñ'), (u'kh', u'ṭ'), (u'kh', u'ṭh'), (u'kh', u'ḍ'), (u'kh', u'ṛ'), (u'kh', u'ḍh'),
    (u'kh', u'ṛh'), (u'kh', u'ṇ'), (u'kh', u't'), (u'kh', u'th'), (u'kh', u'd'), (u'kh', u'dh'), (u'kh', u'n'), (u'kh', u'p'),
    (u'kh', u'ph'), (u'kh', u'f'), (u'kh', u'b'), (u'kh', u'bh'), (u'kh', u'm'), (u'kh', u'y'), (u'kh', u'r'), (u'kh', u'l'),
    (u'kh', u'v'), (u'kh', u'ś'), (u'kh', u'ṣ'), (u'kh', u's'), (u'kh', u'h'), (u'kh', u'ḷ'), (u'kh', u'kṣ'), (u'kh', u'jñ'),

    (u'g', u'k'), (u'g', u'kh'), (u'g', u'g'), (u'g', u'gh'), (u'g', u'ṅ'), (u'g', u'c'), (u'g', u'ch'), (u'g', u'j'),
    (u'g', u'z'), (u'g', u'jh'), (u'g', u'ñ'), (u'g', u'ṭ'), (u'g', u'ṭh'), (u'g', u'ḍ'), (u'g', u'ṛ'), (u'g', u'ḍh'),
    (u'g', u'ṛh'), (u'g', u'ṇ'), (u'g', u't'), (u'g', u'th'), (u'g', u'd'), (u'g', u'dh'), (u'g', u'n'), (u'g', u'p'),
    (u'g', u'ph'), (u'g', u'f'), (u'g', u'b'), (u'g', u'bh'), (u'g', u'm'), (u'g', u'y'), (u'g', u'r'), (u'g', u'l'),
    (u'g', u'v'), (u'g', u'ś'), (u'g', u'ṣ'), (u'g', u's'), (u'g', u'h'), (u'g', u'ḷ'), (u'g', u'kṣ'), (u'g', u'jñ'),

    (u'gh', u'k'), (u'gh', u'kh'), (u'gh', u'g'), (u'gh', u'gh'), (u'gh', u'ṅ'), (u'gh', u'c'), (u'gh', u'ch'), (u'gh', u'j'),
    (u'gh', u'z'), (u'gh', u'jh'), (u'gh', u'ñ'), (u'gh', u'ṭ'), (u'gh', u'ṭh'), (u'gh', u'ḍ'), (u'gh', u'ṛ'), (u'gh', u'ḍh'),
    (u'gh', u'ṛh'), (u'gh', u'ṇ'), (u'gh', u't'), (u'gh', u'th'), (u'gh', u'd'), (u'gh', u'dh'), (u'gh', u'n'), (u'gh', u'p'),
    (u'gh', u'ph'), (u'gh', u'f'), (u'gh', u'b'), (u'gh', u'bh'), (u'gh', u'm'), (u'gh', u'y'), (u'gh', u'r'), (u'gh', u'l'),
    (u'gh', u'v'), (u'gh', u'ś'), (u'gh', u'ṣ'), (u'gh', u's'), (u'gh', u'h'), (u'gh', u'ḷ'), (u'gh', u'kṣ'), (u'gh', u'jñ'),

    (u'ṅ', u'k'), (u'ṅ', u'kh'), (u'ṅ', u'g'), (u'ṅ', u'gh'), (u'ṅ', u'ṅ'), (u'ṅ', u'c'), (u'ṅ', u'ch'), (u'ṅ', u'j'),
    (u'ṅ', u'z'), (u'ṅ', u'jh'), (u'ṅ', u'ñ'), (u'ṅ', u'ṭ'), (u'ṅ', u'ṭh'), (u'ṅ', u'ḍ'), (u'ṅ', u'ṛ'), (u'ṅ', u'ḍh'),
    (u'ṅ', u'ṛh'), (u'ṅ', u'ṇ'), (u'ṅ', u't'), (u'ṅ', u'th'), (u'ṅ', u'd'), (u'ṅ', u'dh'), (u'ṅ', u'n'), (u'ṅ', u'p'),
    (u'ṅ', u'ph'), (u'ṅ', u'f'), (u'ṅ', u'b'), (u'ṅ', u'bh'), (u'ṅ', u'm'), (u'ṅ', u'y'), (u'ṅ', u'r'), (u'ṅ', u'l'),
    (u'ṅ', u'v'), (u'ṅ', u'ś'), (u'ṅ', u'ṣ'), (u'ṅ', u's'), (u'ṅ', u'h'), (u'ṅ', u'ḷ'), (u'ṅ', u'kṣ'), (u'ṅ', u'jñ'),

    (u'c', u'k'), (u'c', u'kh'), (u'c', u'g'), (u'c', u'gh'), (u'c', u'ṅ'), (u'c', u'c'), (u'c', u'ch'), (u'c', u'j'),
    (u'c', u'z'), (u'c', u'jh'), (u'c', u'ñ'), (u'c', u'ṭ'), (u'c', u'ṭh'), (u'c', u'ḍ'), (u'c', u'ṛ'), (u'c', u'ḍh'),
    (u'c', u'ṛh'), (u'c', u'ṇ'), (u'c', u't'), (u'c', u'th'), (u'c', u'd'), (u'c', u'dh'), (u'c', u'n'), (u'c', u'p'),
    (u'c', u'ph'), (u'c', u'f'), (u'c', u'b'), (u'c', u'bh'), (u'c', u'm'), (u'c', u'y'), (u'c', u'r'), (u'c', u'l'),
    (u'c', u'v'), (u'c', u'ś'), (u'c', u'ṣ'), (u'c', u's'), (u'c', u'h'), (u'c', u'ḷ'), (u'c', u'kṣ'), (u'c', u'jñ'),

    (u'ch', u'k'), (u'ch', u'kh'), (u'ch', u'g'), (u'ch', u'gh'), (u'ch', u'ṅ'), (u'ch', u'c'), (u'ch', u'ch'), (u'ch', u'j'),
    (u'ch', u'z'), (u'ch', u'jh'), (u'ch', u'ñ'), (u'ch', u'ṭ'), (u'ch', u'ṭh'), (u'ch', u'ḍ'), (u'ch', u'ṛ'), (u'ch', u'ḍh'),
    (u'ch', u'ṛh'), (u'ch', u'ṇ'), (u'ch', u't'), (u'ch', u'th'), (u'ch', u'd'), (u'ch', u'dh'), (u'ch', u'n'), (u'ch', u'p'),
    (u'ch', u'ph'), (u'ch', u'f'), (u'ch', u'b'), (u'ch', u'bh'), (u'ch', u'm'), (u'ch', u'y'), (u'ch', u'r'), (u'ch', u'l'),
    (u'ch', u'v'), (u'ch', u'ś'), (u'ch', u'ṣ'), (u'ch', u's'), (u'ch', u'h'), (u'ch', u'ḷ'), (u'ch', u'kṣ'), (u'ch', u'jñ'),

    (u'j', u'k'), (u'j', u'kh'), (u'j', u'g'), (u'j', u'gh'), (u'j', u'ṅ'), (u'j', u'c'), (u'j', u'ch'), (u'j', u'j'),
    (u'j', u'z'), (u'j', u'jh'), (u'j', u'ñ'), (u'j', u'ṭ'), (u'j', u'ṭh'), (u'j', u'ḍ'), (u'j', u'ṛ'), (u'j', u'ḍh'),
    (u'j', u'ṛh'), (u'j', u'ṇ'), (u'j', u't'), (u'j', u'th'), (u'j', u'd'), (u'j', u'dh'), (u'j', u'n'), (u'j', u'p'),
    (u'j', u'ph'), (u'j', u'f'), (u'j', u'b'), (u'j', u'bh'), (u'j', u'm'), (u'j', u'y'), (u'j', u'r'), (u'j', u'l'),
    (u'j', u'v'), (u'j', u'ś'), (u'j', u'ṣ'), (u'j', u's'), (u'j', u'h'), (u'j', u'ḷ'), (u'j', u'kṣ'), (u'j', u'jñ'),

    (u'z', u'k'), (u'z', u'kh'), (u'z', u'g'), (u'z', u'gh'), (u'z', u'ṅ'), (u'z', u'c'), (u'z', u'ch'), (u'z', u'j'),
    (u'z', u'z'), (u'z', u'jh'), (u'z', u'ñ'), (u'z', u'ṭ'), (u'z', u'ṭh'), (u'z', u'ḍ'), (u'z', u'ṛ'), (u'z', u'ḍh'),
    (u'z', u'ṛh'), (u'z', u'ṇ'), (u'z', u't'), (u'z', u'th'), (u'z', u'd'), (u'z', u'dh'), (u'z', u'n'), (u'z', u'p'),
    (u'z', u'ph'), (u'z', u'f'), (u'z', u'b'), (u'z', u'bh'), (u'z', u'm'), (u'z', u'y'), (u'z', u'r'), (u'z', u'l'),
    (u'z', u'v'), (u'z', u'ś'), (u'z', u'ṣ'), (u'z', u's'), (u'z', u'h'), (u'z', u'ḷ'), (u'z', u'kṣ'), (u'z', u'jñ'),

    (u'jh', u'k'), (u'jh', u'kh'), (u'jh', u'g'), (u'jh', u'gh'), (u'jh', u'ṅ'), (u'jh', u'c'), (u'jh', u'ch'), (u'jh', u'j'),
    (u'jh', u'z'), (u'jh', u'jh'), (u'jh', u'ñ'), (u'jh', u'ṭ'), (u'jh', u'ṭh'), (u'jh', u'ḍ'), (u'jh', u'ṛ'), (u'jh', u'ḍh'),
    (u'jh', u'ṛh'), (u'jh', u'ṇ'), (u'jh', u't'), (u'jh', u'th'), (u'jh', u'd'), (u'jh', u'dh'), (u'jh', u'n'), (u'jh', u'p'),
    (u'jh', u'ph'), (u'jh', u'f'), (u'jh', u'b'), (u'jh', u'bh'), (u'jh', u'm'), (u'jh', u'y'), (u'jh', u'r'), (u'jh', u'l'),
    (u'jh', u'v'), (u'jh', u'ś'), (u'jh', u'ṣ'), (u'jh', u's'), (u'jh', u'h'), (u'jh', u'ḷ'), (u'jh', u'kṣ'), (u'jh', u'jñ'),

    (u'ñ', u'k'), (u'ñ', u'kh'), (u'ñ', u'g'), (u'ñ', u'gh'), (u'ñ', u'ṅ'), (u'ñ', u'c'), (u'ñ', u'ch'), (u'ñ', u'j'),
    (u'ñ', u'z'), (u'ñ', u'jh'), (u'ñ', u'ñ'), (u'ñ', u'ṭ'), (u'ñ', u'ṭh'), (u'ñ', u'ḍ'), (u'ñ', u'ṛ'), (u'ñ', u'ḍh'),
    (u'ñ', u'ṛh'), (u'ñ', u'ṇ'), (u'ñ', u't'), (u'ñ', u'th'), (u'ñ', u'd'), (u'ñ', u'dh'), (u'ñ', u'n'), (u'ñ', u'p'),
    (u'ñ', u'ph'), (u'ñ', u'f'), (u'ñ', u'b'), (u'ñ', u'bh'), (u'ñ', u'm'), (u'ñ', u'y'), (u'ñ', u'r'), (u'ñ', u'l'),
    (u'ñ', u'v'), (u'ñ', u'ś'), (u'ñ', u'ṣ'), (u'ñ', u's'), (u'ñ', u'h'), (u'ñ', u'ḷ'), (u'ñ', u'kṣ'), (u'ñ', u'jñ'),

    (u'ṭ', u'k'), (u'ṭ', u'kh'), (u'ṭ', u'g'), (u'ṭ', u'gh'), (u'ṭ', u'ṅ'), (u'ṭ', u'c'), (u'ṭ', u'ch'), (u'ṭ', u'j'),
    (u'ṭ', u'z'), (u'ṭ', u'jh'), (u'ṭ', u'ñ'), (u'ṭ', u'ṭ'), (u'ṭ', u'ṭh'), (u'ṭ', u'ḍ'), (u'ṭ', u'ṛ'), (u'ṭ', u'ḍh'),
    (u'ṭ', u'ṛh'), (u'ṭ', u'ṇ'), (u'ṭ', u't'), (u'ṭ', u'th'), (u'ṭ', u'd'), (u'ṭ', u'dh'), (u'ṭ', u'n'), (u'ṭ', u'p'),
    (u'ṭ', u'ph'), (u'ṭ', u'f'), (u'ṭ', u'b'), (u'ṭ', u'bh'), (u'ṭ', u'm'), (u'ṭ', u'y'), (u'ṭ', u'r'), (u'ṭ', u'l'),
    (u'ṭ', u'v'), (u'ṭ', u'ś'), (u'ṭ', u'ṣ'), (u'ṭ', u's'), (u'ṭ', u'h'), (u'ṭ', u'ḷ'), (u'ṭ', u'kṣ'), (u'ṭ', u'jñ'),

    (u'ṭh', u'k'), (u'ṭh', u'kh'), (u'ṭh', u'g'), (u'ṭh', u'gh'), (u'ṭh', u'ṅ'), (u'ṭh', u'c'), (u'ṭh', u'ch'), (u'ṭh', u'j'),
    (u'ṭh', u'z'), (u'ṭh', u'jh'), (u'ṭh', u'ñ'), (u'ṭh', u'ṭ'), (u'ṭh', u'ṭh'), (u'ṭh', u'ḍ'), (u'ṭh', u'ṛ'), (u'ṭh', u'ḍh'),
    (u'ṭh', u'ṛh'), (u'ṭh', u'ṇ'), (u'ṭh', u't'), (u'ṭh', u'th'), (u'ṭh', u'd'), (u'ṭh', u'dh'), (u'ṭh', u'n'), (u'ṭh', u'p'),
    (u'ṭh', u'ph'), (u'ṭh', u'f'), (u'ṭh', u'b'), (u'ṭh', u'bh'), (u'ṭh', u'm'), (u'ṭh', u'y'), (u'ṭh', u'r'), (u'ṭh', u'l'),
    (u'ṭh', u'v'), (u'ṭh', u'ś'), (u'ṭh', u'ṣ'), (u'ṭh', u's'), (u'ṭh', u'h'), (u'ṭh', u'ḷ'), (u'ṭh', u'kṣ'), (u'ṭh', u'jñ'),

    (u'ḍ', u'k'), (u'ḍ', u'kh'), (u'ḍ', u'g'), (u'ḍ', u'gh'), (u'ḍ', u'ṅ'), (u'ḍ', u'c'), (u'ḍ', u'ch'), (u'ḍ', u'j'),
    (u'ḍ', u'z'), (u'ḍ', u'jh'), (u'ḍ', u'ñ'), (u'ḍ', u'ṭ'), (u'ḍ', u'ṭh'), (u'ḍ', u'ḍ'), (u'ḍ', u'ṛ'), (u'ḍ', u'ḍh'),
    (u'ḍ', u'ṛh'), (u'ḍ', u'ṇ'), (u'ḍ', u't'), (u'ḍ', u'th'), (u'ḍ', u'd'), (u'ḍ', u'dh'), (u'ḍ', u'n'), (u'ḍ', u'p'),
    (u'ḍ', u'ph'), (u'ḍ', u'f'), (u'ḍ', u'b'), (u'ḍ', u'bh'), (u'ḍ', u'm'), (u'ḍ', u'y'), (u'ḍ', u'r'), (u'ḍ', u'l'),
    (u'ḍ', u'v'), (u'ḍ', u'ś'), (u'ḍ', u'ṣ'), (u'ḍ', u's'), (u'ḍ', u'h'), (u'ḍ', u'ḷ'), (u'ḍ', u'kṣ'), (u'ḍ', u'jñ'),

    (u'ṛ', u'k'), (u'ṛ', u'kh'), (u'ṛ', u'g'), (u'ṛ', u'gh'), (u'ṛ', u'ṅ'), (u'ṛ', u'c'), (u'ṛ', u'ch'), (u'ṛ', u'j'),
    (u'ṛ', u'z'), (u'ṛ', u'jh'), (u'ṛ', u'ñ'), (u'ṛ', u'ṭ'), (u'ṛ', u'ṭh'), (u'ṛ', u'ḍ'), (u'ṛ', u'ṛ'), (u'ṛ', u'ḍh'),
    (u'ṛ', u'ṛh'), (u'ṛ', u'ṇ'), (u'ṛ', u't'), (u'ṛ', u'th'), (u'ṛ', u'd'), (u'ṛ', u'dh'), (u'ṛ', u'n'), (u'ṛ', u'p'),
    (u'ṛ', u'ph'), (u'ṛ', u'f'), (u'ṛ', u'b'), (u'ṛ', u'bh'), (u'ṛ', u'm'), (u'ṛ', u'y'), (u'ṛ', u'r'), (u'ṛ', u'l'),
    (u'ṛ', u'v'), (u'ṛ', u'ś'), (u'ṛ', u'ṣ'), (u'ṛ', u's'), (u'ṛ', u'h'), (u'ṛ', u'ḷ'), (u'ṛ', u'kṣ'), (u'ṛ', u'jñ'),

    (u'ḍh', u'k'), (u'ḍh', u'kh'), (u'ḍh', u'g'), (u'ḍh', u'gh'), (u'ḍh', u'ṅ'), (u'ḍh', u'c'), (u'ḍh', u'ch'), (u'ḍh', u'j'),
    (u'ḍh', u'z'), (u'ḍh', u'jh'), (u'ḍh', u'ñ'), (u'ḍh', u'ṭ'), (u'ḍh', u'ṭh'), (u'ḍh', u'ḍ'), (u'ḍh', u'ṛ'), (u'ḍh', u'ḍh'),
    (u'ḍh', u'ṛh'), (u'ḍh', u'ṇ'), (u'ḍh', u't'), (u'ḍh', u'th'), (u'ḍh', u'd'), (u'ḍh', u'dh'), (u'ḍh', u'n'), (u'ḍh', u'p'),
    (u'ḍh', u'ph'), (u'ḍh', u'f'), (u'ḍh', u'b'), (u'ḍh', u'bh'), (u'ḍh', u'm'), (u'ḍh', u'y'), (u'ḍh', u'r'), (u'ḍh', u'l'),
    (u'ḍh', u'v'), (u'ḍh', u'ś'), (u'ḍh', u'ṣ'), (u'ḍh', u's'), (u'ḍh', u'h'), (u'ḍh', u'ḷ'), (u'ḍh', u'kṣ'), (u'ḍh', u'jñ'),

    (u'ṛh', u'k'), (u'ṛh', u'kh'), (u'ṛh', u'g'), (u'ṛh', u'gh'), (u'ṛh', u'ṅ'), (u'ṛh', u'c'), (u'ṛh', u'ch'), (u'ṛh', u'j'),
    (u'ṛh', u'z'), (u'ṛh', u'jh'), (u'ṛh', u'ñ'), (u'ṛh', u'ṭ'), (u'ṛh', u'ṭh'), (u'ṛh', u'ḍ'), (u'ṛh', u'ṛ'), (u'ṛh', u'ḍh'),
    (u'ṛh', u'ṛh'), (u'ṛh', u'ṇ'), (u'ṛh', u't'), (u'ṛh', u'th'), (u'ṛh', u'd'), (u'ṛh', u'dh'), (u'ṛh', u'n'), (u'ṛh', u'p'),
    (u'ṛh', u'ph'), (u'ṛh', u'f'), (u'ṛh', u'b'), (u'ṛh', u'bh'), (u'ṛh', u'm'), (u'ṛh', u'y'), (u'ṛh', u'r'), (u'ṛh', u'l'),
    (u'ṛh', u'v'), (u'ṛh', u'ś'), (u'ṛh', u'ṣ'), (u'ṛh', u's'), (u'ṛh', u'h'), (u'ṛh', u'ḷ'), (u'ṛh', u'kṣ'), (u'ṛh', u'jñ'),

    (u'ṇ', u'k'), (u'ṇ', u'kh'), (u'ṇ', u'g'), (u'ṇ', u'gh'), (u'ṇ', u'ṅ'), (u'ṇ', u'c'), (u'ṇ', u'ch'), (u'ṇ', u'j'),
    (u'ṇ', u'z'), (u'ṇ', u'jh'), (u'ṇ', u'ñ'), (u'ṇ', u'ṭ'), (u'ṇ', u'ṭh'), (u'ṇ', u'ḍ'), (u'ṇ', u'ṛ'), (u'ṇ', u'ḍh'),
    (u'ṇ', u'ṛh'), (u'ṇ', u'ṇ'), (u'ṇ', u't'), (u'ṇ', u'th'), (u'ṇ', u'd'), (u'ṇ', u'dh'), (u'ṇ', u'n'), (u'ṇ', u'p'),
    (u'ṇ', u'ph'), (u'ṇ', u'f'), (u'ṇ', u'b'), (u'ṇ', u'bh'), (u'ṇ', u'm'), (u'ṇ', u'y'), (u'ṇ', u'r'), (u'ṇ', u'l'),
    (u'ṇ', u'v'), (u'ṇ', u'ś'), (u'ṇ', u'ṣ'), (u'ṇ', u's'), (u'ṇ', u'h'), (u'ṇ', u'ḷ'), (u'ṇ', u'kṣ'), (u'ṇ', u'jñ'),

    (u't', u'k'), (u't', u'kh'), (u't', u'g'), (u't', u'gh'), (u't', u'ṅ'), (u't', u'c'), (u't', u'ch'), (u't', u'j'),
    (u't', u'z'), (u't', u'jh'), (u't', u'ñ'), (u't', u'ṭ'), (u't', u'ṭh'), (u't', u'ḍ'), (u't', u'ṛ'), (u't', u'ḍh'),
    (u't', u'ṛh'), (u't', u'ṇ'), (u't', u't'), (u't', u'th'), (u't', u'd'), (u't', u'dh'), (u't', u'n'), (u't', u'p'),
    (u't', u'ph'), (u't', u'f'), (u't', u'b'), (u't', u'bh'), (u't', u'm'), (u't', u'y'), (u't', u'r'), (u't', u'l'),
    (u't', u'v'), (u't', u'ś'), (u't', u'ṣ'), (u't', u's'), (u't', u'h'), (u't', u'ḷ'), (u't', u'kṣ'), (u't', u'jñ'),

    (u'th', u'k'), (u'th', u'kh'), (u'th', u'g'), (u'th', u'gh'), (u'th', u'ṅ'), (u'th', u'c'), (u'th', u'ch'), (u'th', u'j'),
    (u'th', u'z'), (u'th', u'jh'), (u'th', u'ñ'), (u'th', u'ṭ'), (u'th', u'ṭh'), (u'th', u'ḍ'), (u'th', u'ṛ'), (u'th', u'ḍh'),
    (u'th', u'ṛh'), (u'th', u'ṇ'), (u'th', u't'), (u'th', u'th'), (u'th', u'd'), (u'th', u'dh'), (u'th', u'n'), (u'th', u'p'),
    (u'th', u'ph'), (u'th', u'f'), (u'th', u'b'), (u'th', u'bh'), (u'th', u'm'), (u'th', u'y'), (u'th', u'r'), (u'th', u'l'),
    (u'th', u'v'), (u'th', u'ś'), (u'th', u'ṣ'), (u'th', u's'), (u'th', u'h'), (u'th', u'ḷ'), (u'th', u'kṣ'), (u'th', u'jñ'),

    (u'd', u'k'), (u'd', u'kh'), (u'd', u'g'), (u'd', u'gh'), (u'd', u'ṅ'), (u'd', u'c'), (u'd', u'ch'), (u'd', u'j'),
    (u'd', u'z'), (u'd', u'jh'), (u'd', u'ñ'), (u'd', u'ṭ'), (u'd', u'ṭh'), (u'd', u'ḍ'), (u'd', u'ṛ'), (u'd', u'ḍh'),
    (u'd', u'ṛh'), (u'd', u'ṇ'), (u'd', u't'), (u'd', u'th'), (u'd', u'd'), (u'd', u'dh'), (u'd', u'n'), (u'd', u'p'),
    (u'd', u'ph'), (u'd', u'f'), (u'd', u'b'), (u'd', u'bh'), (u'd', u'm'), (u'd', u'y'), (u'd', u'r'), (u'd', u'l'),
    (u'd', u'v'), (u'd', u'ś'), (u'd', u'ṣ'), (u'd', u's'), (u'd', u'h'), (u'd', u'ḷ'), (u'd', u'kṣ'), (u'd', u'jñ'),

    (u'dh', u'k'), (u'dh', u'kh'), (u'dh', u'g'), (u'dh', u'gh'), (u'dh', u'ṅ'), (u'dh', u'c'), (u'dh', u'ch'), (u'dh', u'j'),
    (u'dh', u'z'), (u'dh', u'jh'), (u'dh', u'ñ'), (u'dh', u'ṭ'), (u'dh', u'ṭh'), (u'dh', u'ḍ'), (u'dh', u'ṛ'), (u'dh', u'ḍh'),
    (u'dh', u'ṛh'), (u'dh', u'ṇ'), (u'dh', u't'), (u'dh', u'th'), (u'dh', u'd'), (u'dh', u'dh'), (u'dh', u'n'), (u'dh', u'p'),
    (u'dh', u'ph'), (u'dh', u'f'), (u'dh', u'b'), (u'dh', u'bh'), (u'dh', u'm'), (u'dh', u'y'), (u'dh', u'r'), (u'dh', u'l'),
    (u'dh', u'v'), (u'dh', u'ś'), (u'dh', u'ṣ'), (u'dh', u's'), (u'dh', u'h'), (u'dh', u'ḷ'), (u'dh', u'kṣ'), (u'dh', u'jñ'),

    (u'n', u'k'), (u'n', u'kh'), (u'n', u'g'), (u'n', u'gh'), (u'n', u'ṅ'), (u'n', u'c'), (u'n', u'ch'), (u'n', u'j'),
    (u'n', u'z'), (u'n', u'jh'), (u'n', u'ñ'), (u'n', u'ṭ'), (u'n', u'ṭh'), (u'n', u'ḍ'), (u'n', u'ṛ'), (u'n', u'ḍh'),
    (u'n', u'ṛh'), (u'n', u'ṇ'), (u'n', u't'), (u'n', u'th'), (u'n', u'd'), (u'n', u'dh'), (u'n', u'n'), (u'n', u'p'),
    (u'n', u'ph'), (u'n', u'f'), (u'n', u'b'), (u'n', u'bh'), (u'n', u'm'), (u'n', u'y'), (u'n', u'r'), (u'n', u'l'),
    (u'n', u'v'), (u'n', u'ś'), (u'n', u'ṣ'), (u'n', u's'), (u'n', u'h'), (u'n', u'ḷ'), (u'n', u'kṣ'), (u'n', u'jñ'),

    (u'p', u'k'), (u'p', u'kh'), (u'p', u'g'), (u'p', u'gh'), (u'p', u'ṅ'), (u'p', u'c'), (u'p', u'ch'), (u'p', u'j'),
    (u'p', u'z'), (u'p', u'jh'), (u'p', u'ñ'), (u'p', u'ṭ'), (u'p', u'ṭh'), (u'p', u'ḍ'), (u'p', u'ṛ'), (u'p', u'ḍh'),
    (u'p', u'ṛh'), (u'p', u'ṇ'), (u'p', u't'), (u'p', u'th'), (u'p', u'd'), (u'p', u'dh'), (u'p', u'n'), (u'p', u'p'),
    (u'p', u'ph'), (u'p', u'f'), (u'p', u'b'), (u'p', u'bh'), (u'p', u'm'), (u'p', u'y'), (u'p', u'r'), (u'p', u'l'),
    (u'p', u'v'), (u'p', u'ś'), (u'p', u'ṣ'), (u'p', u's'), (u'p', u'h'), (u'p', u'ḷ'), (u'p', u'kṣ'), (u'p', u'jñ'),

    (u'ph', u'k'), (u'ph', u'kh'), (u'ph', u'g'), (u'ph', u'gh'), (u'ph', u'ṅ'), (u'ph', u'c'), (u'ph', u'ch'), (u'ph', u'j'),
    (u'ph', u'z'), (u'ph', u'jh'), (u'ph', u'ñ'), (u'ph', u'ṭ'), (u'ph', u'ṭh'), (u'ph', u'ḍ'), (u'ph', u'ṛ'), (u'ph', u'ḍh'),
    (u'ph', u'ṛh'), (u'ph', u'ṇ'), (u'ph', u't'), (u'ph', u'th'), (u'ph', u'd'), (u'ph', u'dh'), (u'ph', u'n'), (u'ph', u'p'),
    (u'ph', u'ph'), (u'ph', u'f'), (u'ph', u'b'), (u'ph', u'bh'), (u'ph', u'm'), (u'ph', u'y'), (u'ph', u'r'), (u'ph', u'l'),
    (u'ph', u'v'), (u'ph', u'ś'), (u'ph', u'ṣ'), (u'ph', u's'), (u'ph', u'h'), (u'ph', u'ḷ'), (u'ph', u'kṣ'), (u'ph', u'jñ'),

    (u'f', u'k'), (u'f', u'kh'), (u'f', u'g'), (u'f', u'gh'), (u'f', u'ṅ'), (u'f', u'c'), (u'f', u'ch'), (u'f', u'j'),
    (u'f', u'z'), (u'f', u'jh'), (u'f', u'ñ'), (u'f', u'ṭ'), (u'f', u'ṭh'), (u'f', u'ḍ'), (u'f', u'ṛ'), (u'f', u'ḍh'),
    (u'f', u'ṛh'), (u'f', u'ṇ'), (u'f', u't'), (u'f', u'th'), (u'f', u'd'), (u'f', u'dh'), (u'f', u'n'), (u'f', u'p'),
    (u'f', u'ph'), (u'f', u'f'), (u'f', u'b'), (u'f', u'bh'), (u'f', u'm'), (u'f', u'y'), (u'f', u'r'), (u'f', u'l'),
    (u'f', u'v'), (u'f', u'ś'), (u'f', u'ṣ'), (u'f', u's'), (u'f', u'h'), (u'f', u'ḷ'), (u'f', u'kṣ'), (u'f', u'jñ'),

    (u'b', u'k'), (u'b', u'kh'), (u'b', u'g'), (u'b', u'gh'), (u'b', u'ṅ'), (u'b', u'c'), (u'b', u'ch'), (u'b', u'j'),
    (u'b', u'z'), (u'b', u'jh'), (u'b', u'ñ'), (u'b', u'ṭ'), (u'b', u'ṭh'), (u'b', u'ḍ'), (u'b', u'ṛ'), (u'b', u'ḍh'),
    (u'b', u'ṛh'), (u'b', u'ṇ'), (u'b', u't'), (u'b', u'th'), (u'b', u'd'), (u'b', u'dh'), (u'b', u'n'), (u'b', u'p'),
    (u'b', u'ph'), (u'b', u'f'), (u'b', u'b'), (u'b', u'bh'), (u'b', u'm'), (u'b', u'y'), (u'b', u'r'), (u'b', u'l'),
    (u'b', u'v'), (u'b', u'ś'), (u'b', u'ṣ'), (u'b', u's'), (u'b', u'h'), (u'b', u'ḷ'), (u'b', u'kṣ'), (u'b', u'jñ'),

    (u'bh', u'k'), (u'bh', u'kh'), (u'bh', u'g'), (u'bh', u'gh'), (u'bh', u'ṅ'), (u'bh', u'c'), (u'bh', u'ch'), (u'bh', u'j'),
    (u'bh', u'z'), (u'bh', u'jh'), (u'bh', u'ñ'), (u'bh', u'ṭ'), (u'bh', u'ṭh'), (u'bh', u'ḍ'), (u'bh', u'ṛ'), (u'bh', u'ḍh'),
    (u'bh', u'ṛh'), (u'bh', u'ṇ'), (u'bh', u't'), (u'bh', u'th'), (u'bh', u'd'), (u'bh', u'dh'), (u'bh', u'n'), (u'bh', u'p'),
    (u'bh', u'ph'), (u'bh', u'f'), (u'bh', u'b'), (u'bh', u'bh'), (u'bh', u'm'), (u'bh', u'y'), (u'bh', u'r'), (u'bh', u'l'),
    (u'bh', u'v'), (u'bh', u'ś'), (u'bh', u'ṣ'), (u'bh', u's'), (u'bh', u'h'), (u'bh', u'ḷ'), (u'bh', u'kṣ'), (u'bh', u'jñ'),

    (u'm', u'k'), (u'm', u'kh'), (u'm', u'g'), (u'm', u'gh'), (u'm', u'ṅ'), (u'm', u'c'), (u'm', u'ch'), (u'm', u'j'),
    (u'm', u'z'), (u'm', u'jh'), (u'm', u'ñ'), (u'm', u'ṭ'), (u'm', u'ṭh'), (u'm', u'ḍ'), (u'm', u'ṛ'), (u'm', u'ḍh'),
    (u'm', u'ṛh'), (u'm', u'ṇ'), (u'm', u't'), (u'm', u'th'), (u'm', u'd'), (u'm', u'dh'), (u'm', u'n'), (u'm', u'p'),
    (u'm', u'ph'), (u'm', u'f'), (u'm', u'b'), (u'm', u'bh'), (u'm', u'm'), (u'm', u'y'), (u'm', u'r'), (u'm', u'l'),
    (u'm', u'v'), (u'm', u'ś'), (u'm', u'ṣ'), (u'm', u's'), (u'm', u'h'), (u'm', u'ḷ'), (u'm', u'kṣ'), (u'm', u'jñ'),

    (u'y', u'k'), (u'y', u'kh'), (u'y', u'g'), (u'y', u'gh'), (u'y', u'ṅ'), (u'y', u'c'), (u'y', u'ch'), (u'y', u'j'),
    (u'y', u'z'), (u'y', u'jh'), (u'y', u'ñ'), (u'y', u'ṭ'), (u'y', u'ṭh'), (u'y', u'ḍ'), (u'y', u'ṛ'), (u'y', u'ḍh'),
    (u'y', u'ṛh'), (u'y', u'ṇ'), (u'y', u't'), (u'y', u'th'), (u'y', u'd'), (u'y', u'dh'), (u'y', u'n'), (u'y', u'p'),
    (u'y', u'ph'), (u'y', u'f'), (u'y', u'b'), (u'y', u'bh'), (u'y', u'm'), (u'y', u'y'), (u'y', u'r'), (u'y', u'l'),
    (u'y', u'v'), (u'y', u'ś'), (u'y', u'ṣ'), (u'y', u's'), (u'y', u'h'), (u'y', u'ḷ'), (u'y', u'kṣ'), (u'y', u'jñ'),

    (u'r', u'k'), (u'r', u'kh'), (u'r', u'g'), (u'r', u'gh'), (u'r', u'ṅ'), (u'r', u'c'), (u'r', u'ch'), (u'r', u'j'),
    (u'r', u'z'), (u'r', u'jh'), (u'r', u'ñ'), (u'r', u'ṭ'), (u'r', u'ṭh'), (u'r', u'ḍ'), (u'r', u'ṛ'), (u'r', u'ḍh'),
    (u'r', u'ṛh'), (u'r', u'ṇ'), (u'r', u't'), (u'r', u'th'), (u'r', u'd'), (u'r', u'dh'), (u'r', u'n'), (u'r', u'p'),
    (u'r', u'ph'), (u'r', u'f'), (u'r', u'b'), (u'r', u'bh'), (u'r', u'm'), (u'r', u'y'), (u'r', u'r'), (u'r', u'l'),
    (u'r', u'v'), (u'r', u'ś'), (u'r', u'ṣ'), (u'r', u's'), (u'r', u'h'), (u'r', u'ḷ'), (u'r', u'kṣ'), (u'r', u'jñ'),

    (u'l', u'k'), (u'l', u'kh'), (u'l', u'g'), (u'l', u'gh'), (u'l', u'ṅ'), (u'l', u'c'), (u'l', u'ch'), (u'l', u'j'),
    (u'l', u'z'), (u'l', u'jh'), (u'l', u'ñ'), (u'l', u'ṭ'), (u'l', u'ṭh'), (u'l', u'ḍ'), (u'l', u'ṛ'), (u'l', u'ḍh'),
    (u'l', u'ṛh'), (u'l', u'ṇ'), (u'l', u't'), (u'l', u'th'), (u'l', u'd'), (u'l', u'dh'), (u'l', u'n'), (u'l', u'p'),
    (u'l', u'ph'), (u'l', u'f'), (u'l', u'b'), (u'l', u'bh'), (u'l', u'm'), (u'l', u'y'), (u'l', u'r'), (u'l', u'l'),
    (u'l', u'v'), (u'l', u'ś'), (u'l', u'ṣ'), (u'l', u's'), (u'l', u'h'), (u'l', u'ḷ'), (u'l', u'kṣ'), (u'l', u'jñ'),

    (u'v', u'k'), (u'v', u'kh'), (u'v', u'g'), (u'v', u'gh'), (u'v', u'ṅ'), (u'v', u'c'), (u'v', u'ch'), (u'v', u'j'),
    (u'v', u'z'), (u'v', u'jh'), (u'v', u'ñ'), (u'v', u'ṭ'), (u'v', u'ṭh'), (u'v', u'ḍ'), (u'v', u'ṛ'), (u'v', u'ḍh'),
    (u'v', u'ṛh'), (u'v', u'ṇ'), (u'v', u't'), (u'v', u'th'), (u'v', u'd'), (u'v', u'dh'), (u'v', u'n'), (u'v', u'p'),
    (u'v', u'ph'), (u'v', u'f'), (u'v', u'b'), (u'v', u'bh'), (u'v', u'm'), (u'v', u'y'), (u'v', u'r'), (u'v', u'l'),
    (u'v', u'v'), (u'v', u'ś'), (u'v', u'ṣ'), (u'v', u's'), (u'v', u'h'), (u'v', u'ḷ'), (u'v', u'kṣ'), (u'v', u'jñ'),

    (u'ś', u'k'), (u'ś', u'kh'), (u'ś', u'g'), (u'ś', u'gh'), (u'ś', u'ṅ'), (u'ś', u'c'), (u'ś', u'ch'), (u'ś', u'j'),
    (u'ś', u'z'), (u'ś', u'jh'), (u'ś', u'ñ'), (u'ś', u'ṭ'), (u'ś', u'ṭh'), (u'ś', u'ḍ'), (u'ś', u'ṛ'), (u'ś', u'ḍh'),
    (u'ś', u'ṛh'), (u'ś', u'ṇ'), (u'ś', u't'), (u'ś', u'th'), (u'ś', u'd'), (u'ś', u'dh'), (u'ś', u'n'), (u'ś', u'p'),
    (u'ś', u'ph'), (u'ś', u'f'), (u'ś', u'b'), (u'ś', u'bh'), (u'ś', u'm'), (u'ś', u'y'), (u'ś', u'r'), (u'ś', u'l'),
    (u'ś', u'v'), (u'ś', u'ś'), (u'ś', u'ṣ'), (u'ś', u's'), (u'ś', u'h'), (u'ś', u'ḷ'), (u'ś', u'kṣ'), (u'ś', u'jñ'),

    (u'ṣ', u'k'), (u'ṣ', u'kh'), (u'ṣ', u'g'), (u'ṣ', u'gh'), (u'ṣ', u'ṅ'), (u'ṣ', u'c'), (u'ṣ', u'ch'), (u'ṣ', u'j'),
    (u'ṣ', u'z'), (u'ṣ', u'jh'), (u'ṣ', u'ñ'), (u'ṣ', u'ṭ'), (u'ṣ', u'ṭh'), (u'ṣ', u'ḍ'), (u'ṣ', u'ṛ'), (u'ṣ', u'ḍh'),
    (u'ṣ', u'ṛh'), (u'ṣ', u'ṇ'), (u'ṣ', u't'), (u'ṣ', u'th'), (u'ṣ', u'd'), (u'ṣ', u'dh'), (u'ṣ', u'n'), (u'ṣ', u'p'),
    (u'ṣ', u'ph'), (u'ṣ', u'f'), (u'ṣ', u'b'), (u'ṣ', u'bh'), (u'ṣ', u'm'), (u'ṣ', u'y'), (u'ṣ', u'r'), (u'ṣ', u'l'),
    (u'ṣ', u'v'), (u'ṣ', u'ś'), (u'ṣ', u'ṣ'), (u'ṣ', u's'), (u'ṣ', u'h'), (u'ṣ', u'ḷ'), (u'ṣ', u'kṣ'), (u'ṣ', u'jñ'),

    (u's', u'k'), (u's', u'kh'), (u's', u'g'), (u's', u'gh'), (u's', u'ṅ'), (u's', u'c'), (u's', u'ch'), (u's', u'j'),
    (u's', u'z'), (u's', u'jh'), (u's', u'ñ'), (u's', u'ṭ'), (u's', u'ṭh'), (u's', u'ḍ'), (u's', u'ṛ'), (u's', u'ḍh'),
    (u's', u'ṛh'), (u's', u'ṇ'), (u's', u't'), (u's', u'th'), (u's', u'd'), (u's', u'dh'), (u's', u'n'), (u's', u'p'),
    (u's', u'ph'), (u's', u'f'), (u's', u'b'), (u's', u'bh'), (u's', u'm'), (u's', u'y'), (u's', u'r'), (u's', u'l'),
    (u's', u'v'), (u's', u'ś'), (u's', u'ṣ'), (u's', u's'), (u's', u'h'), (u's', u'ḷ'), (u's', u'kṣ'), (u's', u'jñ'),

    (u'h', u'k'), (u'h', u'kh'), (u'h', u'g'), (u'h', u'gh'), (u'h', u'ṅ'), (u'h', u'c'), (u'h', u'ch'), (u'h', u'j'),
    (u'h', u'z'), (u'h', u'jh'), (u'h', u'ñ'), (u'h', u'ṭ'), (u'h', u'ṭh'), (u'h', u'ḍ'), (u'h', u'ṛ'), (u'h', u'ḍh'),
    (u'h', u'ṛh'), (u'h', u'ṇ'), (u'h', u't'), (u'h', u'th'), (u'h', u'd'), (u'h', u'dh'), (u'h', u'n'), (u'h', u'p'),
    (u'h', u'ph'), (u'h', u'f'), (u'h', u'b'), (u'h', u'bh'), (u'h', u'm'), (u'h', u'y'), (u'h', u'r'), (u'h', u'l'),
    (u'h', u'v'), (u'h', u'ś'), (u'h', u'ṣ'), (u'h', u's'), (u'h', u'h'), (u'h', u'ḷ'), (u'h', u'kṣ'), (u'h', u'jñ'),

    (u'ḷ', u'k'), (u'ḷ', u'kh'), (u'ḷ', u'g'), (u'ḷ', u'gh'), (u'ḷ', u'ṅ'), (u'ḷ', u'c'), (u'ḷ', u'ch'), (u'ḷ', u'j'),
    (u'ḷ', u'z'), (u'ḷ', u'jh'), (u'ḷ', u'ñ'), (u'ḷ', u'ṭ'), (u'ḷ', u'ṭh'), (u'ḷ', u'ḍ'), (u'ḷ', u'ṛ'), (u'ḷ', u'ḍh'),
    (u'ḷ', u'ṛh'), (u'ḷ', u'ṇ'), (u'ḷ', u't'), (u'ḷ', u'th'), (u'ḷ', u'd'), (u'ḷ', u'dh'), (u'ḷ', u'n'), (u'ḷ', u'p'),
    (u'ḷ', u'ph'), (u'ḷ', u'f'), (u'ḷ', u'b'), (u'ḷ', u'bh'), (u'ḷ', u'm'), (u'ḷ', u'y'), (u'ḷ', u'r'), (u'ḷ', u'l'),
    (u'ḷ', u'v'), (u'ḷ', u'ś'), (u'ḷ', u'ṣ'), (u'ḷ', u's'), (u'ḷ', u'h'), (u'ḷ', u'ḷ'), (u'ḷ', u'kṣ'), (u'ḷ', u'jñ')
]
def translit_char(char):

    # --- Latin Single Vowels ---
    if char == 'a':
        ret_val = 'अ'
    if char == 'i':
        ret_val = 'इ'
    if char == 'u':
        ret_val = 'उ'
    if char == 'e':
        ret_val = 'ए'
    if char == 'o':
        ret_val = 'ओ'

    # --- Latin Vowels withu Diacritics ---
    if char == u'ā':  # ā  u'\u0101'
        ret_val = 'आ'
    if char == u'ǡ':  # ǡ  u'\u01e1'
        ret_val = 'ऑ'
    if char == u'ī':  # ī  u'\u012b'
        ret_val = 'ई'
    if char == u'ū':  # ū  u'\u016b'
        ret_val = 'ऊ'
    if char == u'ṛ':  # ṛ u'\u1e5b'
        ret_val = 'ऋ'

    # --- Latin Independent Diftongs ---
    if char == 'ai':
        ret_val = 'ऐ'
    if char == 'au':
        ret_val = 'औ'

    # --- Single Latin Consonants ---
    if char == 'k':
        ret_val = 'क'
    if char == 'g':
        ret_val = 'ग'
    if char == 'c':
        ret_val = 'च'
    if char == 'j':
        ret_val = 'ज'
    if char == 'z':
        ret_val = 'ज़'
    if char == 't':
        ret_val = 'त'
    if char == 'd':
        ret_val = 'द'
    if char == 'n':
        ret_val = 'न'
    if char == 'p':
        ret_val = 'प'
    if char == 'f':
        ret_val = 'फ़'
    if char == 'b':
        ret_val = 'ब'
    if char == 'm':
        ret_val = 'म'
    if char == 'y':
        ret_val = 'य'
    if char == 'r':
        ret_val = 'र'
    if char == 'l':
        ret_val = 'ल'
    if char == 'v':
        ret_val = 'व'
    if char == 's':
        ret_val = 'स'
    if char == 'h':
        ret_val = 'ह'

    # --- Single Latin Consonants with Diacritics ---
    if char == u'\u1e45':  # ṅ
        ret_val = 'ङ'
    if char == u'\u00f1':  # ñ
        ret_val = 'ञ'
    if char == u'\u1e6d':  # ṭ
        ret_val = 'ट'
    if char == u'\u1e0d':  # ḍ
        ret_val = 'ड'
    if char == u'\u1e5b':  # ṛ
        ret_val = 'ड़'
    if char == u'\u1e47':  # ṇ
        ret_val = 'ण'
    if char == u'\u015b':  # ś
        ret_val = 'श'
    if char == u'\u1e63':  # ṣ
        ret_val = 'ष'

    # --- Double Latin Consonants ---
    if char == 'kh':
        ret_val = 'ख'
    if char == 'gh':
        ret_val = 'घ'
    if char == 'ch':
        ret_val = 'छ'
    if char == 'jh':
        ret_val = 'झ'
    if char == 'th':
        ret_val = 'थ'
    if char == 'dh':
        ret_val = 'ध'
    if char == 'ph':
        ret_val = 'फ'
    if char == 'bh':
        ret_val = 'भ'

    if char == u'ṭh':  # .decode('utf-8')
        ret_val = 'ठ'
    if char == u'ḍh':   # .decode('utf-8')
        ret_val = 'ढ'
    if char == u'ṛh':  # .decode('utf-8')
        ret_val = 'ढ़'

    if char == 'll':
        ret_val = 'ळ'

    # --- Nasals ---
    if char == u'\u016b\u0303':  # ū̃
        ret_val = 'ूँ'
    if char == u'\u1ebd':  # ẽ
        ret_val = 'ें'
    if char == u'\u012b\u0303':  # ī̃
        ret_val = 'ीं'
    if char == u'\u0061\u0129':
        ret_val = 'ैं'  # aĩ

    return ret_val


def translit_maatra(char):

    # --- Latin Single Vowels ---
    if char == 'i':
        ret_val = 'ि'  # i
    if char == 'u':
        ret_val = 'ु'  # u
    if char == 'e':
        ret_val = 'े'
    if char == 'o':
        ret_val = 'ो'

    # --- Latin Vowels with Diacritics ---
    if char == u'ā':
        ret_val = 'ा'  # ā u'\u0101'
    if char == u'\u01e1':
        ret_val = 'ॉ'  # ǡ
    if char == u'\u012b':
        ret_val = 'ी'  # ī
    if char == u'\u016b':
        ret_val = 'ू'  # ū
    if char == u'\u1e5b':
        ret_val = 'ृ'  # ṛ

    # --- Latin Matra Diftongs ---
    if char == 'ai':
        ret_val = 'ै'
    if char == 'au':
        ret_val = 'ौ'

    # --- Latin Matra Diftongs with Diacritics ---
    if char == u'a\u0129':  # aĩ
        ret_val = 'ैं'

    return ret_val


def latin_to_deva(lat_word):

    lat_word = lat_word.decode('utf-8')

    lat_char_list = []

    # --- Create w_list (Word as Latin list) ---
    for i, lat_char in enumerate(lat_word):

        prev_lat_char = lat_word[i - 1]

        # --- process multilatin ---

        # --- kh ---
        if lat_char == 'h' and prev_lat_char == 'k':
            lat_char_list.append('kh')
            lat_char_list.pop(i - 1)
            continue
        # --- gh ---
        if lat_char == 'h' and prev_lat_char == 'g':
            lat_char_list.append('gh')
            lat_char_list.pop(i - 1)
            continue
        # --- ch ---
        if lat_char == 'h' and prev_lat_char == 'c':
            lat_char_list.append('ch')
            lat_char_list.pop(i - 1)
            continue
        # --- jh ---
        if lat_char == 'h' and prev_lat_char == 'j':
            lat_char_list.append('jh')
            lat_char_list.pop(i - 1)
            continue
        # --- th ---
        if lat_char == 'h' and prev_lat_char == 't':
            lat_char_list.append('th')
            lat_char_list.pop(i - 1)
            continue
        # --- dh ---
        if lat_char == 'h' and prev_lat_char == 'd':
            lat_char_list.append('dh')
            lat_char_list.pop(i - 1)
            continue
        # --- ph ---
        if lat_char == 'h' and prev_lat_char == 'p':
            lat_char_list.append('ph')
            lat_char_list.pop(i - 1)
            continue
        # --- bh ---
        if lat_char == 'h' and prev_lat_char == 'b':
            lat_char_list.append('bh')
            lat_char_list.pop(i - 1)
            continue
        # --- ṭh ---
        if lat_char == 'h' and prev_lat_char == u'ṭ':
            lat_char_list.append(u'ṭh')
            lat_char_list.pop(i - 1)
            continue
        # --- ḍh ---
        if lat_char == 'h' and prev_lat_char == u'ḍ':
            lat_char_list.append(u'ḍh')
            lat_char_list.pop(i - 1)
            continue
        # --- ṛh ---
        if lat_char == 'h' and prev_lat_char == u'ṛ':
            lat_char_list.append(u'ṛh')
            lat_char_list.pop(i - 1)
            continue

        # --- process nasals built of several Unicode points ---
        # --- ū̃ ---
        if lat_char == u'\u0303' and prev_lat_char == u'\u016b':
            lat_char_list.append(u'\u016b\u0303')
            lat_char_list.pop(i - 1)
            continue

        if lat_char == u'\u0303' and prev_lat_char == u'\u012b':
            lat_char_list.append(u'\u012b\u0303')
            lat_char_list.pop(i - 1)
            continue

        # --- Process diftongs ---
        # --- ai ---
        if lat_char == 'i' and prev_lat_char == 'a':
            lat_char_list.append('ai')
            lat_char_list.pop(i - 1)
            continue
        # --- au ---
        if lat_char == 'u' and prev_lat_char == 'a':
            lat_char_list.append('au')
            lat_char_list.pop(i - 1)
            continue
        # --- aĩ ---
        if lat_char == u'ĩ' and prev_lat_char == 'a':
            lat_char_list.append(u'aĩ')
            lat_char_list.pop(i - 1)
            continue

        lat_char_list.append(lat_char)

    #return lat_char_list  # DEBUG

    # --- Translitterate Latin-->Hindi ---
    deva_char_string = ''

    for i, lat_item in enumerate(lat_char_list):

        prev_lat_item = lat_char_list[i - 1]

        # --- process first character ---
        if i == 0:
            deva_char_string = deva_char_string + translit_char(lat_item)
            continue

        # --- process a ---
        if lat_item == 'a':
            continue

        # --- process conjuncts ---
        conjunct_tuple = (prev_lat_item, lat_item)
        if conjunct_tuple in conjunct_tuple_list:
            deva_char_string = deva_char_string[:-3]
            deva_char_string = deva_char_string + translit_char(prev_lat_item) + '्' + translit_char(lat_item)
            continue

        # --- process aspirated consonants ---
        #if lat_item in aspirated_consonants:
        #    deva_char_string = deva_char_string + translit_char(lat_item)
        #    continue

        # --- process simple matra after aspirated consonant ---
        #if lat_item in vowels and prev_lat_item in aspirated_consonants:
        #    deva_char_string = deva_char_string + translit_maatra(lat_item)
        #    continue

        # --- process simple matra ---
        if lat_item in vowels and prev_lat_item in consonants:
            deva_char_string = deva_char_string + translit_maatra(lat_item)
            continue

        # --- process diftong matra ---
        if lat_item in diftongs and prev_lat_item in consonants:
            deva_char_string = deva_char_string + translit_maatra(lat_item)
            continue

        deva_char_string = deva_char_string + translit_char(lat_item)

    return deva_char_string


print latin_to_deva('jhalāī')


# Test words:
# namaste, gra, bolnā, jjh, puchie, kaise, kǡlej, hū̃, karū̃, auratẽ, haĩ, beṭõ, jhalāī

# ā, ǡ, ī, ū, ẽ, ṛ, õ, ī̃
# ĩ  # tilde
# ṅ, ñ, ṭ, ḍ, ṛ, ṇ, ś, ṣ
# ṭh ḍh ṛh