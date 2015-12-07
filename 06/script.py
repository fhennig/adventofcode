#!/usr/bin/env python3
from sys import argv
from enum import Enum
import re
import numpy as np


Command = Enum("Command", "TurnOn TurnOff Toggle")


def parse_position(s):
    x, y = s.split(",")
    return int(x), int(y)


def parse_instruction(s):
    p1, p2 = re.findall("\d+,\d+", s)
    p1, p2 = parse_position(p1), parse_position(p2)
    p2 = (p2[0] + 1, p2[1] +1)
    cmd = None
    if re.search("turn on", s):
        cmd = Command.TurnOn
    elif re.search("turn off", s):
        cmd = Command.TurnOff
    elif re.search("toggle", s):
        cmd = Command.Toggle
    else:
        raise AssertionError("No command found in string: " + s)
    return cmd, p1, p2


def read_instructions(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    instructions = [parse_instruction(l) for l in lines]
    return instructions


class Field:
    def __init__(self, dim):
        self.f = np.full((dim, dim), False)


    def execute_instructions(self, instrs):
        for cmd, p1, p2 in instrs:
            if cmd == Command.TurnOn:
                self.turn_on(*p1, *p2)
            elif cmd == Command.TurnOff:
                self.turn_off(*p1, *p2)
            elif cmd == Command.Toggle:
                self.toggle(*p1, *p2)


    def update(self, x1, y1, x2, y2, fn):
        for y in range(y1, y2):
            for x in range(x1, x2):
                self.f.itemset((x, y), fn(self.f[x, y]))


    def turn_off(self, x1, y1, x2, y2):
        self.update(x1, y1, x2, y2, lambda x: False)
        

    def turn_on(self, x1, y1, x2, y2):
        self.update(x1, y1, x2, y2, lambda x: True)


    def toggle(self, x1, y1, x2, y2):
        self.update(x1, y1, x2, y2, lambda x: not x)


class Field2:
    def __init__(self, dim):
        self.f = np.full((dim, dim), 0)


    def execute_instructions(self, instrs):
        for cmd, p1, p2 in instrs:
            if cmd == Command.TurnOn:
                self.turn_on(*p1, *p2)
            elif cmd == Command.TurnOff:
                self.turn_off(*p1, *p2)
            elif cmd == Command.Toggle:
                self.toggle(*p1, *p2)


    def update(self, x1, y1, x2, y2, fn):
        for y in range(y1, y2):
            for x in range(x1, x2):
                self.f.itemset((x, y), fn(self.f[x, y]))


    def turn_off(self, x1, y1, x2, y2):
        self.update(x1, y1, x2, y2, lambda x: max([0, x - 1]))
        

    def turn_on(self, x1, y1, x2, y2):
        self.update(x1, y1, x2, y2, lambda x: x + 1)


    def toggle(self, x1, y1, x2, y2):
        self.update(x1, y1, x2, y2, lambda x: x + 2)


def main(filename):
    instrs = read_instructions(filename)
    f = Field(1000)
    f.execute_instructions(instrs)
    print(int(sum(sum(f.f))))
    f2 = Field2(1000)
    f2.execute_instructions(instrs)
    print(int(sum(sum(f2.f))))


if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
