#! /usr/bin/env python3
from sys import argv
import numpy as np


instructions = {'^': ( 0, -1),
                '>': ( 1,  0),
                'v': ( 0,  1),
                '<': (-1,  0)}


def read_instructions(filename):
    instrs = []
    with open(filename) as f:
        text = f.read().strip()
        for c in text:
            instrs.append(instructions[c])
    return instrs


def split_list(l, n):
    lists = [[] for i in range(n)]
    for i, item in enumerate(l):
        index = i % n
        lists[index].append(item)
    return lists


def execute_instructions(pos, instrs):
    path = [np.array(pos)]
    for i, instr in enumerate(instrs):
        path.append(path[i] + instr)
    path = [tuple(pos) for pos in path]
    return path


def main(filename):
    start_pos = (0, 0)
    robot_count = 2
    instrs = read_instructions(filename)
    # santa goes alone
    path = execute_instructions(start_pos, instrs)
    houses = set(path)
    print(len(houses))
    # santa with robo-santa
    instrss = split_list(instrs, robot_count)
    paths = [execute_instructions(start_pos, instrs)
             for instrs in instrss]
    houses2 = set(sum(paths, []))
    print(len(houses2))


if __name__ == "__main__":
    if (len(argv) > 1):
        main(argv[1])
    







