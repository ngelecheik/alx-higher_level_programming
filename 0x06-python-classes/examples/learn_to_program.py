#!/usr/bin/python3
"""This are examples from the youtube playlist - learn to program
https://www.youtube.com/watch?v=1AGyBuVCTeE
"""
class Dog:
    def __init__(self, name="", height=0, weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))
    def eat(self):
        print("{} the dog eats".format(self.name))
    def barks(self):
        print("{} the dog barks".format(self.name))

def main():
    spot = Dog("Spot", 66,26)
    spot.barks()

    bowser = Dog()
    bowser.barks()
main()