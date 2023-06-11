#!/usr/bin/python3
def multiple_returns(sentence):
    len = len(sentence)
    c = sentence[0] if len > 0 else None

    return (len, c)
