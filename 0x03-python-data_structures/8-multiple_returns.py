#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    fir_char = sentence[0]
    if str_len == 0:
        new_tuple = (strlen, None)
    else:
        new_tuple = (str_len, fir_char)
    return new_tuple
