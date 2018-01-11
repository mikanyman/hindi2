# -*- coding: utf-8 -*-

import re

filepath = 'C:\Users\Mika\Desktop\AWARENESS\Process Files\kk.txt'
pattern = re.compile('^\[\'(\w+)a\'\,.*$')  # compile pattern

with open(filepath) as fp:
   for line in fp:
       match = re.findall(pattern, line)
       print str(match) + " : " + line
       #regex = r"^\[\'(\w+)a\'\,.*$"


       #cleaned_line = pattern.sub(' ', line).strip()
       #line_buffer[line_counter] = cleaned_lineextracted

