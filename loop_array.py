# -*- coding: utf-8 -*-

import unicodedata

c = unichr(0x915)
d = 2325

print c,unicodedata.name(c)
print u'\N{DEVANAGARI LETTER KA}'
print u'\u0915'

print u''.join(unichr(c) for c in range(0x900,0x980))

# Omia:
#print u'\n'.join(unichr(c) for c in range(0x900,0x980))

# Combining Diacritical Marks
#print u''.join(unichr(c) for c in range(0x300,0x36F))

#print u'\uE02B' EI TOIMI

