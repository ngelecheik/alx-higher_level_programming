#!/usr/bin/python3
"""we now inser a str method and see what happens"""


class A:
    def __str__(self):
        return "42"

a = A()
print(repr(a))
print(str(a))
