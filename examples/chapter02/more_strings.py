#!/usr/bin/env python3
word = "is"
sentence = "The capital of Mississippi is Jackson."
position = sentence.find(word)
print(position)
print(sentence.find(word, position + 1))
print(sentence.find(word, 8, 12))
print("The word", word, "appears", sentence.count(word),
      "times in the sentence:\n", sentence)
padded_string = word.rjust(15)
print(padded_string)
print(word.rjust(15, "*"))

data = "1 4 1 1abc"
new_data = data.replace("1", "0")
print(new_data)
new_data = data.replace("1", "0", 2)
print(new_data)
print()

pieces = data.split(' ')
print(data)
print("pieces is of type:", type(pieces))
print(pieces)
