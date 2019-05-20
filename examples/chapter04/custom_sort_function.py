#!/usr/bin/env python3
def the_last_word(aString):
    fmt = "For Input: {:18}    Sort Using: {}"
    last_word = aString.strip().split()[-1]
    print(fmt.format(aString, last_word))
    return last_word


names = """Ava Smith, Ethan Johnson, Abigail Williams, \
Sophia Brown, Michael Jones, Emily Miller, Declan Lee"""
names = names.split(", ")
print(names)
names.sort(key=the_last_word)
print(names)
