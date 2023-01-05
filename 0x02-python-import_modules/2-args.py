#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    _len = len(sys.argv) - 1
    argv = sys.argv[1:]
    if _len == 0:
        print("{} arguments.".format(_len))
    else:
        index = 1
        if _len == 1:
            print("{} argument.".format(_len))
        else:
            print("{} arguments:".format(_len))
        for arg in argv:
            print("{:d}: {}".format(index, sys.argv[index]))
            if index != _len:
                index += 1
