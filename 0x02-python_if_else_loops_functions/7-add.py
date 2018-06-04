#!/usr/bin/python3
def add(a, b):
    if type(a) and type(b) is int:
        return a + b
    else:
        return "not a number"
print(add(1, 2))
print(add(98, 0))
print(add(100, -2))
