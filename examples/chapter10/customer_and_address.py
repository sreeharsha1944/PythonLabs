#!/usr/bin/env python3
class Address:
    def __init__(self, street, city, state, zip):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
    def __str__(self):
        return self.street + "\n" + self.city + ", " + \
               self.state + " " + self.zip
       
class Customer:
    def __init__(self, firstName, lastName, address):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address

    def __str__(self):
        return self.firstName + " " + self.lastName + \
               "\n" + str(self.address)