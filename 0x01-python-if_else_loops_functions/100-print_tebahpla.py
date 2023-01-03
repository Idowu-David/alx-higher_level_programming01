#!/usr/bin/python3

for i in range(122, 96, -1):
    if i % 2 == 1:
        alp = i - 32
    else:
        alp = i
    print("{}".format(chr(alp)), end="")
