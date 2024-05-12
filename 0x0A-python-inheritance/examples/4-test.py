#!/usr/bin/python3

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age):
        self.sName = name
        self.sAge = age

        super().__init__("Rahul", age)

    def displayInfo(self):
        print(self.sName, self.sAge)


obj = Student("Maynak", 23)
obj.display()
obj.displayInfo()
