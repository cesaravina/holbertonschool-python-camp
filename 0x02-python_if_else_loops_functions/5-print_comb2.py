#!/usr/bin/python3
for num in range (0, 100):
    if num < 10:
        print("0{}, ".format(num), end='')
    elif num >= 10:
        print("{}, ".format(num), end='')
