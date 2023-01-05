#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1
    argv = sys.argv[1:]
    if l == 0:
        print("{} arguments.".format(l))
    else:
        index = 1
        print("{} arguments:".format(l))
        for arg in argv:
            print("{:d}: {}".format(index, sys.argv[index]))
            if index != l:
                index += 1
