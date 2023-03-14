#!/usr/bin/python3
"""Human module"""


class Human:
    """
    Represents Human Being
    """

    """Human population"""
    population = 0

    def __init__(self, name, gender, age):
        print("Initialising human")
        self.name = name
        self.gender = gender
        self.age = age
        Human.population += 1

    def walk(self):
        print("Person can walk")

    def run(self):
        print("Person can run")

    @classmethod
    def human_population(cls):
        print("We are {} in number".format(cls.population))

person_1 = Human("Zak", "M", 29)
print(person_1.name)
Human.human_population()
person_2 = Human("Moh", "M", 27)
print(person_2.name)
Human.human_population()
person_3 = Human("Koo", "M", 25)
print(person_3.name)
Human.human_population()
print("The entire human population is {}".format(Human.population))
