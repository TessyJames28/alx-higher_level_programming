#!/usr/bin/python3


for letters in range(ord('z'), ord('a') - 1, -1):
    if letters % 2 == 1:
        letters = letters - 32
    print("{}".format(chr(letters)), end="")
