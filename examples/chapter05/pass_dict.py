#!/usr/bin/env python3
def update_stickers(the_students, sticker):
    sticker_lists = list(the_students.values())
    for stickers in sticker_lists:
        stickers.append(sticker)


def print_students(students):
    for name, stickers in students.items():
        print("{:>8}:".format(name), " ".join(stickers))


students = {'declan': [" 🦋 ", " 🦉 ", " 🦂 ", " 🦒 "],
            'jill': [" 🦆 ", " 🦓 ", " 🦎 ", " 🦁 "],
            'sam': [" 🦖 ", " 🦂 ", " 🦗 "]}

print_students(students)
update_stickers(students, " 🦈 ")
print("*" * 50)
print_students(students)
