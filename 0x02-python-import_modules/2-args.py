#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    argv = []
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for x in range(len(sys.argv)):
        if x >= 1:
            argv.append(sys.argv[x])
            print("{}: {}".format(x, sys.argv[x]))
