# -*- coding: utf-8 -*-

from HindiTokenizer import Tokenizer

def tokenize():
    t = Tokenizer("यह वाक्य हिन्दी में है।")
    t.tokenize()
    return t


