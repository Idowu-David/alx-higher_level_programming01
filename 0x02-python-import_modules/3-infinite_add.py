#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    l = len(arg) - 1
    add = 0
    if l == 0:
        print("{:d}".format(0))
    else:
        for num in range(l):
            add = add + int(arg[num + 1])
        print(add)
