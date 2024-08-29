#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

woofie = Dog("dan", "whitie")
print(woofie.breed)
print(woofie.name)