#!/usr/bin/env python3
from sys import argv, stdout
import re
import operator as ops
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)
h = logging.StreamHandler()
h.setLevel(logging.INFO)
# added in main()
#log.addHandler(h) 


### Helpers ###

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


### Representation of Gates ###

class Gate:
    def __init__(self, op, *args):
        self.parents = args
        self.op = op

    def get_value(self, circuit):
        log.info("resolving gate %s", self.op)
        vals = [circuit.get_value(v) for v in self.parents]
        return self.op(*vals)
    
def NotGate(p):
    return Gate(ops.inv, p)

def AndGate(*ps):
    return Gate(ops.and_, *ps)

def OrGate(*ps):
    return Gate(ops.or_, *ps)


class LinkGate:
    def __init__(self, p):
        self.p = p

    def get_value(self, circuit):
        log.info("resolving link %s", self.p)
        return circuit.get_value(self.p)


class ShiftGate:
    def __init__(self, op, p, val):
        self.op = op
        self.p = p
        self.val = val

    def get_value(self, circuit):
        log.info("resolving shift %s", self.op)
        return self.op(circuit.get_value(self.p),
                       circuit.get_value(self.val))

def RShiftGate(p, val):
    return ShiftGate(ops.rshift, p, val)

def LShiftGate(p, val):
    return ShiftGate(ops.lshift, p, val)


### Parsing ###

def parse_line(l):
    l = l.split()
    r = l[-1]
    l = l[:-2]
    if "NOT" in l:
        return {r: NotGate(l[1])}
    elif "AND" in l:
        l.remove("AND")
        return {r: AndGate(*l)}
    elif "OR" in l:
        l.remove("OR")
        return {r: OrGate(*l)}
    elif "RSHIFT" in l:
        l.remove("RSHIFT")
        return {r: RShiftGate(*l)}
    elif "LSHIFT" in l:
        l.remove("LSHIFT")
        return {r: LShiftGate(*l)}
    else:
        return {r: LinkGate(*l)}


def parse_circuit(filename):
    lines = []
    with open(filename) as f:
        lines = f.readlines()
    structure = {}
    for l in lines:
        structure.update(parse_line(l))
    return Circuit(structure)


class Circuit:
    def __init__(self, structure):
        self.structure = structure
        self.memoized = {}

    def get_value(self, s):
        log.info("looking for: %s", s)
        if is_int(s):
            log.info("int")
            return int(s)
        elif s in self.memoized:
            log.info("memoized")
            return self.memoized[s]
        else:
            log.info("looking it up")
            v = self.structure[s].get_value(self)
            self.memoized.update({s: v})
            return v


### Main ###
        
def main(filename, v, logging=False):
    if logging:
        log.addHandler(h)
    c = parse_circuit(filename)
    val = c.get_value(v)
    print(val)
    # Part 2
    c.memoized = {"b": val}
    print(c.get_value(v))


if __name__ == "__main__":
    if len(argv) > 2:
        main(*argv[1:])
