#!/usr/bin/env python3
# Define the strings that are used multiple times
prompts = ["Please enter some first names ", "again ",
           "to delete "]
end = "\n" * 2  # define value to use as end in prints

# Using str.join to efficiently join together strings by
# avoiding string concatentation
msg1 = prompts[0]
msg2 = "".join(prompts[:2])
msg3 = "".join(prompts)

nameList = input(msg1).split()
uniqueNames = set(nameList)
backedupNames = set(uniqueNames)
print(uniqueNames, end=end)

# Check to see if name exists prior to adding
nameList = input(msg2).split()
for name in nameList:
    if name not in uniqueNames:
        uniqueNames.add(name)
    else:
        print("\t", name, "already exists and is ignored")
print(uniqueNames, end=end)

# Update contents of set with contents of a list
nameList = input(msg2).split()
uniqueNames.update(nameList)
print(uniqueNames, end=end)

# Check to see if name exists prior to removing
nameList = input(msg3).split()
for name in nameList:
    if name in uniqueNames:
        uniqueNames.remove(name)

# Discard words without checking first
nameList = input(msg3).split()
for name in nameList:
    uniqueNames.discard(name)
print(uniqueNames, end=end)

# Check the relationship of one set to another
print()
print("Original:", backedupNames)
print("Current :", uniqueNames, "\n")
print("Original is subset of Current ? ",
      backedupNames.issubset(uniqueNames))
print("Current is superset of Original ? ",
      uniqueNames.issuperset(backedupNames))

# Pop each element from the set until it is empty
print("Popping each name from set: ", uniqueNames)
while uniqueNames:
    print(uniqueNames.pop(), end=" ")
print()
