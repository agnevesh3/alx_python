#!/usr/bin/python3
def multiple_returns(sentence):
    tup = tuple(sentence)
    if len(sentence) > 0:
        length = len(tup)
        first = tup[0]
    else:
        length = len(tup)
        first = None
    return length, first
