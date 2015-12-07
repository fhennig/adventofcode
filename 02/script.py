#! /usr/bin/env python3
from sys import argv

class Box:
    def __init__(self, l, w, h):
        self.l = l
        self.w = w
        self.h = h

    def wrapping_paper_size(self):
        side1 = self.l * self.h
        side2 = self.l * self.w
        side3 = self.w * self.h
        smallest = min(side1, side2, side3)
        return 2*side1 + 2*side2 + 2*side3 + smallest

    def ribbon_len(self):
        s1, s2, _ = sorted([self.l, self.w, self.h])
        bow_len = self.l * self.w * self.h
        return 2 * s1 + 2 * s2 + bow_len
    

def read_dimensions(filename):
    boxes = []
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            l = l.strip()
            dim = [int(x) for x in l.split('x')]
            boxes.append(Box(*dim))
    return boxes


def main(filename):
    boxes = read_dimensions(filename)
    paper = sum([box.wrapping_paper_size() for box in boxes])
    ribbon = sum([box.ribbon_len() for box in boxes])
    return paper, ribbon


if __name__ == "__main__":
    if len(argv) > 1:
        print(main(argv[1]))
        
        
