#!/usr/bin/env python3
class Student:

    def __init__(self, name, major):
        self.name = name    # Calls the @name.setter method
        self.major = major  # Calls the @major.setter method

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # print("Debug:", "name setter being called")
        self._name = name

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        # print("Debug:", "major setter being called")
        self._major = major


def main():
    jeff = Student("Jeff", "American History")
    heather = Student("Heather", "Mathematics")
    print(jeff.name, ":", jeff.major)
    jeff.name = "Jeffrey"
    print(jeff.name, ":", jeff.major)
    heather.major = "Computer Science"
    print(heather.name, ":", heather.major)


if __name__ == "__main__":
    main()
