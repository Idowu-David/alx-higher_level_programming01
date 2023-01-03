#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) in range(97, 124):
            let = ord(letter) - 32
        else:
            let = ord(letter)
        print("{}".format(chr(let)), end="")
    print()
