#! /usr/bin/env python3


def execute_instructions(start, instructions):
    pos = start
    keller_pos = -1
    for i, c in enumerate(instructions):
        if pos < 0 and keller_pos < 0:
            keller_pos = i
        if c == "(":
            pos += 1
        elif c == ")":
            pos -= 1
    return pos, keller_pos
            


def main():
    code = ""
    with open("input.txt") as f:
        code = f.read().strip()
    pos, k = execute_instructions(0, code)
    print(pos, k)


if __name__ == "__main__":
    main()
    

