#!/usr/bin/env python3
from sys import argv
import hashlib as hl
import itertools as it


def good_key(k):
    return hl.md5(k.encode('utf-8')).hexdigest()[:5] == "00000"


def make_key(text, i):
    return text + str(i)


# def main2(text):
#     ints = it.count(1)
#     valid_ints = filter(lambda i: good_key(make_key(text, i)), ints)
#     return valid_ints


def main(text):
    i = 1
    while not good_key(make_key(text, i)):
        i += 1
    return i


if __name__ == "__main__":
    if len(argv) > 1:
        print(main(argv[1]))
    else:
        print(main("yzbqklnj"))
