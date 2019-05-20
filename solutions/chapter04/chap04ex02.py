#!/usr/bin/env python3
""" A Solution For Chapter 4 Exercise 2

    Use a single set to determine the number of unique words in the
    user's input.
    • The same sample while loop from exercise #1 can be used here.
    • Each time through the loop the individual words should be added
      to the single set.
    • When done looping, output the contents of the set sorted
      alphabetically!
    • Also, output the number of unique words.
"""
words = set()

prompt = "Enter a some text (or just the word 'end' to quit) "
while True:
    data = input(prompt)
    if data == "end":
        break
    # Remainder of while loop goes here
    words.update(data.split())

the_list = sorted(words)

for word in the_list:
    print(word)

print(len(the_list), "words in all")
