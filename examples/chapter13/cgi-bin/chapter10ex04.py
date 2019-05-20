#!/usr/bin/env python3
#
# A Solution For Chapter 10 Exercise 4
#
import sys
file = open("DATA", "r")

lines = file.readlines()
file.close()

map = {}

for line in lines:
        name, typ, amount = line.split()
        ctm = map.get(name)
        if ctm:
                value = ctm.get(typ)
                if value:
                        ctm[typ] += int(amount)
                else:
                        ctm[typ] = int(amount)
        else:
                map[name] = { typ : int(amount) }

print(map)
