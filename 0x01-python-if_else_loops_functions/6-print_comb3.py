#!/usr/bin/python3

for digit_1 in range(0, 9):
    for digit_2 in range(digit_1 + 1, 10):
        if digit_1 == 8 and digit_2 == 9:
            print("{}{}".format(digit_1, digit_2))
        else:
            print("{}{}".format(digit_1, digit_2), end=", ")
