import math
from Operations.basic import error


def power(x,y):
    try:
        if float(x) == 0:
            return 0
        if y == 0:
            return 1
        return float(x) ** y
    except:
        return error()


def root(x,y):
    try:
        if float(x) == 0:
            return 0
        if y == 0:
            return 1
        return float(x) ** (1/y)
    except:
        return error()


