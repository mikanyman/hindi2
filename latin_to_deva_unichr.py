# -*- coding: utf-8 -*-

import unicodedata

class ucp:
    name = unicodedata.name(u'क')
    category = unicodedata.category(u'क')
    medial = 'ka'
    final = 'k'

print ucp.name

