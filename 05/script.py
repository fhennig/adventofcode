#!/usr/bin/env python3
from sys import argv


vowels = "aeiou"
forbidden = ["ab", "cd", "pq", "xy"]


def is_nice(string):
    three_vowels = len([c for c in string if c in vowels]) >= 3
    double = len([c for i, c in enumerate(string[:-1]) if string[i] == string[i+1]]) > 0
    no_forbiddens = all([False for s in forbidden if s in string])
    return three_vowels and double and no_forbiddens


def is_nice2(s):
    a = any(map(lambda i: s[i:i+2] in s[i+2:], range(len(s[:-2]))))
    b = any(map(lambda i: s[i] == s[i+2], range(len(s[:-2]))))
    return a and b
    

def main(filename):
    strs = []
    with open(filename) as f:
        strs = f.readlines()
    nice_strs = filter(lambda s: is_nice(s.strip()), strs)
    print(len(list(nice_strs)))
    nice_strs2 = filter(lambda s: is_nice2(s.strip()), strs)
    print(len(list(nice_strs2)))


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
