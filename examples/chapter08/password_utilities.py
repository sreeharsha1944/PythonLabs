#!/usr/bin/env python3
from password_errors import *


def checkTrivial(password):
    bad = ["password", "p@ssword", "passw0rd", "p@ssw0rd"]
    if password.lower() in bad:
        raise TrivialPasswordError(password)


def checkLength(password):
    min_length = 10
    length = len(password)
    if length < min_length:
        raise PasswordLengthError("Too short", length)


def checkDuplicates(password):
    removedupes = set(password)
    if len(removedupes) < len(password):
        raise RepetetiveError("Repetetive Characters Exist")
