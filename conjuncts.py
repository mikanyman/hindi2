# -*- coding: utf-8 -*-


#k̲k̲ क्क # kk
#k = 'k̲k̲h̲'.decode('utf-8')
#print k # क्ख
#print 'k̲k̲h̲'.decode('utf-8')

#Under the hood, Python represents Unicode strings as either 16- or 32-bit integers

#>>> unichr(40960)
#u'\ua000'
#>>> ord(u'\ua000') # a Unicode string of length 1
#40960

kkh = unicode('k̲k̲h̲', encoding='utf-8') # OK converts string to unicode using specific encoding
#print type(kkh) # <type 'unicode'>

def translit_conjuncts(str):
    str_utf8 = str.decode('utf-8');
    """
    ka  kha ga  gha ṅa
    ca  cha ja  jha ña
    ṭa  ṭha ḍ   ḍha ṛha ṇa
    ta  tha da  dha na
    pa  pha fa  ba  bha ma
    ya  ra  la  lla
    va  śa  ṣa  sa  ha
    
    k  kh g  gh ṅ
    c  ch j  jh ñ
    ṭ  ṭh ḍ   ḍh ṛh ṇ
    t  th d  dh n
    p  ph f  b  bh m
    y  r  l  ll
    v  ś  ṣ  s  h
    """
    # --- Conjuncts with क ---
    k_k_utf8 = 'k̲k̲'.decode('utf-8')
    if str_utf8 == k_k_utf8: return 'क्क'

    k_kh_utf8 = 'k̲k̲h̲'.decode('utf-8')
    if str_utf8 == k_kh_utf8: return 'क्ख'

    k_g_utf8 = 'k̲g̲'.decode('utf-8')
    if str_utf8 == k_g_utf8: return 'क्ग'

    k_gh_utf8 = 'k̲g̲h̲'.decode('utf-8')
    if str_utf8 == k_gh_utf8: return 'क्घ'

    k_ndotabove_utf8 = 'k̲ṅ̲'.decode('utf-8')
    if str_utf8 == k_ndotabove_utf8: return 'xx'

    k_c_utf8 = 'c̲'.decode('utf-8')
    if str_utf8 == k_c_utf8: return 'xx'

    k_ch_utf8 = 'c̲h̲'.decode('utf-8')
    if str_utf8 == k_ch_utf8: return 'xx'

    k_j_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_j_utf8: return 'xx'

    k_jh_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_jh_utf8: return 'xx'

    k_ntilde_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_ntilde_utf8: return 'xx'

    k_tdotbelow_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_tdotbelow_utf8: return 'xx'

    k_tdotbelowh_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_tdotbelowh_utf8: return 'xx'

    k_ddotbelow_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_ddotbelow_utf8: return 'xx'

    k_ddotbelowh_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_ddotbelowh_utf8: return 'xx'

    k_rdotbelowh_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_rdotbelowh_utf8: return 'xx'

    k_ndotbelow_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_ndotbelow_utf8: return 'xx'

    k_t_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_t_utf8: return 'xx'

    k_th_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_th_utf8: return 'xx'

    k_d_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_d_utf8: return 'xx'

    k_dh_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_dh_utf8: return 'xx'

    k_n_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_n_utf8: return 'xx'

    k_p_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_p_utf8: return 'xx'

    k_ph_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_ph_utf8: return 'xx'

    k_f_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_f_utf8: return 'xx'

    k_b_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_b_utf8: return 'xx'

    k_bh_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_bh_utf8: return 'xx'

    k_m_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_m_utf8: return 'xx'

    k_y_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_y_utf8: return 'xx'

    k_r_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_r_utf8: return 'xx'

    k_l_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_l_utf8: return 'xx'

    k_ll_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_ll_utf8: return 'xx'

    k_v_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_v_utf8: return 'xx'

    k_sacute_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_sacute_utf8: return 'xx'

    k_sdotbelow_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_sdotbelow_utf8: return 'xx'

    k_s_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_s_utf8: return 'xx'

    k_h_utf8 = 'xxx'.decode('utf-8')
    if str_utf8 == k_h_utf8: return 'xx'

# CALL
print translit_conjuncts('k̲k̲h̲')