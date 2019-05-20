the_map = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

number = input("Enter a number: ")

for digit in number:
    print(the_map[int(digit)], end=" ")

print()
