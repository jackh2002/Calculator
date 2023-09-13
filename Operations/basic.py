import math


def add(x, y):
    try:
        return float(x) + float(y)
    except ValueError:
        return error()


def multiply(x,y):
    try:
        return float(x) * float(y)
    except:
        return error()


def divide(x, y):
    try:
        return float(x) / float(y)
    except:
        return error()


def subtract(x, y):
    try:
        return float(x) - float(y)
    except:
        return error()

def error():
    return "ERROR, PLEASE RESET"
