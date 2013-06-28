# coding=utf-8
"""Mantra 5: Don't self obfusicate your code."""


# Taken from http://p-nand-q.com/python/obfuscated_python.html

# No normal human will ever make sense of this

fibonacci = lambda x:map(lambda o:(map(lambda c:map(lambda l:
o.__setslice__(l[0],l[1],l[2]),([o[2]+3,o[2]+4,[o[0]]],[0,3,[o[1],
reduce(lambda x,o:x+o,o[:2]),o[2]+1]])),range(x)),o)[1],[[1,1,0]+
range(x)])[0][3:]

print fibonacci(20)


def obfusicated():
    """Some hard to read code."""
    crn_ln = 100
    hgt = 200
    rslt = crn_ln + hgt
    return rslt


def clear():
    """Some easy to read code."""
    corner_length = 100
    height = 200
    result = corner_length + height
    return result
