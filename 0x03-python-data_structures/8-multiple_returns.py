#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
    str_len = len(sentence)
    fir_char = sentence[0]
    new_tuple = (str_len, fir_char)
    return new_tuple
